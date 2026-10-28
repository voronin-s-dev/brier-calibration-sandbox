"""
Unit tests for Task 2: Shadow Market Evaluation & Position Lifecycle in GrokCharterPaperTrader.
Verifies market partitioning into active vs shadow, shadow execution logic, and shadow exit conditions.
"""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from database import SimDatabase
from polymarket_api import MarketInfo, OrderBookSimulation
from oracles import EvaluationResult
from trader import GrokCharterPaperTrader


def make_market_info(
    id: str,
    question: str,
    category: str,
    hours_to_close: float = 24.0,
    volume_24h_usd: float = 10000.0,
    liquidity_usd: float = 6000.0,
    gamma_prices: list = None,
    resolved: bool = False,
) -> MarketInfo:
    return MarketInfo(
        id=id,
        question=question,
        slug=id,
        description="",
        resolution_source="https://official.org",
        has_official_source=True,
        end_date_iso="2026-10-30T00:00:00Z",
        hours_to_close=hours_to_close,
        liquidity_usd=liquidity_usd,
        volume_24h_usd=volume_24h_usd,
        outcomes=["Yes", "No"],
        gamma_prices=gamma_prices or [0.50, 0.50],
        clob_token_ids=[f"tok_{id}_yes", f"tok_{id}_no"],
        order_min_size=1.0,
        tick_size=0.01,
        category=category,
        closed=resolved,
        resolved=resolved,
    )


class TestShadowTrader(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_dir = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.db_path = Path(self.tmp_dir.name) / "test_sim.db"
        self.trades_txt = Path(self.tmp_dir.name) / "trades.txt"
        self.db = SimDatabase(db_path=self.db_path, initial_capital=50.0)
        self.trader = GrokCharterPaperTrader(db=self.db, trades_txt_path=self.trades_txt)

    def tearDown(self) -> None:
        self.tmp_dir.cleanup()

    def test_shadow_candidate_partitioning(self) -> None:
        """When active_category_filter is 'Sports', non-sports markets must be routed to shadow candidates."""
        with self.db._connect() as conn:
            conn.execute("UPDATE portfolio_state SET active_category_filter = 'Sports' WHERE id = 1")
            conn.commit()

        m_sports = make_market_info("m_sp_1", "Lakers vs Celtics", "Sports")
        m_crypto = make_market_info("m_cr_1", "Will Bitcoin hit $80k?", "Crypto")

        active_cand, shadow_cand = self.trader.partition_markets(
            [m_sports, m_crypto],
            open_real_market_ids=set(),
            open_shadow_market_ids=set(),
            cat_filter="Sports",
            min_liq=5000.0,
        )

        self.assertEqual(len(active_cand), 1)
        self.assertEqual(active_cand[0].id, "m_sp_1")
        self.assertEqual(len(shadow_cand), 1)
        self.assertEqual(shadow_cand[0].id, "m_cr_1")

    @patch("trader.simulate_clob_buy_and_exit_check")
    def test_shadow_trade_execution(self, mock_buy: MagicMock) -> None:
        """Shadow trade meeting Edge >= 8% opens position in shadow_positions with shadow cash."""
        # Mock CLOB buy simulation
        mock_buy.return_value = OrderBookSimulation(
            token_id="tok_m_cr_2_yes",
            side_label="YES",
            best_bid=0.39,
            best_ask=0.40,
            midpoint=0.395,
            spread_pct=0.025,
            bet_usdc=3.00,
            shares_filled=7.50,
            vwap_buy_price=0.40,
            vwap_sell_price=0.39,
            entry_slippage_pct=0.01,
            exit_slippage_pct=0.01,
            roundtrip_slippage_pct=0.015,
            sufficient_depth=True,
            passes_slippage_limit=True,
        )

        m_crypto = make_market_info("m_cr_2", "Solana above $160?", "Crypto", gamma_prices=[0.40, 0.60])

        # Mock market evaluation to return strong Edge (+15 pp on YES: p_yes=0.55 vs gamma=0.40)
        self.trader._evaluate_market_probability = MagicMock(return_value=(
            EvaluationResult(
                market_id="m_cr_2",
                question="Solana above $160?",
                category="Crypto",
                oracle_used="CryptoSpot",
                official_source="Coinbase",
                p_yes=0.55,
                p_no=0.45,
                confidence=0.8,
                rationale="Spot break",
            ),
            None
        ))

        opened = self.trader.evaluate_and_execute_shadow_candidates(
            shadow_markets=[m_crypto],
            open_shadow_market_ids=set(),
        )
        self.assertEqual(opened, 1)

        # Real portfolio must still have $50 cash
        real_pf = self.db.get_portfolio()
        self.assertEqual(float(real_pf["cash_usdc"]), 50.0)

        # Shadow portfolio must have $47.00 cash and 1 open position
        shadow_pf = self.db.get_shadow_portfolio()
        self.assertAlmostEqual(float(shadow_pf["cash_usdc"]), 47.00, places=2)

        open_shadow = self.db.get_open_shadow_positions()
        self.assertEqual(len(open_shadow), 1)
        self.assertEqual(open_shadow[0]["market_id"], "m_cr_2")

    @patch("trader.fetch_market_by_id")
    def test_shadow_position_settlement(self, mock_fetch: MagicMock) -> None:
        """When market resolves, monitor_and_manage_shadow_positions closes shadow position without telegram alert."""
        pos_id = self.db.open_shadow_position(
            market_id="m_cr_resolved", question="BTC > 80k", category="Crypto", side="YES",
            token_id="tok_yes", shares=10.0, entry_vwap=0.40, cost_usdc=4.00,
            initial_p_est=0.60, entry_edge=0.20, kelly_full_pct=0.10, kelly_half_pct=0.05,
            applied_size_pct=0.05, roundtrip_slippage_pct=0.01, official_source="Coinbase",
            exit_condition="Resolution", rationale="Test", end_date_iso="2026-10-30"
        )

        # Mock market resolution: settled YES at 1.00
        mock_fetch.return_value = make_market_info(
            "m_cr_resolved", "BTC > 80k", "Crypto", hours_to_close=0.0,
            gamma_prices=[1.0, 0.0], resolved=True
        )

        closed = self.trader.monitor_and_manage_shadow_positions()
        self.assertEqual(closed, 1)

        open_shadow = self.db.get_open_shadow_positions()
        self.assertEqual(len(open_shadow), 0)

        # Shadow cash: 46.00 + 10.00 = 56.00
        shadow_pf = self.db.get_shadow_portfolio()
        self.assertAlmostEqual(float(shadow_pf["cash_usdc"]), 56.00, places=2)


if __name__ == "__main__":
    unittest.main()
