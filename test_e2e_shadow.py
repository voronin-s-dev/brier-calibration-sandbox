"""
End-to-end integration test for Shadow Portfolio (Sandbox).
Verifies a full cycle with dual-track execution:
- Real trading executes on Sports (high conviction)
- Shadow sandbox executes on Crypto
- Both real and shadow state update with strict isolation
- Reports and governance reports render correctly
"""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from auto_governor import AutoGovernor
from dashboard_gen import generate_reports
from database import SimDatabase
from polymarket_api import MarketInfo, OrderBookSimulation
from oracles import EvaluationResult
from trader import GrokCharterPaperTrader


def make_market(id: str, question: str, category: str, gamma_prices: list) -> MarketInfo:
    return MarketInfo(
        id=id,
        question=question,
        slug=id,
        description="",
        resolution_source="https://official.org",
        has_official_source=True,
        end_date_iso="2026-10-31T00:00:00Z",
        hours_to_close=24.0,
        liquidity_usd=8000.0,
        volume_24h_usd=20000.0,
        outcomes=["Yes", "No"],
        gamma_prices=gamma_prices,
        clob_token_ids=[f"tok_{id}_yes", f"tok_{id}_no"],
        order_min_size=1.0,
        tick_size=0.01,
        category=category,
        closed=False,
        resolved=False,
    )


class TestE2EShadowPortfolio(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_dir = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.db_path = Path(self.tmp_dir.name) / "test_sim.db"
        self.trades_txt = Path(self.tmp_dir.name) / "trades.txt"
        self.html_path = Path(self.tmp_dir.name) / "dashboard.html"
        self.md_path = Path(self.tmp_dir.name) / "STATUS_REPORT.md"
        self.db = SimDatabase(db_path=self.db_path, initial_capital=50.0)
        self.trader = GrokCharterPaperTrader(db=self.db, trades_txt_path=self.trades_txt)

        # Restrict real trading to Sports
        with self.db._connect() as conn:
            conn.execute("UPDATE portfolio_state SET active_category_filter = 'Sports' WHERE id = 1")
            conn.commit()

    def tearDown(self) -> None:
        self.tmp_dir.cleanup()

    @patch("trader.fetch_active_markets")
    @patch("trader.simulate_clob_buy_and_exit_check")
    def test_e2e_dual_track_execution(self, mock_buy: MagicMock, mock_markets: MagicMock) -> None:
        """Simulate a complete cycle with 1 Sports market and 1 Crypto market."""
        m_sports = make_market("m_sp_100", "Lakers vs Warriors", "Sports", [0.84, 0.16])
        m_crypto = make_market("m_cr_100", "Bitcoin > 82k", "Crypto", [0.40, 0.60])
        mock_markets.return_value = [m_sports, m_crypto]

        # Mock CLOB buy simulation
        def side_effect_buy(token_id, side_label, bet_usdc, max_slippage_pct, preloaded_book=None):
            price = 0.84 if "sp_100" in token_id else 0.40
            return OrderBookSimulation(
                token_id=token_id,
                side_label=side_label,
                best_bid=price - 0.01,
                best_ask=price,
                midpoint=price - 0.005,
                spread_pct=0.015,
                bet_usdc=bet_usdc,
                shares_filled=bet_usdc / price,
                vwap_buy_price=price,
                vwap_sell_price=price - 0.01,
                entry_slippage_pct=0.01,
                exit_slippage_pct=0.01,
                roundtrip_slippage_pct=0.015,
                sufficient_depth=True,
                passes_slippage_limit=True,
            )

        mock_buy.side_effect = side_effect_buy

        # Mock evaluation: sports is high conviction (95%), crypto is shadow (55%)
        def side_effect_eval(mkt):
            p_yes = 0.95 if mkt.category == "Sports" else 0.55
            return (
                EvaluationResult(
                    market_id=mkt.id, question=mkt.question, category=mkt.category,
                    oracle_used="TestOracle", official_source="ESPN/Coinbase",
                    p_yes=p_yes, p_no=1.0 - p_yes, confidence=0.85, rationale="Strong Edge",
                ),
                None,
            )

        self.trader._evaluate_market_probability = MagicMock(side_effect=side_effect_eval)

        # Run 1 cycle
        cycle_res = self.trader.run_cycle(max_markets_to_scan=10)
        self.assertEqual(cycle_res["trades_opened"], 1)

        # Verify real portfolio: 1 open Sports position, cash deducted
        real_positions = self.db.get_open_positions()
        self.assertEqual(len(real_positions), 1)
        self.assertEqual(real_positions[0]["category"], "Sports")
        real_pf = self.db.get_portfolio()
        self.assertLess(float(real_pf["cash_usdc"]), 50.0)

        # Verify shadow portfolio: 1 open Crypto position, shadow cash deducted
        shadow_positions = self.db.get_open_shadow_positions()
        self.assertEqual(len(shadow_positions), 1)
        self.assertEqual(shadow_positions[0]["category"], "Crypto")
        shadow_pf = self.db.get_shadow_portfolio()
        self.assertLess(float(shadow_pf["cash_usdc"]), 50.0)

        # Generate reports and verify both files render
        paths = generate_reports(self.db, self.html_path, self.md_path, self.trades_txt)
        self.assertTrue(self.html_path.exists())
        self.assertTrue(self.md_path.exists())

        md_content = self.md_path.read_text(encoding="utf-8")
        self.assertIn("Теневая песочница", md_content)
        self.assertIn("Sports", md_content)


if __name__ == "__main__":
    unittest.main()
