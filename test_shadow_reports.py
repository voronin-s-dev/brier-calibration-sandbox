"""
Unit tests for Task 4: Reporting & Dashboard Integration.
Verifies that STATUS_REPORT.md and dashboard.html include the Shadow Sandbox section,
and that report generation handles zero shadow positions without ZeroDivisionError.
"""

import tempfile
import unittest
from pathlib import Path

from dashboard_gen import generate_reports
from database import SimDatabase


class TestShadowReports(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_dir = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.db_path = Path(self.tmp_dir.name) / "test_sim.db"
        self.html_path = Path(self.tmp_dir.name) / "dashboard.html"
        self.md_path = Path(self.tmp_dir.name) / "STATUS_REPORT.md"
        self.trades_txt = Path(self.tmp_dir.name) / "trades.txt"
        self.trades_txt.write_text("INIT LOG\n", encoding="utf-8")
        self.db = SimDatabase(db_path=self.db_path, initial_capital=50.0)

    def tearDown(self) -> None:
        self.tmp_dir.cleanup()

    def test_reports_zero_division_guard(self) -> None:
        """Verify report generation succeeds with zero shadow positions."""
        paths = generate_reports(
            db=self.db,
            html_path=self.html_path,
            md_path=self.md_path,
            trades_txt_path=self.trades_txt,
        )
        self.assertTrue(self.html_path.exists())
        self.assertTrue(self.md_path.exists())

        md_content = self.md_path.read_text(encoding="utf-8")
        html_content = self.html_path.read_text(encoding="utf-8")

        self.assertIn("Теневая песочница", md_content)
        self.assertIn("Shadow Sandbox", html_content)

    def test_reports_include_shadow_stats(self) -> None:
        """Verify that when shadow positions exist, their stats appear in the markdown and HTML."""
        pos_id = self.db.open_shadow_position(
            market_id="m1", question="Crypto Q1", category="Crypto", side="YES",
            token_id="tok1", shares=10.0, entry_vwap=0.30, cost_usdc=3.00,
            initial_p_est=0.50, entry_edge=0.20, kelly_full_pct=0.10, kelly_half_pct=0.05,
            applied_size_pct=0.06, roundtrip_slippage_pct=0.01, official_source="Coinbase",
            exit_condition="Exp", rationale="Test", end_date_iso="2026-10-30"
        )
        self.db.close_shadow_position(
            pos_id=pos_id, status="RESOLVED", exit_vwap=0.60, proceeds_usdc=6.00,
            exit_reason="TP", latest_p_est=0.60
        )

        generate_reports(
            db=self.db,
            html_path=self.html_path,
            md_path=self.md_path,
            trades_txt_path=self.trades_txt,
        )

        md_content = self.md_path.read_text(encoding="utf-8")
        html_content = self.html_path.read_text(encoding="utf-8")

        self.assertIn("Crypto", md_content)
        self.assertIn("+$3.00", md_content)
        self.assertIn("Crypto", html_content)


if __name__ == "__main__":
    unittest.main()
