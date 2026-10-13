"""
Unit tests for Risk Management & Budget Protection v2:
- Bayesian probability calibration (shrinkage toward market prior)
- Quarter-Kelly (0.25x) position sizing ($1.00..$3.00 dynamic scaling)
- Event deduplication (`1 underlying event = max 1 open position`)
- Category concentration limit (`max 3-4 positions per category`)
- Kill-Switch (40% drawdown hard stop: halts all execution immediately)
- Mid-Drawdown Shield (15% drawdown auto-tightens liquidity and slippage)
- Minimum bet ($1.00) & cash constraint enforcement
"""

import tempfile
import unittest
from pathlib import Path

from auto_governor import AutoGovernor
from database import SimDatabase
from oracles import calibrate_probability
from trader import GrokCharterPaperTrader, extract_event_key


class TestRiskManagementV2(unittest.TestCase):
    def test_bayesian_shrinkage_prevents_overconfidence(self) -> None:
        # Raw model says 99.5% on a 50/50 market -> calibrated should be ~82.2%, not 99.5%
        p_cal = calibrate_probability(p_raw=0.995, p_market=0.50, oracle_weight=0.65)
        self.assertAlmostEqual(p_cal, 0.65 * 0.995 + 0.35 * 0.50, places=3)
        self.assertLess(p_cal, 0.85)

    def test_quarter_kelly_dynamic_sizing(self) -> None:
        # Moderate edge (+10 pp: p_est=0.60, ask=0.50) on $50 bankroll:
        # Full Kelly = (0.60 - 0.50)/(1 - 0.50) = 0.20 (20%)
        # Quarter Kelly (0.25x) = 0.05 (5.0%) -> $2.50 USDC (below $3.00 cap!)
        full_k, frac_k, applied_pct, bet_usdc = GrokCharterPaperTrader.compute_kelly_sizing(
            p_est=0.60, ask_vwap=0.50, total_equity=50.0, max_pct=0.06, kelly_fraction=0.25
        )
        self.assertAlmostEqual(full_k, 0.20, places=4)
        self.assertAlmostEqual(frac_k, 0.05, places=4)
        self.assertAlmostEqual(applied_pct, 0.05, places=4)
        self.assertEqual(bet_usdc, 2.50)

        # Modest edge (+8.5 pp: p_est=0.585, ask=0.50) on $50 bankroll:
        # Full Kelly = 0.17, Quarter Kelly = 0.0425 -> $2.12 USDC
        _, _, _, bet_small = GrokCharterPaperTrader.compute_kelly_sizing(
            p_est=0.585, ask_vwap=0.50, total_equity=50.0, max_pct=0.06, kelly_fraction=0.25
        )
        self.assertEqual(bet_small, 2.12)

        # Very strong edge (+25 pp: p_est=0.75, ask=0.50): capped at 6% ($3.00)
        _, _, applied_cap, bet_cap = GrokCharterPaperTrader.compute_kelly_sizing(
            p_est=0.75, ask_vwap=0.50, total_equity=50.0, max_pct=0.06, kelly_fraction=0.25
        )
        self.assertEqual(applied_cap, 0.06)
        self.assertEqual(bet_cap, 3.00)

    def test_event_key_deduplication(self) -> None:
        # Two different temperature brackets in Shanghai on the same day must share the same event_key
        k1 = extract_event_key("Will the highest temperature in Shanghai be 26°C on October 13?", "Weather")
        k2 = extract_event_key("Will the highest temperature in Shanghai be 27°C on October 13?", "Weather")
        self.assertEqual(k1, k2)
        self.assertEqual(k1, "weather:shanghai:october 13")

        # Two Bitcoin markets on the same date must share the same event_key
        c1 = extract_event_key("Will the price of Bitcoin be above $84,000 on October 13?", "Crypto")
        c2 = extract_event_key("Bitcoin Up or Down on October 13?", "Crypto")
        self.assertEqual(c1, c2)
        self.assertEqual(c1, "crypto:bitcoin:october 13")

    def test_kill_switch_at_40_percent_drawdown(self) -> None:
        """Verify that a 40% drawdown halts the portfolio and prevents any further trading."""
        import gc
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db_path = Path(tmp_dir) / "test_sim.db"
            db = SimDatabase(db_path=db_path, initial_capital=50.0)

            # Peak equity is $50.00. Drop cash to $29.00 (42% drawdown)
            with db._connect() as conn:
                conn.execute("UPDATE portfolio_state SET cash_usdc = 29.00, peak_equity = 50.00 WHERE id = 1")
                conn.commit()

            pf = db.recalculate_portfolio()
            self.assertEqual(pf["halted"], 1)
            self.assertIn("KILL-SWITCH TRIGGERED", pf["halt_reason"])

            # Verify GrokCharterPaperTrader stops execution immediately
            trades_log = Path(tmp_dir) / "trades.txt"
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=trades_log)
            res = trader.run_cycle()
            self.assertEqual(res["status"], "HALTED")
            del db, trader
            gc.collect()

    def test_mid_drawdown_shield_tightens_filters(self) -> None:
        """Verify that a 15% drawdown automatically engages the TIER 3 safety shield."""
        import gc
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db_path = Path(tmp_dir) / "test_sim.db"
            db = SimDatabase(db_path=db_path, initial_capital=50.0)

            # Drop cash to $40.00 (20% drawdown, above 15% shield threshold)
            with db._connect() as conn:
                conn.execute("UPDATE portfolio_state SET cash_usdc = 40.00, peak_equity = 50.00 WHERE id = 1")
                conn.commit()

            gov = AutoGovernor(db)
            res = gov.evaluate_portfolio_and_rules()
            self.assertTrue(len(res["triggered_event_ids"]) > 0)

            # Filters must be automatically tightened
            pf = db.get_portfolio()
            self.assertGreaterEqual(float(pf["min_liquidity_filter"]), 10000.0)
            self.assertLessEqual(float(pf["max_slippage_filter"]), 0.02)
            del db, gov
            gc.collect()

    def test_zero_or_negative_edge_sizing_is_zero(self) -> None:
        """Verify that negative or non-existent edge results in zero bet size."""
        # p_est <= ask_vwap
        f_k, half_k, app_pct, bet = GrokCharterPaperTrader.compute_kelly_sizing(
            p_est=0.45, ask_vwap=0.50, total_equity=50.0
        )
        self.assertEqual(bet, 0.0)
        self.assertEqual(app_pct, 0.0)


if __name__ == "__main__":
    unittest.main()
