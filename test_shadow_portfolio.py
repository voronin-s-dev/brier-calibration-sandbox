"""
Unit tests for Task 1: Shadow Portfolio Schema and Database Layer.
Verifies strict isolation between real portfolio and shadow portfolio,
accurate cash deduction/proceeds handling, and category aggregation.
"""

import tempfile
import unittest
from pathlib import Path

from database import SimDatabase


class TestShadowPortfolioDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_dir = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.db_path = Path(self.tmp_dir.name) / "test_sim.db"
        self.db = SimDatabase(db_path=self.db_path, initial_capital=50.0)

    def tearDown(self) -> None:
        self.tmp_dir.cleanup()

    def test_shadow_schema_initialization(self) -> None:
        """Verify shadow portfolio initializes with default $50.0 virtual capital and 0 locked."""
        pf = self.db.get_shadow_portfolio()
        self.assertIsNotNone(pf)
        self.assertEqual(float(pf["initial_capital"]), 50.0)
        self.assertEqual(float(pf["cash_usdc"]), 50.0)
        self.assertEqual(float(pf["locked_usdc"]), 0.0)
        self.assertEqual(float(pf["total_equity"]), 50.0)
        self.assertEqual(float(pf["peak_equity"]), 50.0)
        self.assertEqual(int(pf["halted"]), 0)

    def test_real_and_shadow_isolation(self) -> None:
        """Opening a shadow position must never alter the real portfolio's cash, locked, or equity."""
        real_pf_before = self.db.get_portfolio()

        pos_id = self.db.open_shadow_position(
            market_id="mkt_crypto_1",
            question="Will Bitcoin break $85,000 on Friday?",
            category="Crypto",
            side="YES",
            token_id="tok_yes_123",
            shares=10.0,
            entry_vwap=0.30,
            cost_usdc=3.00,
            initial_p_est=0.45,
            entry_edge=0.15,
            kelly_full_pct=0.20,
            kelly_half_pct=0.10,
            applied_size_pct=0.06,
            roundtrip_slippage_pct=0.015,
            official_source="CoinGecko API",
            exit_condition="Edge closed or TP +12%",
            rationale="Strong spot momentum",
            end_date_iso="2026-10-30T12:00:00Z",
        )
        self.assertGreater(pos_id, 0)

        # Real portfolio must remain completely untouched
        real_pf_after = self.db.get_portfolio()
        self.assertEqual(float(real_pf_before["cash_usdc"]), float(real_pf_after["cash_usdc"]))
        self.assertEqual(float(real_pf_before["locked_usdc"]), float(real_pf_after["locked_usdc"]))
        self.assertEqual(float(real_pf_before["total_equity"]), float(real_pf_after["total_equity"]))

        # Shadow portfolio must reflect the deduction and locked equity
        shadow_pf = self.db.get_shadow_portfolio()
        self.assertAlmostEqual(float(shadow_pf["cash_usdc"]), 47.00, places=2)
        self.assertAlmostEqual(float(shadow_pf["locked_usdc"]), 3.00, places=2)
        self.assertAlmostEqual(float(shadow_pf["total_equity"]), 50.00, places=2)

    def test_shadow_position_lifecycle(self) -> None:
        """Verify opening, querying, and closing a shadow position updates shadow metrics accurately."""
        pos_id = self.db.open_shadow_position(
            market_id="mkt_weather_1",
            question="Highest temperature in Berlin above 18C?",
            category="Weather",
            side="YES",
            token_id="tok_weather_yes",
            shares=5.0,
            entry_vwap=0.40,
            cost_usdc=2.00,
            initial_p_est=0.60,
            entry_edge=0.20,
            kelly_full_pct=0.15,
            kelly_half_pct=0.075,
            applied_size_pct=0.04,
            roundtrip_slippage_pct=0.01,
            official_source="DWD Station",
            exit_condition="Resolution",
            rationale="ECMWF forecast alignment",
            end_date_iso="2026-10-31T18:00:00Z",
        )

        open_positions = self.db.get_open_shadow_positions()
        self.assertEqual(len(open_positions), 1)
        self.assertEqual(open_positions[0]["id"], pos_id)
        self.assertEqual(open_positions[0]["category"], "Weather")

        # Close with profit: settlement at $1.00/share -> $5.00 proceeds (+$3.00 PnL)
        pnl = self.db.close_shadow_position(
            pos_id=pos_id,
            status="RESOLVED",
            exit_vwap=1.00,
            proceeds_usdc=5.00,
            exit_reason="Settled YES at $1.00",
            latest_p_est=1.00,
        )
        self.assertAlmostEqual(pnl, 3.00, places=2)

        open_after = self.db.get_open_shadow_positions()
        self.assertEqual(len(open_after), 0)

        # Shadow cash must be 48.00 + 5.00 = 53.00 USDC
        shadow_pf = self.db.recalculate_shadow_portfolio()
        self.assertAlmostEqual(float(shadow_pf["cash_usdc"]), 53.00, places=2)
        self.assertAlmostEqual(float(shadow_pf["locked_usdc"]), 0.00, places=2)
        self.assertAlmostEqual(float(shadow_pf["total_equity"]), 53.00, places=2)
        self.assertAlmostEqual(float(shadow_pf["peak_equity"]), 53.00, places=2)

    def test_shadow_category_stats(self) -> None:
        """Verify category breakdown aggregates count, pnl, and wins correctly."""
        # 1. Weather winning trade (+$2.00)
        p1 = self.db.open_shadow_position(
            market_id="m1", question="Q1", category="Weather", side="YES", token_id="t1",
            shares=4.0, entry_vwap=0.50, cost_usdc=2.00, initial_p_est=0.70, entry_edge=0.20,
            kelly_full_pct=0.10, kelly_half_pct=0.05, applied_size_pct=0.04, roundtrip_slippage_pct=0.01,
            official_source="NOAA", exit_condition="Exp", rationale="Test", end_date_iso="2026-10-30"
        )
        self.db.close_shadow_position(p1, "RESOLVED", 1.00, 4.00, "Win", 1.00)

        # 2. Crypto losing trade (-$1.50)
        p2 = self.db.open_shadow_position(
            market_id="m2", question="Q2", category="Crypto", side="NO", token_id="t2",
            shares=3.0, entry_vwap=0.50, cost_usdc=1.50, initial_p_est=0.65, entry_edge=0.15,
            kelly_full_pct=0.10, kelly_half_pct=0.05, applied_size_pct=0.03, roundtrip_slippage_pct=0.01,
            official_source="Binance", exit_condition="Exp", rationale="Test", end_date_iso="2026-10-30"
        )
        self.db.close_shadow_position(p2, "RESOLVED", 0.00, 0.00, "Loss", 0.00)

        stats = self.db.get_shadow_category_stats()
        self.assertIn("Weather", stats)
        self.assertIn("Crypto", stats)

        self.assertEqual(stats["Weather"]["count"], 1)
        self.assertAlmostEqual(stats["Weather"]["pnl"], 2.00, places=2)
        self.assertEqual(stats["Weather"]["wins"], 1)

        self.assertEqual(stats["Crypto"]["count"], 1)
        self.assertAlmostEqual(stats["Crypto"]["pnl"], -1.50, places=2)
        self.assertEqual(stats["Crypto"]["wins"], 0)


if __name__ == "__main__":
    unittest.main()
