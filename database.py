"""
SQLite Persistence Layer for the Polymarket Paper Trading Simulator.
Tracks virtual USDC balance, peak equity, drawdown kill-switch, open & closed positions,
order book executions, calibration metrics (Brier score), and rejected opportunities.
"""

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


DEFAULT_DB_PATH = Path(__file__).resolve().parent / "data" / "polymarket_sim.db"


class SimDatabase:
    def __init__(self, db_path: Path = DEFAULT_DB_PATH, initial_capital: float = 50.0) -> None:
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.initial_capital = initial_capital
        self._init_schema()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        return conn

    def _init_schema(self) -> None:
        with self._connect() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS portfolio_state (
                    id INTEGER PRIMARY KEY CHECK (id = 1),
                    initial_capital REAL NOT NULL,
                    cash_usdc REAL NOT NULL,
                    locked_usdc REAL NOT NULL,
                    total_equity REAL NOT NULL,
                    peak_equity REAL NOT NULL,
                    max_drawdown_pct REAL NOT NULL,
                    current_drawdown_pct REAL NOT NULL,
                    monthly_target_usdc REAL NOT NULL DEFAULT 60.0,
                    halted INTEGER NOT NULL DEFAULT 0,
                    halt_reason TEXT DEFAULT '',
                    active_category_filter TEXT DEFAULT 'ALL',
                    min_liquidity_filter REAL NOT NULL DEFAULT 5000.0,
                    max_slippage_filter REAL NOT NULL DEFAULT 0.03,
                    updated_at TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS positions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    market_id TEXT NOT NULL,
                    question TEXT NOT NULL,
                    category TEXT NOT NULL,
                    side TEXT NOT NULL,            -- 'YES' or 'NO'
                    token_id TEXT NOT NULL,
                    status TEXT NOT NULL,          -- 'OPEN', 'CLOSED', 'RESOLVED'
                    shares REAL NOT NULL,
                    entry_vwap REAL NOT NULL,
                    cost_usdc REAL NOT NULL,
                    current_bid REAL NOT NULL,
                    market_value_usdc REAL NOT NULL,
                    unrealized_pnl REAL NOT NULL,
                    exit_vwap REAL DEFAULT 0.0,
                    proceeds_usdc REAL DEFAULT 0.0,
                    realized_pnl REAL DEFAULT 0.0,
                    initial_p_est REAL NOT NULL,
                    latest_p_est REAL NOT NULL,
                    entry_edge REAL NOT NULL,
                    kelly_full_pct REAL NOT NULL,
                    kelly_half_pct REAL NOT NULL,
                    applied_size_pct REAL NOT NULL,
                    roundtrip_slippage_pct REAL NOT NULL,
                    official_source TEXT NOT NULL,
                    exit_condition TEXT NOT NULL,
                    rationale TEXT NOT NULL,
                    exit_reason TEXT DEFAULT '',
                    end_date_iso TEXT NOT NULL,
                    opened_at TEXT NOT NULL,
                    closed_at TEXT DEFAULT ''
                );

                CREATE TABLE IF NOT EXISTS trades_ledger (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    position_id INTEGER NOT NULL,
                    action TEXT NOT NULL,          -- 'BUY', 'SELL_EXIT', 'SETTLE_RESOLVE'
                    market_id TEXT NOT NULL,
                    question TEXT NOT NULL,
                    side TEXT NOT NULL,
                    shares REAL NOT NULL,
                    vwap_price REAL NOT NULL,
                    usdc_amount REAL NOT NULL,
                    pnl_usdc REAL NOT NULL,
                    p_estimated REAL NOT NULL,
                    slippage_pct REAL NOT NULL,
                    reason TEXT NOT NULL,
                    timestamp TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS scan_cycles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    markets_scanned INTEGER NOT NULL,
                    passed_filters INTEGER NOT NULL,
                    evaluated_count INTEGER NOT NULL,
                    edges_found INTEGER NOT NULL,
                    trades_opened INTEGER NOT NULL,
                    trades_closed INTEGER NOT NULL,
                    cash_usdc REAL NOT NULL,
                    total_equity REAL NOT NULL,
                    drawdown_pct REAL NOT NULL,
                    notes TEXT DEFAULT ''
                );

                CREATE TABLE IF NOT EXISTS candidate_evaluations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cycle_id INTEGER NOT NULL,
                    timestamp TEXT NOT NULL,
                    market_id TEXT NOT NULL,
                    question TEXT NOT NULL,
                    category TEXT NOT NULL,
                    side TEXT NOT NULL,
                    p_estimated REAL NOT NULL,
                    ask_vwap REAL NOT NULL,
                    bid_vwap REAL NOT NULL,
                    edge REAL NOT NULL,
                    roundtrip_slippage_pct REAL NOT NULL,
                    liquidity_usd REAL NOT NULL,
                    hours_to_close REAL NOT NULL,
                    decision TEXT NOT NULL,        -- 'EXECUTED' or 'REJECTED: ...'
                    rationale TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS governance_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    rule_key TEXT NOT NULL UNIQUE,
                    tier TEXT NOT NULL,            -- 'TIER_1_48H', 'TIER_2_CALIBRATION', 'TIER_3_HOTFIX'
                    mode TEXT NOT NULL,            -- 'AUTO_FIX' or 'SEMI_AUTO'
                    status TEXT NOT NULL,          -- 'APPLIED', 'PENDING_APPROVAL', 'APPROVED', 'DISMISSED'
                    title TEXT NOT NULL,
                    explanation TEXT NOT NULL,
                    proposed_action_json TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    resolved_at TEXT DEFAULT ''
                );
                """
            )
            # Safe schema migrations for dynamic tuning parameters
            existing_cols = {
                r["name"] for r in conn.execute("PRAGMA table_info(portfolio_state)").fetchall()
            }
            if "oracle_weight" not in existing_cols:
                conn.execute("ALTER TABLE portfolio_state ADD COLUMN oracle_weight REAL NOT NULL DEFAULT 0.65")
            if "prob_shift_exit_pp" not in existing_cols:
                conn.execute("ALTER TABLE portfolio_state ADD COLUMN prob_shift_exit_pp REAL NOT NULL DEFAULT 0.05")

            row = conn.execute("SELECT * FROM portfolio_state WHERE id = 1").fetchone()
            if row is None:
                now_str = datetime.now(timezone.utc).isoformat()
                conn.execute(
                    """
                    INSERT INTO portfolio_state (
                        id, initial_capital, cash_usdc, locked_usdc, total_equity,
                        peak_equity, max_drawdown_pct, current_drawdown_pct,
                        monthly_target_usdc, halted, halt_reason, active_category_filter,
                        min_liquidity_filter, max_slippage_filter, oracle_weight, prob_shift_exit_pp, updated_at
                    ) VALUES (1, ?, ?, 0.0, ?, ?, 0.0, 0.0, 60.0, 0, '', 'ALL', 5000.0, 0.03, 0.65, 0.05, ?)
                    """,
                    (self.initial_capital, self.initial_capital, self.initial_capital, self.initial_capital, now_str),
                )
            conn.commit()

    def get_portfolio(self) -> Dict[str, Any]:
        with self._connect() as conn:
            row = conn.execute("SELECT * FROM portfolio_state WHERE id = 1").fetchone()
            return dict(row) if row else {}

    def get_open_positions(self) -> List[Dict[str, Any]]:
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM positions WHERE status = 'OPEN' ORDER BY id ASC").fetchall()
            return [dict(r) for r in rows]

    def get_all_positions(self, limit: int = 100) -> List[Dict[str, Any]]:
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM positions ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
            return [dict(r) for r in rows]

    def get_recent_trades(self, limit: int = 100) -> List[Dict[str, Any]]:
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM trades_ledger ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
            return [dict(r) for r in rows]

    def get_recent_candidates(self, limit: int = 40) -> List[Dict[str, Any]]:
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM candidate_evaluations ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
            return [dict(r) for r in rows]

    def get_scan_cycles(self, limit: int = 50) -> List[Dict[str, Any]]:
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM scan_cycles ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
            return [dict(r) for r in rows]

    def open_position(
        self,
        market_id: str,
        question: str,
        category: str,
        side: str,
        token_id: str,
        shares: float,
        entry_vwap: float,
        cost_usdc: float,
        current_bid: float,
        p_est: float,
        entry_edge: float,
        kelly_full_pct: float,
        kelly_half_pct: float,
        applied_size_pct: float,
        roundtrip_slippage_pct: float,
        official_source: str,
        exit_condition: str,
        rationale: str,
        end_date_iso: str,
    ) -> int:
        now_str = datetime.now(timezone.utc).isoformat()
        mkt_val = shares * current_bid
        unrealized = mkt_val - cost_usdc

        with self._connect() as conn:
            cur = conn.execute(
                """
                INSERT INTO positions (
                    market_id, question, category, side, token_id, status,
                    shares, entry_vwap, cost_usdc, current_bid, market_value_usdc,
                    unrealized_pnl, initial_p_est, latest_p_est, entry_edge,
                    kelly_full_pct, kelly_half_pct, applied_size_pct,
                    roundtrip_slippage_pct, official_source, exit_condition,
                    rationale, end_date_iso, opened_at
                ) VALUES (?, ?, ?, ?, ?, 'OPEN', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    market_id, question, category, side, token_id,
                    shares, entry_vwap, cost_usdc, current_bid, mkt_val,
                    unrealized, p_est, p_est, entry_edge,
                    kelly_full_pct, kelly_half_pct, applied_size_pct,
                    roundtrip_slippage_pct, official_source, exit_condition,
                    rationale, end_date_iso, now_str,
                ),
            )
            pos_id = int(cur.lastrowid)

            conn.execute(
                """
                INSERT INTO trades_ledger (
                    position_id, action, market_id, question, side,
                    shares, vwap_price, usdc_amount, pnl_usdc,
                    p_estimated, slippage_pct, reason, timestamp
                ) VALUES (?, 'BUY', ?, ?, ?, ?, ?, ?, 0.0, ?, ?, ?, ?)
                """,
                (
                    pos_id, market_id, question, side,
                    shares, entry_vwap, cost_usdc,
                    p_est, roundtrip_slippage_pct, rationale, now_str,
                ),
            )

            # Deduct cash
            conn.execute(
                "UPDATE portfolio_state SET cash_usdc = cash_usdc - ?, updated_at = ? WHERE id = 1",
                (cost_usdc, now_str),
            )
            conn.commit()

        self.recalculate_portfolio()
        return pos_id

    def update_open_position_mtm(
        self,
        pos_id: int,
        current_bid: float,
        latest_p_est: float,
    ) -> None:
        with self._connect() as conn:
            row = conn.execute("SELECT shares, cost_usdc FROM positions WHERE id = ?", (pos_id,)).fetchone()
            if not row:
                return
            shares = float(row["shares"])
            cost = float(row["cost_usdc"])
            mkt_val = shares * current_bid
            unrealized = mkt_val - cost
            conn.execute(
                """
                UPDATE positions
                SET current_bid = ?, market_value_usdc = ?, unrealized_pnl = ?, latest_p_est = ?
                WHERE id = ?
                """,
                (current_bid, mkt_val, unrealized, latest_p_est, pos_id),
            )
            conn.commit()
        self.recalculate_portfolio()

    def close_position(
        self,
        pos_id: int,
        status: str,  # 'CLOSED' or 'RESOLVED'
        exit_vwap: float,
        proceeds_usdc: float,
        exit_reason: str,
        latest_p_est: float,
    ) -> float:
        now_str = datetime.now(timezone.utc).isoformat()
        with self._connect() as conn:
            row = conn.execute("SELECT * FROM positions WHERE id = ?", (pos_id,)).fetchone()
            if not row:
                return 0.0
            cost = float(row["cost_usdc"])
            shares = float(row["shares"])
            realized_pnl = proceeds_usdc - cost

            conn.execute(
                """
                UPDATE positions
                SET status = ?, current_bid = ?, market_value_usdc = 0.0,
                    unrealized_pnl = 0.0, exit_vwap = ?, proceeds_usdc = ?,
                    realized_pnl = ?, latest_p_est = ?, exit_reason = ?, closed_at = ?
                WHERE id = ?
                """,
                (
                    status, exit_vwap, exit_vwap, proceeds_usdc,
                    realized_pnl, latest_p_est, exit_reason, now_str, pos_id,
                ),
            )

            action = "SETTLE_RESOLVE" if status == "RESOLVED" else "SELL_EXIT"
            conn.execute(
                """
                INSERT INTO trades_ledger (
                    position_id, action, market_id, question, side,
                    shares, vwap_price, usdc_amount, pnl_usdc,
                    p_estimated, slippage_pct, reason, timestamp
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0.0, ?, ?)
                """,
                (
                    pos_id, action, row["market_id"], row["question"], row["side"],
                    shares, exit_vwap, proceeds_usdc, realized_pnl,
                    latest_p_est, exit_reason, now_str,
                ),
            )

            # Add proceeds back to cash
            conn.execute(
                "UPDATE portfolio_state SET cash_usdc = cash_usdc + ?, updated_at = ? WHERE id = 1",
                (proceeds_usdc, now_str),
            )
            conn.commit()

        self.recalculate_portfolio()
        return realized_pnl

    def recalculate_portfolio(self) -> Dict[str, Any]:
        now_str = datetime.now(timezone.utc).isoformat()
        with self._connect() as conn:
            pf = conn.execute("SELECT * FROM portfolio_state WHERE id = 1").fetchone()
            cash = float(pf["cash_usdc"])
            peak = float(pf["peak_equity"])
            max_dd = float(pf["max_drawdown_pct"])

            open_rows = conn.execute("SELECT market_value_usdc FROM positions WHERE status = 'OPEN'").fetchall()
            locked = sum(float(r["market_value_usdc"]) for r in open_rows)
            total_equity = cash + locked

            if total_equity > peak:
                peak = total_equity

            curr_dd = (peak - total_equity) / peak if peak > 0 else 0.0
            if curr_dd > max_dd:
                max_dd = curr_dd

            halted = int(pf["halted"])
            halt_reason = str(pf["halt_reason"])
            # Rule #28: Stop at 40% drawdown from peak
            if curr_dd >= 0.40 and not halted:
                halted = 1
                halt_reason = f"KILL-SWITCH TRIGGERED: Drawdown reached {curr_dd*100:.1f}% from peak (${peak:.2f} -> ${total_equity:.2f})"

            conn.execute(
                """
                UPDATE portfolio_state
                SET locked_usdc = ?, total_equity = ?, peak_equity = ?,
                    max_drawdown_pct = ?, current_drawdown_pct = ?,
                    halted = ?, halt_reason = ?, updated_at = ?
                WHERE id = 1
                """,
                (locked, total_equity, peak, max_dd, curr_dd, halted, halt_reason, now_str),
            )
            conn.commit()
        return self.get_portfolio()

    def record_scan_cycle(
        self,
        markets_scanned: int,
        passed_filters: int,
        evaluated_count: int,
        edges_found: int,
        trades_opened: int,
        trades_closed: int,
        notes: str = "",
    ) -> int:
        pf = self.recalculate_portfolio()
        now_str = datetime.now(timezone.utc).isoformat()
        with self._connect() as conn:
            cur = conn.execute(
                """
                INSERT INTO scan_cycles (
                    timestamp, markets_scanned, passed_filters, evaluated_count,
                    edges_found, trades_opened, trades_closed,
                    cash_usdc, total_equity, drawdown_pct, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    now_str, markets_scanned, passed_filters, evaluated_count,
                    edges_found, trades_opened, trades_closed,
                    pf["cash_usdc"], pf["total_equity"], pf["current_drawdown_pct"], notes,
                ),
            )
            conn.commit()
            return int(cur.lastrowid)

    def record_candidate(
        self,
        cycle_id: int,
        market_id: str,
        question: str,
        category: str,
        side: str,
        p_estimated: float,
        ask_vwap: float,
        bid_vwap: float,
        edge: float,
        roundtrip_slippage_pct: float,
        liquidity_usd: float,
        hours_to_close: float,
        decision: str,
        rationale: str,
    ) -> None:
        now_str = datetime.now(timezone.utc).isoformat()
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO candidate_evaluations (
                    cycle_id, timestamp, market_id, question, category, side,
                    p_estimated, ask_vwap, bid_vwap, edge, roundtrip_slippage_pct,
                    liquidity_usd, hours_to_close, decision, rationale
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    cycle_id, now_str, market_id, question, category, side,
                    p_estimated, ask_vwap, bid_vwap, edge, roundtrip_slippage_pct,
                    liquidity_usd, hours_to_close, decision, rationale,
                ),
            )
            conn.commit()
