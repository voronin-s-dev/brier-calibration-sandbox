"""
Unit tests for Task 3: Auto-Governor Tier 2 Shadow Category Recovery Audit and Unfreeze Proposals.
Verifies that when a disabled category proves profitable in the sandbox, an unfreeze proposal is generated.
"""

import tempfile
import unittest
from pathlib import Path

import auto_governor
from auto_governor import AutoGovernor
from database import SimDatabase
import telegram_notify

# Silence live Telegram alerts during unit test execution
telegram_notify.send_telegram_alert = lambda text: False
auto_governor.send_telegram_alert = lambda text: False


class TestShadowGovernor(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_dir = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.db_path = Path(self.tmp_dir.name) / "test_sim.db"
        self.gov_report_path = Path(self.tmp_dir.name) / "GOVERNANCE_REPORT.md"
        self.db = SimDatabase(db_path=self.db_path, initial_capital=50.0)
        self.gov = AutoGovernor(self.db, report_path=self.gov_report_path)

        # Set active filter to Sports
        with self.db._connect() as conn:
            conn.execute("UPDATE portfolio_state SET active_category_filter = 'Sports' WHERE id = 1")
            conn.commit()

    def tearDown(self) -> None:
        self.tmp_dir.cleanup()

    def test_unfreeze_proposal_triggered_on_strong_shadow_performance(self) -> None:
        """When shadow Crypto closes >= 5 trades with PnL >= +$1.50 and WR >= 60%, unfreeze proposal must trigger."""
        # Insert 5 winning trades in shadow Crypto (total PnL: +$2.50, WR 100%)
        for i in range(5):
            pos_id = self.db.open_shadow_position(
                market_id=f"m_cr_{i}", question=f"Crypto Q{i}", category="Crypto", side="YES",
                token_id=f"tok_{i}", shares=5.0, entry_vwap=0.50, cost_usdc=2.50,
                initial_p_est=0.70, entry_edge=0.20, kelly_full_pct=0.10, kelly_half_pct=0.05,
                applied_size_pct=0.05, roundtrip_slippage_pct=0.01, official_source="Coinbase",
                exit_condition="Exp", rationale="Test", end_date_iso="2026-10-30"
            )
            self.db.close_shadow_position(
                pos_id=pos_id, status="RESOLVED", exit_vwap=0.60, proceeds_usdc=3.00,
                exit_reason="TP", latest_p_est=0.60
            )

        res = self.gov.evaluate_portfolio_and_rules()
        events = self.gov.get_pending_proposals() if hasattr(self.gov, "get_pending_proposals") else []

        with self.db._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM governance_events WHERE rule_key LIKE 'tier2_shadow_unfreeze_crypto_%'"
            ).fetchall()

        self.assertEqual(len(rows), 1)
        event = dict(rows[0])
        self.assertEqual(event["status"], "PENDING_APPROVAL")
        self.assertEqual(event["tier"], "TIER_2_CALIBRATION")
        self.assertIn("Разморозка категории Crypto", event["title"])
        self.assertIn('"active_category_filter": "ALL"', event["proposed_action_json"])

    def test_unfreeze_requires_minimum_five_trades(self) -> None:
        """If shadow category has only 2 winning trades, it must not trigger an unfreeze proposal yet."""
        for i in range(2):
            pos_id = self.db.open_shadow_position(
                market_id=f"m_cr_few_{i}", question=f"Crypto Q{i}", category="Crypto", side="YES",
                token_id=f"tok_{i}", shares=5.0, entry_vwap=0.50, cost_usdc=2.50,
                initial_p_est=0.70, entry_edge=0.20, kelly_full_pct=0.10, kelly_half_pct=0.05,
                applied_size_pct=0.05, roundtrip_slippage_pct=0.01, official_source="Coinbase",
                exit_condition="Exp", rationale="Test", end_date_iso="2026-10-30"
            )
            self.db.close_shadow_position(
                pos_id=pos_id, status="RESOLVED", exit_vwap=0.80, proceeds_usdc=4.00,
                exit_reason="TP", latest_p_est=0.80
            )

        self.gov.evaluate_portfolio_and_rules()

        with self.db._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM governance_events WHERE rule_key LIKE 'tier2_shadow_unfreeze_%'"
            ).fetchall()

        self.assertEqual(len(rows), 0)

    def test_brier_calibration_auto_dismissed_when_score_heals(self) -> None:
        """When Brier score is <= 0.22, pending tier2_brier_calibration proposals must be auto-dismissed."""
        ev_id = self.gov._record_event(
            rule_key="tier2_brier_calibration_batch_1",
            tier="TIER_2_CALIBRATION",
            mode="SEMI_AUTO",
            status="PENDING_APPROVAL",
            title="Калибровка Brier Score (0.230)",
            explanation="Old bad brier score",
            action_dict={"oracle_weight": 0.53},
        )
        pos_id = self.db.open_position(
            market_id="m_good", question="Good mkt", category="Sports", side="YES",
            token_id="tok_g", shares=5.0, entry_vwap=0.85, cost_usdc=4.25,
            current_bid=0.85, p_est=0.90, entry_edge=0.05, kelly_full_pct=0.10, kelly_half_pct=0.05,
            applied_size_pct=0.05, roundtrip_slippage_pct=0.01, official_source="Official",
            exit_condition="Exp", rationale="Good", end_date_iso="2026-10-30"
        )
        self.db.close_position(
            pos_id=pos_id, status="RESOLVED", exit_vwap=1.00, proceeds_usdc=5.00,
            exit_reason="Resolution", latest_p_est=0.95
        )

        self.gov.evaluate_portfolio_and_rules()

        with self.db._connect() as conn:
            row = conn.execute("SELECT status, explanation FROM governance_events WHERE id = ?", (ev_id,)).fetchone()

        self.assertEqual(row["status"], "DISMISSED")
        self.assertIn("[DISMISSED]:", row["explanation"])
        self.assertIn("Самоисцеление метрики", row["explanation"])



if __name__ == "__main__":
    unittest.main()
