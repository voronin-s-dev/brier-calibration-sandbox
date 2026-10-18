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

    def test_conservative_v3_defaults_and_horizon(self) -> None:
        """Verify that Risk Management v3 enforces 0.25x Kelly and 4% max cap by default."""
        # Strong edge (+30 pp: p_est=0.80, ask=0.50) on $50 bankroll:
        # Full Kelly = 0.60, Quarter Kelly = 0.15
        # Default cap is 4% (0.04) -> max $2.00 USDC
        full_k, frac_k, applied_pct, bet = GrokCharterPaperTrader.compute_kelly_sizing(
            p_est=0.80, ask_vwap=0.50, total_equity=50.0
        )
        self.assertAlmostEqual(full_k, 0.60, places=4)
        self.assertAlmostEqual(frac_k, 0.15, places=4)
        self.assertEqual(applied_pct, 0.04)
        self.assertEqual(bet, 2.00)
        self.assertEqual(GrokCharterPaperTrader.MIN_HOURS_TO_CLOSE, 12.0)
        self.assertEqual(GrokCharterPaperTrader.EXIT_HOURS_THRESHOLD, 1.5)
        self.assertEqual(GrokCharterPaperTrader.STOP_LOSS_PCT, 0.30)
        self.assertEqual(GrokCharterPaperTrader.MIN_EDGE_PP, 0.08)

    def test_stop_loss_triggers_on_steep_price_drop(self) -> None:
        """Verify that a position is liquidated when Bid falls > 35% below entry."""
        import gc
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db_path = Path(tmp_dir) / "test_sim.db"
            db = SimDatabase(db_path=db_path, initial_capital=50.0)
            trades_log = Path(tmp_dir) / "trades.txt"
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=trades_log)

            # Open a virtual position with entry 0.50
            pos_id = db.open_position(
                market_id="test_mkt_1",
                question="Will Test Event Happen?",
                category="Crypto",
                side="YES",
                token_id="tok_123",
                shares=10.0,
                entry_vwap=0.50,
                cost_usdc=5.00,
                current_bid=0.50,
                p_est=0.65,
                entry_edge=0.15,
                kelly_full_pct=0.30,
                kelly_half_pct=0.075,
                applied_size_pct=0.04,
                roundtrip_slippage_pct=0.01,
                official_source="Test Source",
                exit_condition="Test Condition",
                rationale="Test Rationale",
                end_date_iso="2026-10-25T12:00:00Z",
            )

            # Mock simulate_clob_sell_shares to return 0.28 (44% drop from 0.50, exceeds 35% stop)
            import trader as trader_mod
            orig_sim = trader_mod.simulate_clob_sell_shares
            try:
                trader_mod.simulate_clob_sell_shares = lambda tok, sh: (0.28, 2.80, 0.28)
                closed = trader.monitor_and_manage_open_positions()
                self.assertEqual(closed, 1)

                closed_pos = db.get_all_positions()[0]
                self.assertEqual(closed_pos["status"], "CLOSED")
                self.assertIn("STOP-LOSS TRIGGERED", closed_pos["exit_reason"])
                self.assertEqual(closed_pos["exit_vwap"], 0.28)
            finally:
                trader_mod.simulate_clob_sell_shares = orig_sim
                del db, trader
                gc.collect()

    def test_whipsaw_prevented_when_edge_still_above_entry(self) -> None:
        """Verify that a drop in P_est does NOT exit if P_est remains above entry price."""
        import gc
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db_path = Path(tmp_dir) / "test_sim.db"
            db = SimDatabase(db_path=db_path, initial_capital=50.0)
            trades_log = Path(tmp_dir) / "trades.txt"
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=trades_log)

            # Open position: entry 0.50, initial_p=0.85
            pos_id = db.open_position(
                market_id="test_mkt_2",
                question="Will Test Event Happen?",
                category="Weather",
                side="NO",
                token_id="tok_456",
                shares=10.0,
                entry_vwap=0.50,
                cost_usdc=5.00,
                current_bid=0.52,
                p_est=0.85,
                entry_edge=0.35,
                kelly_full_pct=0.40,
                kelly_half_pct=0.10,
                applied_size_pct=0.04,
                roundtrip_slippage_pct=0.01,
                official_source="Test Source",
                exit_condition="Test Condition",
                rationale="Test Rationale",
                end_date_iso="2026-10-25T12:00:00Z",
            )

            # P_est drops from 0.85 to 0.72 (-13 pp shift, exceeds prob_shift_limit of 10 pp),
            # BUT 0.72 is still above entry 0.50 (edge is still positive!). Must NOT exit!
            import trader as trader_mod
            orig_sim = trader_mod.simulate_clob_sell_shares
            orig_fetch = trader_mod.fetch_market_by_id
            try:
                trader_mod.simulate_clob_sell_shares = lambda tok, sh: (0.52, 5.20, 0.52)
                # Mock live_mkt evaluation to return 0.72
                from polymarket_api import MarketInfo
                mock_mkt = MarketInfo(
                    id="test_mkt_2", question="Test", slug="test", description="", resolution_source="test",
                    has_official_source=True, end_date_iso="2026-10-25T12:00:00Z", hours_to_close=100.0,
                    liquidity_usd=5000.0, volume_24h_usd=1000.0, outcomes=["YES", "NO"],
                    gamma_prices=[0.28, 0.72], clob_token_ids=["tok_yes", "tok_456"], order_min_size=1.0,
                    tick_size=0.01, category="Weather"
                )
                trader_mod.fetch_market_by_id = lambda m_id: mock_mkt
                from oracles import EvaluationResult
                trader._evaluate_market_probability = lambda mkt: (
                    EvaluationResult(
                        market_id="test_mkt_2", question="Test", category="Weather", oracle_used="Mock",
                        official_source="Mock", p_yes=0.28, p_no=0.72, confidence=0.8, rationale="Mock"
                    ), None
                )

                closed = trader.monitor_and_manage_open_positions()
                self.assertEqual(closed, 0)  # Must remain open!

                pos = db.get_open_positions()[0]
                self.assertEqual(pos["status"], "OPEN")
            finally:
                trader_mod.simulate_clob_sell_shares = orig_sim
                trader_mod.fetch_market_by_id = orig_fetch
                del db, trader
                gc.collect()

    def test_kill_switch_resets_and_rebaselines(self) -> None:
        """Verify that reset_kill_switch re-baselines peak equity and clears halted status."""
        import gc
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db_path = Path(tmp_dir) / "test_sim.db"
            db = SimDatabase(db_path=db_path, initial_capital=50.0)

            # Drop cash to $28.00 (44% drawdown from $50 peak) -> triggers halt
            with db._connect() as conn:
                conn.execute("UPDATE portfolio_state SET cash_usdc = 28.00, peak_equity = 50.00 WHERE id = 1")
                conn.commit()

            pf = db.recalculate_portfolio()
            self.assertEqual(pf["halted"], 1)

            # Reset kill switch
            pf_reset = db.reset_kill_switch()
            self.assertEqual(pf_reset["halted"], 0)
            self.assertEqual(pf_reset["halt_reason"], "")
            self.assertEqual(pf_reset["peak_equity"], 28.00)
            self.assertEqual(pf_reset["current_drawdown_pct"], 0.0)
            del db
            gc.collect()

    def test_open_positions_monitored_even_when_halted(self) -> None:
        """Verify that run_cycle calls monitor_and_manage_open_positions even if portfolio is halted."""
        import gc
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db_path = Path(tmp_dir) / "test_sim.db"
            trades_log = Path(tmp_dir) / "trades.txt"
            db = SimDatabase(db_path=db_path, initial_capital=50.0)

            # Drop cash to trigger halt
            with db._connect() as conn:
                conn.execute("UPDATE portfolio_state SET cash_usdc = 28.00, peak_equity = 50.00 WHERE id = 1")
                conn.commit()

            db.recalculate_portfolio()
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=trades_log)

            monitored = False
            def mock_monitor():
                nonlocal monitored
                monitored = True
                return 0

            trader.monitor_and_manage_open_positions = mock_monitor
            res = trader.run_cycle()
            self.assertTrue(monitored)
            self.assertEqual(res["status"], "HALTED")
            del db, trader
            gc.collect()


if __name__ == "__main__":
    unittest.main()

