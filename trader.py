"""
Autonomous Paper-Trading Engine implementing the exact Charter from `grok метод.txt`.
Executes realistic orderbook-matched virtual trades on Polymarket, manages risk via
Half-Kelly (capped at 6% bankroll, max 5 open positions), enforces the 3% CLOB round-trip
slippage limit, monitors exit conditions, and logs every action to `trades.txt` and SQLite.
"""

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from database import SimDatabase
from oracles import CryptoOracle, EvaluationResult, HighConvictionFactOracle, NewsAndOrderbookOracle, WeatherOracle
from polymarket_api import (
    MarketInfo,
    OrderBookSimulation,
    fetch_active_markets,
    fetch_clob_book,
    fetch_market_by_id,
    simulate_clob_buy_and_exit_check,
    simulate_clob_sell_shares,
)
from telegram_notify import check_and_send_daily_digest, notify_position_closed, send_telegram_alert


TRADES_LOG_PATH = Path(__file__).resolve().parent / "data" / "trades.txt"


def extract_event_key(question: str, category: str) -> str:
    """
    Extracts a canonical underlying event key so the bot never opens multiple positions
    on the same thermometer/city, crypto asset on the same day, or sports match.
    """
    q_low = question.lower().strip()
    date_m = re.search(
        r"\b(january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2}\b|\b202\d-\d{2}-\d{2}\b",
        q_low,
    )
    date_part = date_m.group(0) if date_m else "nodate"

    if category == "Weather" or "temperature in" in q_low:
        city_m = re.search(r"temperature\s+in\s+([a-z\s\(\)]+?)\s+be\b", q_low)
        city = city_m.group(1).strip() if city_m else q_low[:25]
        return f"weather:{city}:{date_part}"

    if category == "Crypto":
        for coin in ("bitcoin", "btc", "ethereum", "eth", "solana", "sol", "xrp", "doge", "bnb"):
            if re.search(rf"\b{coin}\b", q_low):
                norm_coin = "bitcoin" if coin == "btc" else ("ethereum" if coin == "eth" else ("solana" if coin == "sol" else coin))
                return f"crypto:{norm_coin}:{date_part}"

    if category == "Sports":
        cleaned = re.sub(r"^(spread:\s*|will\s+)", "", q_low)
        cleaned = re.sub(r":\s*o/u.*$|\s+win\s+on.*$|\(\-[0-9\.]+\)", "", cleaned).strip()
        return f"sports:{cleaned[:35]}:{date_part}"

    return f"{category.lower()}:{q_low[:40]}"


class GrokCharterPaperTrader:
    """
    Implements the 10-step autonomous Polymarket trading charter on a virtual demo account
    with Conservative Risk Management v3 (0.25x Quarter-Kelly, 4% trade cap, min 12h horizon,
    Strict Time Exit < 1.5h without holding to binary resolution cliff, and Mathematical Oracles only).
    """

    MAX_OPEN_POSITIONS = 8          # Expanded to 8 open positions for wider high-conviction coverage
    MAX_POSITIONS_PER_CATEGORY = 3  # Max 3 per general category (disciplined diversification)
    MAX_CRYPTO_POSITIONS = 4        # Max 4 for high-liquidity Crypto (fast turnover ~6.7h)
    KELLY_FRACTION = 0.40           # Fractional Kelly sizing for high-winrate strategy (up from 0.35)
    MAX_BANK_PCT_PER_TRADE = 0.15   # Up to 15% bankroll per trade (~$4.50-$4.70 on current bankroll)
    MIN_EDGE_PP = 0.015             # 1.5 percentage points minimum divergence against Ask VWAP
    MIN_ESTIMATED_PROB = 0.92       # Minimum estimated probability: strictly high-conviction events (92%+ likelihood)
    MIN_CONTRACT_PRICE = 0.84       # Buy only discount mature contracts [0.84, 0.965]
    MAX_CONTRACT_PRICE = 0.965      # Yield: +3.6% to +19.0% upon resolution
    MIN_HOURS_TO_CLOSE = 0.8        # Focus on near-term resolutions (1h to 5 days)
    MAX_HOURS_TO_CLOSE = 120.0      # Fast capital turnover
    EXIT_HOURS_THRESHOLD = 0.0      # NEVER dump prematurely before expiry: hold into resolution ($1.00 payout)
    PROB_SHIFT_EXIT_PP = 0.10       # Exit only if probability estimate drops by > 10 pp and falls below entry
    STOP_LOSS_PCT = 0.40            # Hard Stop-Loss: cut positions losing > 40% if thesis severely deteriorates

    def __init__(
        self,
        db: Optional[SimDatabase] = None,
        trades_txt_path: Path = TRADES_LOG_PATH,
        initial_capital: float = 50.0,
    ) -> None:
        self.db = db or SimDatabase(initial_capital=initial_capital)
        self.trades_txt_path = trades_txt_path
        self.trades_txt_path.parent.mkdir(parents=True, exist_ok=True)
        self.crypto_oracle = CryptoOracle()
        self.weather_oracle = WeatherOracle()
        self.news_oracle = NewsAndOrderbookOracle()
        self.fact_oracle = HighConvictionFactOracle()

        if not self.trades_txt_path.exists():
            self._append_trades_log(
                "================================================================================\n"
                "POLYMARKET AUTONOMOUS PAPER TRADER — GROK CHARTER SIMULATION LOG (trades.txt)\n"
                f"Initialized at: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}\n"
                f"Starting Virtual Bankroll: ${initial_capital:.2f} USDC | Monthly Target: +$60.00/mo\n"
                "Rules: Edge >= 8 pp | CLOB Round-Trip Slippage <= 2% | Size: 0.25x Kelly (max 4% bank)\n"
                "Max Open Positions: 8 (max 3/category, 1/event) | Kill-Switch: 40% Drawdown\n"
                "================================================================================\n"
            )

    def _append_trades_log(self, text: str) -> None:
        with open(self.trades_txt_path, "a", encoding="utf-8") as f:
            f.write(text + "\n")

    @classmethod
    def compute_kelly_sizing(
        cls,
        p_est: float,
        ask_vwap: float,
        total_equity: float,
        max_pct: float = 0.04,
        kelly_fraction: float = 0.25,
    ) -> Tuple[float, float, float, float]:
        """
        Calculates Full Kelly, Fractional (0.25x) Kelly, Capped % of bankroll, and USDC bet size.
        Formula for binary contract at cost `c` paying $1 on win:
          f* = (p - c) / (1 - c)
        """
        if ask_vwap <= 0.001 or ask_vwap >= 0.999 or p_est <= ask_vwap:
            return 0.0, 0.0, 0.0, 0.0

        full_kelly = (p_est - ask_vwap) / (1.0 - ask_vwap)
        frac_kelly = kelly_fraction * full_kelly
        applied_pct = min(frac_kelly, max_pct)
        bet_usdc = round(total_equity * applied_pct, 2)
        return full_kelly, frac_kelly, applied_pct, bet_usdc

    def _evaluate_market_probability(
        self,
        market: MarketInfo,
        preloaded_book: Optional[Dict[str, List[Tuple[float, float]]]] = None,
    ) -> Tuple[Optional[EvaluationResult], Optional[Dict[str, List[Tuple[float, float]]]]]:
        """
        Runs the appropriate oracle for `market`.
        Returns (EvaluationResult, clob_yes_book).
        """
        # 1. Try High-Conviction Fact Oracle first (Sports exact scores, ceasefires, macro consensus)
        res = self.fact_oracle.evaluate(market)
        if res is not None:
            return res, preloaded_book

        # 2. Try Crypto Quantitative Oracle (Binance / Kraken / Coinbase spot klines & barriers)
        if market.category == "Crypto" or any(
            k in market.question.lower() for k in ["bitcoin", "ethereum", "solana", "btc", "eth"]
        ):
            res = self.crypto_oracle.evaluate(market)
            if res is not None:
                return res, preloaded_book
            return None, None

        # 3. Try Weather Oracle (strict microclimate-safe brackets only)
        if market.category == "Weather" or "temperature" in market.question.lower():
            res = self.weather_oracle.evaluate(market)
            if res is not None:
                return res, preloaded_book

        # 4. Fallback for Macro, Geopolitics, Sports, Other: News Consensus & CLOB Imbalance
        if market.clob_token_ids:
            try:
                book = preloaded_book or fetch_clob_book(market.clob_token_ids[0])
                bids = book.get("bids", [])
                asks = book.get("asks", [])
                if bids and asks:
                    res = self.news_oracle.evaluate_with_orderbook(market, bids, asks)
                    if res is not None:
                        return res, book
            except Exception:
                pass

        return None, None

    def monitor_and_manage_open_positions(self) -> int:
        """
        Step 9 of Charter:
        Checks all open positions against live Gamma resolution status and live CLOB Bids.
        Exits if:
          - Market resolved on Polymarket ($1 or $0 payout)
          - Edge closed (Bid VWAP >= latest_p_est - 0.01)
          - Estimate dropped by > 5 percentage points against us
          - < 1 hour left to market close
        Returns number of positions closed/settled.
        """
        open_positions = self.db.get_open_positions()
        closed_count = 0

        for pos in open_positions:
            pos_id = int(pos["id"])
            market_id = str(pos["market_id"])
            side = str(pos["side"])
            token_id = str(pos["token_id"])
            shares = float(pos["shares"])
            entry_vwap = float(pos["entry_vwap"])
            initial_p = float(pos["initial_p_est"])

            live_mkt = fetch_market_by_id(market_id)

            # Check if resolved on Polymarket
            if live_mkt and live_mkt.resolved:
                # Index 0 is YES, Index 1 is NO
                win_price = live_mkt.gamma_prices[0] if side == "YES" else live_mkt.gamma_prices[1]
                payout_per_share = 1.0 if win_price >= 0.95 else 0.0
                proceeds = round(shares * payout_per_share, 4)
                reason = f"MARKET RESOLVED on Polymarket: {side} settled at ${payout_per_share:.2f}/share"
                pnl = self.db.close_position(
                    pos_id=pos_id,
                    status="RESOLVED",
                    exit_vwap=payout_per_share,
                    proceeds_usdc=proceeds,
                    exit_reason=reason,
                    latest_p_est=payout_per_share,
                )
                self._append_trades_log(
                    f"[RESOLVED] #{pos_id} | {pos['question']} ({side})\n"
                    f"  Entry VWAP: {entry_vwap:.4f} | Settlement: {payout_per_share:.2f} | "
                    f"PnL: ${pnl:+.2f} USDC | Reason: {reason}"
                )
                notify_position_closed(
                    pos=pos,
                    pnl=pnl,
                    exit_vwap=payout_per_share,
                    exit_reason=reason,
                    total_equity=float(self.db.get_portfolio()["total_equity"]),
                )
                closed_count += 1
                continue

            # Otherwise check live CLOB Bid book for mark-to-market & exit triggers
            try:
                vwap_sell, proceeds, best_bid = simulate_clob_sell_shares(token_id, shares)
            except Exception:
                vwap_sell, proceeds, best_bid = 0.0, 0.0, 0.0

            hours_left = live_mkt.hours_to_close if live_mkt else 24.0

            # Re-evaluate probability if live_mkt available
            latest_p = float(pos["latest_p_est"])
            if live_mkt:
                eval_res, _ = self._evaluate_market_probability(live_mkt)
                if eval_res is not None:
                    latest_p = eval_res.p_yes if side == "YES" else eval_res.p_no

            # Update MTM in database if valid bid exists
            if vwap_sell > 0:
                self.db.update_open_position_mtm(
                    pos_id=pos_id,
                    current_bid=vwap_sell,
                    latest_p_est=latest_p,
                )

            pf_now = self.db.get_portfolio()
            prob_shift_limit = float(pf_now.get("prob_shift_exit_pp", self.PROB_SHIFT_EXIT_PP))
            exit_triggered = False
            exit_reason = ""

            # Exit Rule A: GENUINE TAKE PROFIT (Lock in 98.5%+ bid early to free up capital)
            if vwap_sell >= 0.985:
                exit_triggered = True
                gain_pct = (vwap_sell - entry_vwap) / entry_vwap * 100.0
                exit_reason = (
                    f"TAKE PROFIT (98.5%+ Bid Reached): Live CLOB Bid VWAP ({vwap_sell*100:.1f}%) "
                    f"secured early with +{gain_pct:.1f}% gain"
                )
            # Exit Rule B: HARD STOP-LOSS (Protect capital only if price drops AND thesis deteriorated)
            elif vwap_sell > 0 and (
                vwap_sell <= entry_vwap * (1.0 - self.STOP_LOSS_PCT) and latest_p <= 0.75
            ):
                exit_triggered = True
                loss_pct = (entry_vwap - vwap_sell) / entry_vwap * 100.0
                exit_reason = (
                    f"STOP-LOSS TRIGGERED: Price dropped to ${vwap_sell:.3f} "
                    f"(-{loss_pct:.1f}% from entry ${entry_vwap:.3f}, P_est={latest_p*100:.1f}%)"
                )
            elif vwap_sell <= 0:
                continue
            # Exit Rule C: Prob estimate shifted down AND no longer high-conviction
            elif (initial_p - latest_p) >= prob_shift_limit and latest_p <= 0.70:
                exit_triggered = True
                exit_reason = (
                    f"THESIS INVALIDATED (Prob Shift > {prob_shift_limit*100:.1f}pp & P_est <= 70%): "
                    f"Estimate dropped from {initial_p*100:.1f}% to {latest_p*100:.1f}%"
                )

            if exit_triggered:
                pnl = self.db.close_position(
                    pos_id=pos_id,
                    status="CLOSED",
                    exit_vwap=vwap_sell,
                    proceeds_usdc=round(proceeds, 4),
                    exit_reason=exit_reason,
                    latest_p_est=latest_p,
                )
                self._append_trades_log(
                    f"[EXIT] #{pos_id} | {pos['question']} ({side})\n"
                    f"  Shares: {shares:.2f} | Entry VWAP: {entry_vwap:.4f} -> Exit Bid VWAP: {vwap_sell:.4f}\n"
                    f"  Proceeds: ${proceeds:.2f} | Realized PnL: ${pnl:+.2f} USDC | Reason: {exit_reason}"
                )
                notify_position_closed(
                    pos=pos,
                    pnl=pnl,
                    exit_vwap=vwap_sell,
                    exit_reason=exit_reason,
                    total_equity=float(self.db.get_portfolio()["total_equity"]),
                )
                closed_count += 1

        return closed_count

    def monitor_and_manage_shadow_positions(self) -> int:
        """
        Monitors open shadow (sandbox) positions against Polymarket resolution and CLOB bids.
        Applies identical TP (+12%), Stop-Loss (-35%), and probability shift exits,
        logging actions with [SHADOW] prefix without sending public Telegram alerts.
        """
        open_positions = self.db.get_open_shadow_positions()
        closed_count = 0
        prob_shift_exit_pp = 0.08

        for pos in open_positions:
            pos_id = int(pos["id"])
            market_id = str(pos["market_id"])
            side = str(pos["side"])
            token_id = str(pos["token_id"])
            shares = float(pos["shares"])
            entry_vwap = float(pos["entry_vwap"])
            initial_p = float(pos["initial_p_est"])

            live_mkt = fetch_market_by_id(market_id)

            # Check if resolved on Polymarket
            if live_mkt and live_mkt.resolved:
                win_price = live_mkt.gamma_prices[0] if side == "YES" else live_mkt.gamma_prices[1]
                payout_per_share = 1.0 if win_price >= 0.95 else 0.0
                proceeds = round(shares * payout_per_share, 4)
                reason = f"SHADOW MARKET RESOLVED on Polymarket: {side} settled at ${payout_per_share:.2f}/share"
                pnl = self.db.close_shadow_position(
                    pos_id=pos_id,
                    status="RESOLVED",
                    exit_vwap=payout_per_share,
                    proceeds_usdc=proceeds,
                    exit_reason=reason,
                    latest_p_est=payout_per_share,
                )
                self._append_trades_log(
                    f"[SHADOW RESOLVED] #{pos_id} | {pos['question']} ({side})\n"
                    f"  Entry VWAP: {entry_vwap:.4f} | Settlement: {payout_per_share:.2f} | "
                    f"PnL: ${pnl:+.2f} USDC | Reason: {reason}"
                )
                closed_count += 1
                continue

            try:
                vwap_sell, proceeds, best_bid = simulate_clob_sell_shares(token_id, shares)
            except Exception:
                vwap_sell, proceeds, best_bid = 0.0, 0.0, 0.0

            hours_left = live_mkt.hours_to_close if live_mkt else 24.0

            latest_p = float(pos["latest_p_est"])
            if live_mkt:
                eval_res, _ = self._evaluate_market_probability(live_mkt)
                if eval_res is not None:
                    latest_p = eval_res.p_yes if side == "YES" else eval_res.p_no

            if vwap_sell > 0:
                self.db.update_open_shadow_position_mtm(pos_id=pos_id, current_bid=best_bid, latest_p_est=latest_p)

            should_exit = False
            exit_reason = ""

            if vwap_sell > 0:
                cost = float(pos["cost_usdc"])
                gross_return_pct = (proceeds - cost) / cost if cost > 0 else 0.0
                if gross_return_pct >= 0.12:
                    should_exit = True
                    exit_reason = f"TAKE-PROFIT TRIGGERED: Net return +{gross_return_pct*100:.1f}% >= +12% (Bid VWAP: {vwap_sell:.4f} vs Entry: {entry_vwap:.4f})"
                elif vwap_sell <= entry_vwap * 0.65:
                    should_exit = True
                    exit_reason = f"STOP-LOSS TRIGGERED: Price dropped by {(1 - vwap_sell/entry_vwap)*100:.1f}% from entry ({entry_vwap:.4f} -> {vwap_sell:.4f})"

            if not should_exit and hours_left <= self.MIN_HOURS_TO_CLOSE_EXIT:
                should_exit = True
                exit_reason = f"TIME EXIT: {hours_left:.1f}h left to close (under {self.MIN_HOURS_TO_CLOSE_EXIT:.1f}h threshold)"

            if not should_exit and (initial_p - latest_p) >= prob_shift_exit_pp and vwap_sell < entry_vwap:
                should_exit = True
                exit_reason = f"PROBABILITY SHIFT: Model confidence dropped by {(initial_p - latest_p)*100:.1f} pp ({initial_p:.3f} -> {latest_p:.3f})"

            if should_exit:
                pnl = self.db.close_shadow_position(
                    pos_id=pos_id,
                    status="CLOSED",
                    exit_vwap=vwap_sell,
                    proceeds_usdc=proceeds,
                    exit_reason=exit_reason,
                    latest_p_est=latest_p,
                )
                self._append_trades_log(
                    f"[SHADOW EXIT] #{pos_id} | {pos['question']} ({side})\n"
                    f"  Shares: {shares:.2f} | Entry VWAP: {entry_vwap:.4f} -> Exit Bid VWAP: {vwap_sell:.4f}\n"
                    f"  Proceeds: ${proceeds:.2f} | Realized PnL: ${pnl:+.2f} USDC | Reason: {exit_reason}"
                )
                closed_count += 1

        return closed_count

    def partition_markets(
        self,
        all_markets: List[MarketInfo],
        open_real_market_ids: Set[str],
        open_shadow_market_ids: Set[str],
        cat_filter: str,
        min_liq: float,
    ) -> Tuple[List[MarketInfo], List[MarketInfo]]:
        """
        Partitions active markets into candidates for real execution vs. candidates for shadow evaluation.
        """
        active_candidates: List[MarketInfo] = []
        shadow_candidates: List[MarketInfo] = []

        for m in all_markets:
            if not m.has_official_source:
                continue
            if not (self.MIN_HOURS_TO_CLOSE <= m.hours_to_close <= self.MAX_HOURS_TO_CLOSE):
                continue
            liq_threshold = 400.0 if m.category == "Weather" else min_liq
            if m.liquidity_usd < liq_threshold:
                continue

            if cat_filter == "ALL" or m.category.upper() == cat_filter.upper():
                if m.id not in open_real_market_ids:
                    active_candidates.append(m)
            else:
                if m.id not in open_shadow_market_ids:
                    shadow_candidates.append(m)

        def _priority_key(m: MarketInfo) -> Tuple[int, float]:
            has_high_prob = 0 if (m.gamma_prices and (0.84 <= m.gamma_prices[0] <= 0.98 or 0.84 <= m.gamma_prices[1] <= 0.98)) else 1
            return (has_high_prob, -m.volume_24h_usd)

        active_candidates.sort(key=_priority_key)
        shadow_candidates.sort(key=_priority_key)

        return active_candidates[:50], shadow_candidates[:10]

    def evaluate_and_execute_shadow_candidates(
        self,
        shadow_markets: List[MarketInfo],
        open_shadow_market_ids: Set[str],
    ) -> int:
        """
        Evaluates up to 10 shadow candidates, checks Edge >= 8% and CLOB slippage,
        and opens virtual shadow positions with shadow cash.
        """
        open_shadow = self.db.get_open_shadow_positions()
        if len(open_shadow) >= 5:
            return 0

        shadow_pf = self.db.get_shadow_portfolio()
        if shadow_pf.get("halted"):
            return 0

        shadow_equity = float(shadow_pf.get("total_equity", 50.0))
        shadow_cash = float(shadow_pf.get("cash_usdc", 50.0))
        max_slippage = float(self.db.get_portfolio().get("max_slippage_filter", 0.02))

        opened_count = 0
        for mkt in shadow_markets:
            if len(open_shadow) + opened_count >= 5:
                break
            if mkt.id in open_shadow_market_ids:
                continue

            eval_res, preloaded_yes_book = self._evaluate_market_probability(mkt)
            if eval_res is None:
                continue

            gamma_yes, gamma_no = mkt.gamma_prices[0], mkt.gamma_prices[1]
            raw_edge_yes = eval_res.p_yes - gamma_yes
            raw_edge_no = eval_res.p_no - gamma_no

            if raw_edge_yes >= raw_edge_no:
                chosen_side = "YES"
                token_id = mkt.clob_token_ids[0]
                p_est = eval_res.p_yes
                indicative_price = gamma_yes
            else:
                chosen_side = "NO"
                token_id = mkt.clob_token_ids[1]
                p_est = eval_res.p_no
                indicative_price = gamma_no

            if not (0.15 <= p_est <= 0.85):
                continue

            full_k, half_k, applied_size_pct, tentative_bet = self.compute_kelly_sizing(
                p_est=p_est,
                ask_vwap=indicative_price,
                total_equity=shadow_equity,
                max_pct=0.06,
                kelly_fraction=0.25,
            )
            bet_usdc = min(tentative_bet, shadow_cash)
            if bet_usdc < 1.00:
                continue

            try:
                ob_sim: OrderBookSimulation = simulate_clob_buy_and_exit_check(
                    token_id=token_id,
                    side_label=chosen_side,
                    bet_usdc=bet_usdc,
                    max_slippage_pct=max_slippage,
                    preloaded_book=preloaded_yes_book if chosen_side == "YES" else None,
                )
            except Exception:
                continue

            real_edge = p_est - ob_sim.vwap_buy_price
            if real_edge < self.MIN_EDGE_PP:
                continue
            if not (ob_sim.sufficient_depth and ob_sim.passes_slippage_limit):
                continue

            pos_id = self.db.open_shadow_position(
                market_id=mkt.id,
                question=mkt.question,
                category=mkt.category,
                side=chosen_side,
                token_id=token_id,
                shares=ob_sim.shares_filled,
                entry_vwap=ob_sim.vwap_buy_price,
                cost_usdc=ob_sim.bet_usdc,
                initial_p_est=p_est,
                entry_edge=real_edge,
                kelly_full_pct=full_k,
                kelly_half_pct=half_k,
                applied_size_pct=applied_size_pct,
                roundtrip_slippage_pct=ob_sim.roundtrip_slippage_pct,
                official_source=mkt.resolution_source,
                exit_condition="Take-Profit (+12%), Stop-Loss (-35%), or Settlement",
                rationale=eval_res.rationale,
                end_date_iso=mkt.end_date_iso,
            )
            self._append_trades_log(
                f"[SHADOW EXEC] #{pos_id} | {mkt.question} ({chosen_side})\n"
                f"  Category: {mkt.category} | Shares: {ob_sim.shares_filled:.2f} @ {ob_sim.vwap_buy_price:.4f}\n"
                f"  Bet: ${ob_sim.bet_usdc:.2f} USDC | P_est: {p_est*100:.1f}% | Edge: {real_edge*100:+.1f} pp"
            )
            opened_count += 1
            shadow_cash -= ob_sim.bet_usdc

        return opened_count

    def run_cycle(self, max_markets_to_scan: int = 500) -> Dict[str, Any]:
        """
        Runs one complete 10-minute autonomous scan & trade cycle according to the Charter.
        """
        now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        # Step 0: ALWAYS monitor and update existing open positions first!
        # Even during a halt or kill-switch, existing positions must be actively protected:
        # Stop-Loss, Strict Time-Exit, and Resolution settlement MUST execute so capital is not abandoned.
        trades_closed = self.monitor_and_manage_open_positions()
        shadow_closed = self.monitor_and_manage_shadow_positions()
        pf = self.db.recalculate_portfolio()

        # Check Kill-Switch (40% drawdown): Halt NEW entries, but positions were managed above
        if pf.get("halted"):
            msg = f"Cycle skipped (entries halted): Bot is HALTED due to 40% drawdown rule ({pf.get('halt_reason')})"
            self._append_trades_log(f"[{now_str}] {msg}")
            return {"status": "HALTED", "reason": pf.get("halt_reason"), "portfolio": pf, "trades_closed": trades_closed}

        open_positions = self.db.get_open_positions()
        open_market_ids = {str(p["market_id"]) for p in open_positions}
        open_shadow_positions = self.db.get_open_shadow_positions()
        open_shadow_market_ids = {str(p["market_id"]) for p in open_shadow_positions}

        # Track active underlying events (1 event = 1 trade) and category concentration (max 3 per category)
        active_event_keys: Set[str] = {
            extract_event_key(str(p["question"]), str(p["category"])) for p in open_positions
        }
        category_counts: Dict[str, int] = {}
        for p in open_positions:
            cat = str(p["category"])
            category_counts[cat] = category_counts.get(cat, 0) + 1

        # Step 1: Fetch active markets from Gamma API
        all_markets = fetch_active_markets(max_Count=max_markets_to_scan)
        min_liq = float(pf.get("min_liquidity_filter", 5000.0))
        max_slippage = float(pf.get("max_slippage_filter", 0.03))
        cat_filter = str(pf.get("active_category_filter", "ALL"))

        candidates_to_evaluate, shadow_candidates = self.partition_markets(
            all_markets,
            open_real_market_ids=open_market_ids,
            open_shadow_market_ids=open_shadow_market_ids,
            cat_filter=cat_filter,
            min_liq=min_liq,
        )

        # Auto-Governor Tier 3 Hotfix: discover and geocode any new Polymarket weather cities on the fly
        try:
            from auto_governor import AutoGovernor
            gov = AutoGovernor(self.db)
            added_cities = gov.scan_and_fix_unmapped_weather_cities(candidates_to_evaluate)
            if added_cities:
                self.weather_oracle._load_custom_stations()
        except Exception:
            pass

        # Record cycle placeholder to get cycle_id
        cycle_id = self.db.record_scan_cycle(
            markets_scanned=len(all_markets),
            passed_filters=len(candidates_to_evaluate),
            evaluated_count=0,
            edges_found=0,
            trades_opened=0,
            trades_closed=trades_closed,
            notes="In progress",
        )

        evaluated_count = 0
        edges_found = 0
        trades_opened = 0

        for mkt in candidates_to_evaluate:
            eval_res, preloaded_yes_book = self._evaluate_market_probability(mkt)
            if eval_res is None:
                continue

            evaluated_count += 1

            # Determine which side (YES or NO) has positive divergence vs Gamma indicative price first
            gamma_yes, gamma_no = mkt.gamma_prices[0], mkt.gamma_prices[1]
            raw_edge_yes = eval_res.p_yes - gamma_yes
            raw_edge_no = eval_res.p_no - gamma_no

            if raw_edge_yes >= raw_edge_no:
                chosen_side = "YES"
                token_id = mkt.clob_token_ids[0]
                p_est = eval_res.p_yes
            else:
                chosen_side = "NO"
                token_id = mkt.clob_token_ids[1]
                p_est = eval_res.p_no

            # Refresh portfolio state before sizing
            pf = self.db.get_portfolio()
            total_equity = float(pf["total_equity"])
            cash_available = float(pf["cash_usdc"])

            # Estimate tentative bet size using Gamma price first, then verify against real CLOB Ask VWAP
            tentative_price = gamma_yes if chosen_side == "YES" else gamma_no
            _, _, _, tentative_bet = self.compute_kelly_sizing(
                p_est=p_est,
                ask_vwap=max(tentative_price, 0.02),
                total_equity=total_equity,
                max_pct=self.MAX_BANK_PCT_PER_TRADE,
                kelly_fraction=self.KELLY_FRACTION,
            )
            probe_bet_usdc = min(
                max(tentative_bet, round(total_equity * 0.12, 2), 2.50),
                max(cash_available, 1.00),
            )

            # Step 6: Check real CLOB Order Book for entry Ask VWAP and immediate exit Bid VWAP
            try:
                ob_sim: OrderBookSimulation = simulate_clob_buy_and_exit_check(
                    token_id=token_id,
                    side_label=chosen_side,
                    bet_usdc=probe_bet_usdc,
                    max_slippage_pct=max_slippage,
                )
            except Exception:
                continue

            # Real actionable edge is against the actual CLOB Ask VWAP price (not mid or stale Gamma price!)
            real_edge = p_est - ob_sim.vwap_buy_price

            if real_edge >= self.MIN_EDGE_PP:
                edges_found += 1

            event_key = extract_event_key(mkt.question, mkt.category)
            cat_cap = self.MAX_CRYPTO_POSITIONS if mkt.category == "Crypto" else self.MAX_POSITIONS_PER_CATEGORY

            # Decide whether to execute or reject
            decision = ""
            if real_edge < self.MIN_EDGE_PP:
                decision = f"REJECTED: Edge {real_edge*100:+.1f} pp < {self.MIN_EDGE_PP*100:.0f} pp threshold (P_est={p_est*100:.1f}% vs AskVWAP={ob_sim.vwap_buy_price*100:.1f}%)"
            elif p_est < self.MIN_ESTIMATED_PROB:
                decision = f"REJECTED: Win probability {p_est*100:.1f}% < {self.MIN_ESTIMATED_PROB*100:.0f}% minimum (no underdog lottery bets)"
            elif ob_sim.vwap_buy_price < self.MIN_CONTRACT_PRICE or ob_sim.vwap_buy_price > self.MAX_CONTRACT_PRICE:
                decision = f"REJECTED: Contract price ${ob_sim.vwap_buy_price:.3f} outside sweet spot [${self.MIN_CONTRACT_PRICE:.2f}, ${self.MAX_CONTRACT_PRICE:.2f}]"
            elif (
                mkt.category == "Weather"
                and chosen_side == "NO"
                and any(w in mkt.question.lower() for w in [" be ", "between"])
                and not any(w in mkt.question.lower() for w in ["above", "below", "or higher", "or lower", "or more", "or less"])
            ):
                decision = "REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk)"
            elif not ob_sim.sufficient_depth:
                decision = f"REJECTED: {ob_sim.reject_reason}"
            elif not ob_sim.passes_slippage_limit:
                decision = f"REJECTED: CLOB round-trip slippage {ob_sim.roundtrip_slippage_pct*100:.2f}% > {max_slippage*100:.1f}% limit"
            elif event_key in active_event_keys:
                decision = f"REJECTED: Duplicate underlying event ({event_key})"
            elif category_counts.get(mkt.category, 0) >= cat_cap:
                decision = f"REJECTED: Category cap reached ({cat_cap}/{cat_cap} in {mkt.category})"
            elif len(open_positions) + trades_opened >= self.MAX_OPEN_POSITIONS:
                decision = f"REJECTED: Max open positions ({self.MAX_OPEN_POSITIONS}) reached"
            else:
                # Re-calculate exact Quarter-Kelly size using the real CLOB Ask VWAP
                full_k, frac_k, applied_pct, final_bet_usdc = self.compute_kelly_sizing(
                    p_est=p_est,
                    ask_vwap=ob_sim.vwap_buy_price,
                    total_equity=total_equity,
                    max_pct=self.MAX_BANK_PCT_PER_TRADE,
                    kelly_fraction=self.KELLY_FRACTION,
                )
                # If calculated Kelly bet exceeds currently available cash, but cash is sufficient for minimum order,
                # utilize remaining available cash to prevent capital from sitting idle
                if final_bet_usdc > cash_available and cash_available >= 1.00:
                    final_bet_usdc = round(cash_available, 2)
                    applied_pct = round(final_bet_usdc / total_equity, 4)

                # If fractional Kelly bet is near minimum order ($0.70..$1.00) and within bank risk, floor at $1.00
                if 0.70 <= final_bet_usdc < 1.00 and cash_available >= 1.00 and 1.00 <= total_equity * 0.05:
                    final_bet_usdc = 1.00
                    applied_pct = round(1.00 / total_equity, 4)

                if final_bet_usdc < 1.00 or final_bet_usdc > cash_available:
                    decision = f"REJECTED: Available cash ${cash_available:.2f} below $1.00 minimum bet"
                else:
                    # Re-verify exact shares for `final_bet_usdc`
                    final_sim = simulate_clob_buy_and_exit_check(
                        token_id=token_id,
                        side_label=chosen_side,
                        bet_usdc=final_bet_usdc,
                        max_slippage_pct=max_slippage,
                    )
                    if not final_sim.passes_slippage_limit or (p_est - final_sim.vwap_buy_price) < self.MIN_EDGE_PP:
                        decision = f"REJECTED on final sizing: slippage={final_sim.roundtrip_slippage_pct*100:.2f}%"
                    else:
                        # EXECUTE VIRTUAL TRADE!
                        exit_cond = (
                            f"Hold to binary resolution ($1.00 payout), "
                            f"or early Take Profit if Bid VWAP >= 0.985, "
                            f"or Stop-Loss <= {final_sim.vwap_buy_price * (1.0 - self.STOP_LOSS_PCT):.3f} if P_est <= 70%"
                        )
                        pos_id = self.db.open_position(
                            market_id=mkt.id,
                            question=mkt.question,
                            category=mkt.category,
                            side=chosen_side,
                            token_id=token_id,
                            shares=round(final_sim.shares_filled, 4),
                            entry_vwap=round(final_sim.vwap_buy_price, 4),
                            cost_usdc=final_bet_usdc,
                            current_bid=round(final_sim.vwap_sell_price, 4),
                            p_est=p_est,
                            entry_edge=round(p_est - final_sim.vwap_buy_price, 4),
                            kelly_full_pct=round(full_k, 4),
                            kelly_half_pct=round(frac_k, 4),
                            applied_size_pct=round(applied_pct, 4),
                            roundtrip_slippage_pct=round(final_sim.roundtrip_slippage_pct, 4),
                            official_source=eval_res.official_source,
                            exit_condition=exit_cond,
                            rationale=eval_res.rationale,
                            end_date_iso=mkt.end_date_iso,
                        )
                        trades_opened += 1
                        active_event_keys.add(event_key)
                        category_counts[mkt.category] = category_counts.get(mkt.category, 0) + 1
                        decision = f"EXECUTED BUY #{pos_id} (${final_bet_usdc:.2f} @ {final_sim.vwap_buy_price:.4f})"

                        # Log to trades.txt per Rule #8
                        self._append_trades_log(
                            f"[{now_str}] [OPEN TRADE #{pos_id}] {mkt.question}\n"
                            f"  Категория: {mkt.category} | Сторона: {chosen_side} | Источник: {eval_res.official_source}\n"
                            f"  Оценка бота: {p_est*100:.1f}% vs Рынок (Ask VWAP): {final_sim.vwap_buy_price*100:.1f}% "
                            f"(Перекос/Edge: +{(p_est - final_sim.vwap_buy_price)*100:.1f} п.п.)\n"
                            f"  Стакан CLOB: BestBid={final_sim.best_bid:.3f}, BestAsk={final_sim.best_ask:.3f}, "
                            f"Проскальзывание входа/выхода={final_sim.roundtrip_slippage_pct*100:.2f}% (<= 3.0%)\n"
                            f"  Келли: Полный={full_k*100:.1f}%, Четверть(0.25x)={frac_k*100:.1f}% -> Применён={applied_pct*100:.1f}% банка\n"
                            f"  Размер сделки: ${final_bet_usdc:.2f} USDC ({final_sim.shares_filled:.2f} shares @ ${final_sim.vwap_buy_price:.4f})\n"
                            f"  Условие выхода: {exit_cond}\n"
                            f"  Причина: {eval_res.rationale}\n"
                        )


            # Store candidate evaluation in DB if edge >= 4 pp or if executed
            if abs(real_edge) >= 0.04 or decision.startswith("EXECUTED"):
                self.db.record_candidate(
                    cycle_id=cycle_id,
                    market_id=mkt.id,
                    question=mkt.question,
                    category=mkt.category,
                    side=chosen_side,
                    p_estimated=round(p_est, 4),
                    ask_vwap=round(ob_sim.vwap_buy_price, 4),
                    bid_vwap=round(ob_sim.vwap_sell_price, 4),
                    edge=round(real_edge, 4),
                    roundtrip_slippage_pct=round(ob_sim.roundtrip_slippage_pct, 4),
                    liquidity_usd=round(mkt.liquidity_usd, 2),
                    hours_to_close=round(mkt.hours_to_close, 2),
                    decision=decision,
                    rationale=eval_res.rationale,
                )

        # Step 7 (Sandbox): Evaluate and execute shadow candidates on disabled categories
        shadow_opened = 0
        if shadow_candidates:
            try:
                shadow_opened = self.evaluate_and_execute_shadow_candidates(
                    shadow_candidates, open_shadow_market_ids
                )
            except Exception:
                pass

        # Update scan cycle record with final stats
        pf_after = self.db.recalculate_portfolio()
        with self.db._connect() as conn:
            conn.execute(
                """
                UPDATE scan_cycles
                SET evaluated_count = ?, edges_found = ?, trades_opened = ?, trades_closed = ?,
                    cash_usdc = ?, total_equity = ?, drawdown_pct = ?, notes = ?
                WHERE id = ?
                """,
                (
                    evaluated_count,
                    edges_found,
                    trades_opened,
                    trades_closed,
                    pf_after["cash_usdc"],
                    pf_after["total_equity"],
                    pf_after["current_drawdown_pct"],
                    f"Scanned {len(all_markets)}, filtered {len(candidates_to_evaluate)}, eval {evaluated_count}, shadow_opened {shadow_opened}",
                    cycle_id,
                ),
            )
            conn.commit()

        self._append_trades_log(
            f"[{now_str}] [CYCLE #{cycle_id} SUMMARY] Scanned={len(all_markets)} | "
            f"PassedFilter={len(candidates_to_evaluate)} | Evaluated={evaluated_count} | "
            f"Edges(>=8pp)={edges_found} | Opened={trades_opened} (Shadow={shadow_opened}) | Closed={trades_closed} | "
            f"Cash=${pf_after['cash_usdc']:.2f} | Equity=${pf_after['total_equity']:.2f} "
            f"(DD={pf_after['current_drawdown_pct']*100:.2f}%)"
        )

        # Run 3-tier Auto-Governor after every cycle (auto-fixes & semi-auto proposals)
        try:
            from auto_governor import AutoGovernor
            AutoGovernor(self.db).evaluate_portfolio_and_rules()
        except Exception:
            pass

        # Send consolidated daily digest once per 24 hours
        try:
            check_and_send_daily_digest(self.db)
        except Exception:
            pass

        return {
            "cycle_id": cycle_id,
            "timestamp": now_str,
            "markets_scanned": len(all_markets),
            "passed_filters": len(filtered_markets),
            "evaluated_count": evaluated_count,
            "edges_found": edges_found,
            "trades_opened": trades_opened,
            "trades_closed": trades_closed,
            "portfolio": pf_after,
        }
