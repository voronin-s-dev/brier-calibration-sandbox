"""
Unit tests for Risk Management v2:
- Bayesian probability calibration (shrinkage toward market prior)
- Quarter-Kelly (0.25x) position sizing ($1.00..$3.00 dynamic scaling)
- Event deduplication (`1 underlying event = max 1 open position`)
- Category concentration limit (`max 3 positions per category`)
"""

import unittest
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


if __name__ == "__main__":
    unittest.main()
