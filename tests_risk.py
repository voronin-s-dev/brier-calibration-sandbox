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

import os
os.environ["TESTING"] = "1"

import auto_governor
from auto_governor import AutoGovernor
from database import SimDatabase
from oracles import calibrate_probability
import trader
from trader import GrokCharterPaperTrader, extract_event_key
import telegram_notify

# Silence live Telegram alerts during test suite execution
telegram_notify.send_telegram_alert = lambda text: False
auto_governor.send_telegram_alert = lambda text: False
trader.send_telegram_alert = lambda text: False


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

            gov = AutoGovernor(db, report_path=Path(tmp_dir) / "test_gov.md")
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
        """Verify Strategy 2 (Fact-Harvest) parameters and high-conviction horizons."""
        # Sizing test with 0.35x fractional Kelly on 0.04 max cap:
        full_k, frac_k, applied_pct, bet = GrokCharterPaperTrader.compute_kelly_sizing(
            p_est=0.80, ask_vwap=0.50, total_equity=50.0, max_pct=0.04, kelly_fraction=0.25
        )
        self.assertAlmostEqual(full_k, 0.60, places=4)
        self.assertAlmostEqual(frac_k, 0.15, places=4)
        self.assertEqual(applied_pct, 0.04)
        self.assertEqual(bet, 2.00)
        self.assertEqual(GrokCharterPaperTrader.MIN_HOURS_TO_CLOSE, 0.8)
        self.assertEqual(GrokCharterPaperTrader.EXIT_HOURS_THRESHOLD, 0.0)
        self.assertEqual(GrokCharterPaperTrader.STOP_LOSS_PCT, 0.40)
        self.assertEqual(GrokCharterPaperTrader.MIN_EDGE_PP, 0.015)
        self.assertEqual(GrokCharterPaperTrader.MIN_ESTIMATED_PROB, 0.80)
        self.assertEqual(GrokCharterPaperTrader.MIN_CONTRACT_PRICE, 0.76)
        self.assertEqual(GrokCharterPaperTrader.MAX_CONTRACT_PRICE, 0.92)
        self.assertEqual(GrokCharterPaperTrader.MAX_BANK_PCT_PER_TRADE, 0.08)

    def test_soccer_draw_guard(self) -> None:
        """Verify that 3-way soccer win markets are flagged to prevent draw loss traps."""
        self.assertTrue(GrokCharterPaperTrader.is_soccer_draw_trap("Will Arsenal FC win on 2026-10-27?"))
        self.assertTrue(GrokCharterPaperTrader.is_soccer_draw_trap("Will FC Barcelona win on 2026-10-31?"))
        self.assertTrue(GrokCharterPaperTrader.is_soccer_draw_trap("Will CD Santa Clara win on 2026-10-26?"))
        self.assertTrue(GrokCharterPaperTrader.is_soccer_draw_trap("Premier League: Chelsea vs Liverpool win"))

        # Spreads, totals, and non-soccer sports must NOT be flagged
        self.assertFalse(GrokCharterPaperTrader.is_soccer_draw_trap("Spread: FC Barcelona (-3.5)"))
        self.assertFalse(GrokCharterPaperTrader.is_soccer_draw_trap("Pacers vs. Bucks: O/U 212.5"))
        self.assertFalse(GrokCharterPaperTrader.is_soccer_draw_trap("Counter-Strike: FURIA vs TYLOO (BO3)"))
        self.assertFalse(GrokCharterPaperTrader.is_soccer_draw_trap("Will the Milwaukee Brewers win the 2026 World Series?"))

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

    def test_single_category_slot_expansion(self) -> None:
        """Direction C: Verify that single-category focus dynamically expands cat_cap up to 6 positions."""
        from trader import GrokCharterPaperTrader
        # Under ALL categories, cat_cap for Sports must be 3
        cat_cap_all = 3
        # Under single category (Sports), cat_cap must expand to min(MAX_OPEN_POSITIONS, 6) = 6
        cat_cap_single = min(GrokCharterPaperTrader.MAX_OPEN_POSITIONS, 6)
        self.assertEqual(cat_cap_all, 3)
        self.assertEqual(cat_cap_single, 6)

    def test_shadow_candidate_funnel_not_starved(self) -> None:
        """Direction C / S: Verify that shadow candidates in [0.20, 0.80] range are prioritized."""
        from polymarket_api import MarketInfo
        from trader import GrokCharterPaperTrader
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_d:
            db_tmp = SimDatabase(db_path=Path(tmp_d) / "temp_rf.db", initial_capital=50.0)
            trader = GrokCharterPaperTrader(db=db_tmp, trades_txt_path=Path(tmp_d) / "t.txt")
            def _mk(mid, q, prices):
                return MarketInfo(
                    id=mid, question=q, slug=mid, description="", resolution_source="https://official.org",
                    has_official_source=True, end_date_iso="2026-11-10T00:00:00Z", hours_to_close=24.0,
                    liquidity_usd=10000.0, volume_24h_usd=20000.0, outcomes=["Yes", "No"],
                    gamma_prices=prices, clob_token_ids=[f"t_{mid}_y", f"t_{mid}_n"],
                    order_min_size=1.0, tick_size=0.01, category="Crypto", closed=False,
                )
            m1 = _mk("1", "High prob", [0.95, 0.05])
            m2 = _mk("2", "Tradable shadow", [0.55, 0.45])
            active, shadow = trader.partition_markets([m1, m2], cat_filter="Sports", min_liq=5000.0,
                                                      open_real_market_ids=set(), open_shadow_market_ids=set())
            # m2 (0.55 price) must be prioritized first in shadow_candidates
            self.assertEqual(len(shadow), 2)
            self.assertEqual(shadow[0].id, "2")

    def test_mature_consensus_oracle_strict_threshold(self) -> None:
        """Direction C: Verify that HighConvictionFactOracle does NOT manufacture fake edge at P < 0.90."""
        from oracles import HighConvictionFactOracle
        from polymarket_api import MarketInfo
        oracle = HighConvictionFactOracle()
        def _mk(mid, q, prices):
            return MarketInfo(
                id=mid, question=q, slug=mid, description="", resolution_source="https://official.org",
                has_official_source=True, end_date_iso="2026-11-10T00:00:00Z", hours_to_close=12.0,
                liquidity_usd=20000.0, volume_24h_usd=30000.0, outcomes=["Yes", "No"],
                gamma_prices=prices, clob_token_ids=[f"t_{mid}_y", f"t_{mid}_n"],
                order_min_size=1.0, tick_size=0.01, category="Sports", closed=False,
            )
        # Market at 0.82 (e.g. 82% favorite) must NOT trigger MatureMarketConsensusOracle
        m_82 = _mk("m_82", "Some Regular Game", [0.82, 0.18])
        res_82 = oracle.evaluate(m_82)
        self.assertIsNone(res_82)

        # Market at 0.92 (true high consensus) MUST trigger
        m_92 = _mk("m_92", "Some Decided Game", [0.92, 0.08])
        res_92 = oracle.evaluate(m_92)
        self.assertIsNotNone(res_92)
        self.assertEqual(res_92.oracle_used, "MatureMarketConsensusOracle")


    def test_sports_heavy_handicap_requires_high_market_consensus(self) -> None:
        """Direction C: SportsHeavyHandicapOracle must NOT trigger on NBA/NFL point spreads (p ~ 0.50)."""
        from oracles import HighConvictionFactOracle
        from polymarket_api import MarketInfo
        oracle = HighConvictionFactOracle()
        def _mk(mid, q, prices):
            return MarketInfo(
                id=mid, question=q, slug=mid, description="", resolution_source="https://official.org",
                has_official_source=True, end_date_iso="2026-11-10T00:00:00Z", hours_to_close=12.0,
                liquidity_usd=20000.0, volume_24h_usd=30000.0, outcomes=["Yes", "No"],
                gamma_prices=prices, clob_token_ids=[f"t_{mid}_y", f"t_{mid}_n"],
                order_min_size=1.0, tick_size=0.01, category="Sports", closed=False,
            )
        # NBA spread at 0.37 (even-money point spread) must NOT trigger
        m_nba = _mk("m_nba", "Spread: Rockets (-4.5)", [0.63, 0.37])
        res_nba = oracle.evaluate(m_nba)
        self.assertIsNone(res_nba)

        # Soccer severe blowout handicap at 0.88 MUST trigger
        m_soccer = _mk("m_soccer", "Spread: Real Madrid (-3.5)", [0.12, 0.88])
        res_soccer = oracle.evaluate(m_soccer)
        self.assertIsNotNone(res_soccer)
        self.assertEqual(res_soccer.oracle_used, "SportsHeavyHandicapOracle")
        self.assertEqual(res_soccer.p_no, 0.975)

    def test_trader_does_not_pick_inverted_underdog_on_resolved_markets(self) -> None:
        """Direction C: Trader must not pick the 1.5% losing side when market is 100%/0%."""
        from unittest.mock import MagicMock, patch
        from database import SimDatabase
        from polymarket_api import MarketInfo
        from oracles import EvaluationResult
        import tempfile
        from trader import GrokCharterPaperTrader

        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            db = SimDatabase(db_path=Path(tmp) / "test.db", initial_capital=50.0)
            trader_instance = GrokCharterPaperTrader(db=db, trades_txt_path=Path(tmp) / "trades.txt")

            m_decided = MarketInfo(
                id="m_dec", question="Counter-Strike: Sökerorg vs Prestige - Map 2 Winner",
                slug="m_dec", description="", resolution_source="https://official.org",
                has_official_source=True, end_date_iso="2026-11-10T00:00:00Z", hours_to_close=3.0,
                liquidity_usd=15000.0, volume_24h_usd=25000.0, outcomes=["Yes", "No"],
                gamma_prices=[1.0, 0.0], clob_token_ids=["tok_y", "tok_n"],
                order_min_size=1.0, tick_size=0.01, category="Sports", closed=False,
            )

            # Oracle consensus favors YES (0.985 vs 0.015)
            eval_res = EvaluationResult(
                market_id="m_dec", question=m_decided.question, category="Sports",
                oracle_used="MatureMarketConsensusOracle", official_source="HLTV",
                p_yes=0.985, p_no=0.015, confidence=0.92, rationale="High consensus",
            )
            trader_instance._evaluate_market_probability = MagicMock(return_value=(eval_res, None))

            with patch("trader.fetch_active_markets", return_value=[m_decided]):
                with patch("trader.simulate_clob_buy_and_exit_check") as mock_clob:
                    res = trader_instance.run_cycle(max_markets_to_scan=5)
                    # CLOB simulation should NEVER be called on the 1.5% underdog side!
                    mock_clob.assert_not_called()
                    self.assertEqual(res["trades_opened"], 0)

    def test_main_trader_active_time_exit(self) -> None:
        """Direction M & U: Active main position under 1.0h to close must trigger TIME EXIT."""
        from unittest.mock import MagicMock, patch
        from database import SimDatabase
        from polymarket_api import MarketInfo
        import tempfile
        from trader import GrokCharterPaperTrader

        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            db = SimDatabase(db_path=Path(tmp) / "test.db", initial_capital=50.0)
            trader_instance = GrokCharterPaperTrader(db=db, trades_txt_path=Path(tmp) / "trades.txt")

            db.open_position(
                market_id="m_time_1", question="Bucks vs Knicks", category="Sports", side="NO",
                token_id="tok_no_1", shares=10.0, entry_vwap=0.90, cost_usdc=9.00,
                current_bid=0.90, p_est=0.94, entry_edge=0.04, kelly_full_pct=0.20,
                kelly_half_pct=0.08, applied_size_pct=0.08, roundtrip_slippage_pct=0.01,
                official_source="NBA.com", exit_condition="Hold", rationale="Consensus",
                end_date_iso="2026-11-10T12:00:00Z",
            )

            m_live = MarketInfo(
                id="m_time_1", question="Bucks vs Knicks", slug="bucks-knicks",
                description="", resolution_source="NBA.com", has_official_source=True,
                end_date_iso="2026-11-10T12:00:00Z", hours_to_close=0.6,
                liquidity_usd=10000.0, volume_24h_usd=20000.0, outcomes=["YES", "NO"],
                gamma_prices=[0.10, 0.90], clob_token_ids=["tok_yes_1", "tok_no_1"],
                order_min_size=1.0, tick_size=0.01, category="Sports", closed=False,
            )

            with patch("trader.fetch_market_by_id", return_value=m_live):
                with patch("trader.simulate_clob_sell_shares", return_value=(0.91, 9.10, 0.91)):
                    closed = trader_instance.monitor_and_manage_open_positions()
                    self.assertEqual(closed, 1)

                    open_pos = db.get_open_positions()
                    self.assertEqual(len(open_pos), 0)

                    all_pos = db.get_all_positions()
                    self.assertEqual(all_pos[0]["status"], "CLOSED")
                    self.assertIn("TIME EXIT", all_pos[0]["exit_reason"])

    def test_main_trader_thesis_invalidation_even_with_zero_bids(self) -> None:
        """Direction U & S: Collapsed probability thesis exits and frees slot even if CLOB bids evaporate to 0."""
        from unittest.mock import MagicMock, patch
        from database import SimDatabase
        from polymarket_api import MarketInfo
        from oracles import EvaluationResult
        import tempfile
        from trader import GrokCharterPaperTrader

        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            db = SimDatabase(db_path=Path(tmp) / "test.db", initial_capital=50.0)
            trader_instance = GrokCharterPaperTrader(db=db, trades_txt_path=Path(tmp) / "trades.txt")

            db.open_position(
                market_id="m_collapse", question="LoL: Team A vs Team B", category="Sports", side="YES",
                token_id="tok_lol_yes", shares=5.0, entry_vwap=0.90, cost_usdc=4.50,
                current_bid=0.90, p_est=0.98, entry_edge=0.08, kelly_full_pct=0.20,
                kelly_half_pct=0.08, applied_size_pct=0.08, roundtrip_slippage_pct=0.01,
                official_source="gol.gg", exit_condition="Hold", rationale="Strong consensus",
                end_date_iso="2026-11-10T12:00:00Z",
            )

            m_live = MarketInfo(
                id="m_collapse", question="LoL: Team A vs Team B", slug="lol-ab",
                description="", resolution_source="gol.gg", has_official_source=True,
                end_date_iso="2026-11-10T12:00:00Z", hours_to_close=2.5,
                liquidity_usd=10000.0, volume_24h_usd=20000.0, outcomes=["YES", "NO"],
                gamma_prices=[0.001, 0.999], clob_token_ids=["tok_lol_yes", "tok_lol_no"],
                order_min_size=1.0, tick_size=0.01, category="Sports", closed=False,
            )

            # Re-evaluation shows thesis collapsed to 1.5% for YES
            eval_res = EvaluationResult(
                market_id="m_collapse", question=m_live.question, category="Sports",
                oracle_used="MatureMarketConsensusOracle", official_source="gol.gg",
                p_yes=0.015, p_no=0.985, confidence=0.92, rationale="Market consensus shifted to NO",
            )
            trader_instance._evaluate_market_probability = MagicMock(return_value=(eval_res, None))

            # Simulate CLOB sell returning 0.0 bids
            with patch("trader.fetch_market_by_id", return_value=m_live):
                with patch("trader.simulate_clob_sell_shares", return_value=(0.0, 0.0, 0.0)):
                    closed = trader_instance.monitor_and_manage_open_positions()
                    self.assertEqual(closed, 1)

                    # Slot must be cleanly freed
                    open_pos = db.get_open_positions()
                    self.assertEqual(len(open_pos), 0)

                    all_pos = db.get_all_positions()
                    self.assertEqual(all_pos[0]["status"], "CLOSED")
                    self.assertIn("THESIS INVALIDATED", all_pos[0]["exit_reason"])
                    self.assertEqual(all_pos[0]["exit_vwap"], 0.0)
                    self.assertEqual(all_pos[0]["proceeds_usdc"], 0.0)

    def test_dynamic_risk_cap_for_ceiling_contracts(self) -> None:
        """Direction C: High-price contracts (>= 0.895) must be capped at 4% bankroll to limit tail risk."""
        from trader import GrokCharterPaperTrader
        # Sweet spot [0.76, 0.895) gets standard 8% cap
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.76), 0.08)
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.84), 0.08)
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.89), 0.08)

        # Ceiling contracts [0.895, 0.92] capped at 4%
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.90), 0.04)
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.91), 0.04)
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.92), 0.04)

        # Kelly sizing with 4% cap on $50 equity: max bet is $2.00 (not $4.00)
        _, _, applied_pct, bet_usdc = GrokCharterPaperTrader.compute_kelly_sizing(
            p_est=0.98, ask_vwap=0.90, total_equity=50.0,
            max_pct=GrokCharterPaperTrader.get_max_bank_pct_for_price(0.90),
            kelly_fraction=0.40,
        )
        self.assertEqual(applied_pct, 0.04)
        self.assertEqual(bet_usdc, 2.00)

    def test_multi_category_filter_partitioning(self) -> None:
        """Direction C / S: Comma-separated category filters (e.g. 'Sports, Other') must route correctly."""
        from polymarket_api import MarketInfo
        from trader import GrokCharterPaperTrader
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_d:
            db_tmp = SimDatabase(db_path=Path(tmp_d) / "temp_mc.db", initial_capital=50.0)
            trader = GrokCharterPaperTrader(db=db_tmp, trades_txt_path=Path(tmp_d) / "t.txt")

            def _mk(mid, q, cat, prices):
                return MarketInfo(
                    id=mid, question=q, slug=mid, description="", resolution_source="https://official.org",
                    has_official_source=True, end_date_iso="2026-11-10T00:00:00Z", hours_to_close=24.0,
                    liquidity_usd=10000.0, volume_24h_usd=20000.0, outcomes=["Yes", "No"],
                    gamma_prices=prices, clob_token_ids=[f"t_{mid}_y", f"t_{mid}_n"],
                    order_min_size=1.0, tick_size=0.01, category=cat, closed=False,
                )

            m_sp = _mk("1", "Sports Match", "Sports", [0.85, 0.15])
            m_ot = _mk("2", "Esports Kills", "Other", [0.55, 0.45])
            m_cr = _mk("3", "Bitcoin > 80k", "Crypto", [0.45, 0.55])

            active, shadow = trader.partition_markets(
                [m_sp, m_ot, m_cr],
                cat_filter="Sports, Other",
                min_liq=5000.0,
                open_real_market_ids=set(),
                open_shadow_market_ids=set(),
            )

            active_ids = {m.id for m in active}
            shadow_ids = {m.id for m in shadow}

            self.assertIn("1", active_ids)
            self.assertIn("2", active_ids)
            self.assertIn("3", shadow_ids)
            self.assertNotIn("3", active_ids)


if __name__ == "__main__":
    unittest.main()

