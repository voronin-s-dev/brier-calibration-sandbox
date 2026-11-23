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
ORIGINAL_SEND_TELEGRAM_ALERT = telegram_notify.send_telegram_alert
telegram_notify.send_telegram_alert = lambda *args, **kwargs: False
auto_governor.send_telegram_alert = lambda *args, **kwargs: False
trader.send_telegram_alert = lambda *args, **kwargs: False


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
        self.assertEqual(GrokCharterPaperTrader.MIN_HOURS_TO_CLOSE, 2.0)
        self.assertEqual(GrokCharterPaperTrader.EXIT_HOURS_THRESHOLD, 0.0)
        self.assertEqual(GrokCharterPaperTrader.STOP_LOSS_PCT, 0.40)
        self.assertEqual(GrokCharterPaperTrader.MIN_EDGE_PP, 0.025)
        self.assertEqual(GrokCharterPaperTrader.MIN_NET_EDGE_PP, 0.015)
        self.assertEqual(GrokCharterPaperTrader.MIN_ESTIMATED_PROB, 0.70)
        self.assertEqual(GrokCharterPaperTrader.MIN_CONTRACT_PRICE, 0.70)
        self.assertEqual(GrokCharterPaperTrader.MAX_CONTRACT_PRICE, 0.92)
        self.assertEqual(GrokCharterPaperTrader.PROB_SHIFT_EXIT_PP, 0.12)
        self.assertEqual(GrokCharterPaperTrader.MAX_BANK_PCT_PER_TRADE, 0.08)

    def test_social_mention_count_guard(self) -> None:
        """Verify high-variance social post/tweet count markets (Elon Musk tweets, Truth Social) are blocked."""
        self.assertTrue(GrokCharterPaperTrader.is_social_mention_count_trap("Will Elon Musk post 65-89 tweets from November 16 to November 18, 2026?"))
        self.assertTrue(GrokCharterPaperTrader.is_social_mention_count_trap("Will Elon Musk post 220-239 tweets this week?"))
        self.assertTrue(GrokCharterPaperTrader.is_social_mention_count_trap("Will Donald Trump post 30-39 Truth Social posts?"))
        self.assertFalse(GrokCharterPaperTrader.is_social_mention_count_trap("Fourth Jensen Huang affair reported by November 20?"))
        self.assertFalse(GrokCharterPaperTrader.is_social_mention_count_trap("Will Argentina win on 2026-11-17?"))
        self.assertFalse(GrokCharterPaperTrader.is_social_mention_count_trap("Spurs vs. Jazz"))

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
        """Direction M & U: Active non-Sports main position under 1.0h to close must trigger TIME EXIT."""
        from unittest.mock import MagicMock, patch
        from database import SimDatabase
        from polymarket_api import MarketInfo
        import tempfile
        from trader import GrokCharterPaperTrader

        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            db = SimDatabase(db_path=Path(tmp) / "test.db", initial_capital=50.0)
            trader_instance = GrokCharterPaperTrader(db=db, trades_txt_path=Path(tmp) / "trades.txt")

            db.open_position(
                market_id="m_time_1", question="Will BTC be above $66,000?", category="Crypto", side="NO",
                token_id="tok_no_1", shares=10.0, entry_vwap=0.82, cost_usdc=8.20,
                current_bid=0.82, p_est=0.88, entry_edge=0.06, kelly_full_pct=0.20,
                kelly_half_pct=0.08, applied_size_pct=0.08, roundtrip_slippage_pct=0.01,
                official_source="Kraken", exit_condition="Hold", rationale="Terminal GBM",
                end_date_iso="2026-11-10T12:00:00Z",
            )

            m_live = MarketInfo(
                id="m_time_1", question="Will BTC be above $66,000?", slug="btc-66k",
                description="", resolution_source="Kraken", has_official_source=True,
                end_date_iso="2026-11-10T12:00:00Z", hours_to_close=0.6,
                liquidity_usd=10000.0, volume_24h_usd=20000.0, outcomes=["YES", "NO"],
                gamma_prices=[0.14, 0.86], clob_token_ids=["tok_yes_1", "tok_no_1"],
                order_min_size=1.0, tick_size=0.01, category="Crypto", closed=False,
            )

            with patch("trader.fetch_market_by_id", return_value=m_live):
                with patch("trader.simulate_clob_sell_shares", return_value=(0.86, 8.60, 0.86)):
                    closed = trader_instance.monitor_and_manage_open_positions()
                    self.assertEqual(closed, 1)

                    open_pos = db.get_open_positions()
                    self.assertEqual(len(open_pos), 0)

                    all_pos = db.get_all_positions()
                    self.assertEqual(all_pos[0]["status"], "CLOSED")
                    self.assertIn("TIME EXIT", all_pos[0]["exit_reason"])

    def test_sports_skips_pre_match_time_exit(self) -> None:
        """Verify Sports positions do NOT trigger TIME EXIT before kickoff (endDate is game start, not resolution)."""
        from unittest.mock import patch
        from database import SimDatabase
        from polymarket_api import MarketInfo
        import tempfile
        from trader import GrokCharterPaperTrader

        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            db = SimDatabase(db_path=Path(tmp) / "test_sp.db", initial_capital=50.0)
            trader_instance = GrokCharterPaperTrader(db=db, trades_txt_path=Path(tmp) / "trades.txt")

            db.open_position(
                market_id="m_sp_1", question="Spurs vs. Jazz", category="Sports", side="YES",
                token_id="tok_sp_1", shares=10.0, entry_vwap=0.84, cost_usdc=8.40,
                current_bid=0.83, p_est=0.90, entry_edge=0.06, kelly_full_pct=0.20,
                kelly_half_pct=0.08, applied_size_pct=0.04, roundtrip_slippage_pct=0.01,
                official_source="NBA.com", exit_condition="Hold", rationale="Consensus",
                end_date_iso="2026-11-17T22:00:00Z",
            )

            m_live = MarketInfo(
                id="m_sp_1", question="Spurs vs. Jazz", slug="spurs-jazz",
                description="", resolution_source="NBA.com", has_official_source=True,
                end_date_iso="2026-11-17T22:00:00Z", hours_to_close=0.5,
                liquidity_usd=10000.0, volume_24h_usd=20000.0, outcomes=["YES", "NO"],
                gamma_prices=[0.84, 0.16], clob_token_ids=["tok_sp_1", "tok_no_1"],
                order_min_size=1.0, tick_size=0.01, category="Sports", closed=False,
            )

            with patch("trader.fetch_market_by_id", return_value=m_live), \
                 patch("trader.simulate_clob_sell_shares", return_value=(0.83, 8.30, 0.83)):
                closed = trader_instance.monitor_and_manage_open_positions()

            self.assertEqual(closed, 0)
            self.assertEqual(len(db.get_open_positions()), 1)

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
        """Direction C: Tiered risk cap to protect against asymmetric upsets on expensive contracts."""
        from trader import GrokCharterPaperTrader
        # Value sweet spot [0.60, 0.80) gets standard 8% cap
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.60), 0.08)
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.70), 0.08)
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.76), 0.08)
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.79), 0.08)

        # High-price contracts [0.80, 0.88) capped at 4%
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.80), 0.04)
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.84), 0.04)
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.87), 0.04)

        # Extreme ceiling contracts (>= 0.88) strictly capped at 3%
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.88), 0.03)
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.90), 0.03)
        self.assertEqual(GrokCharterPaperTrader.get_max_bank_pct_for_price(0.92), 0.03)

        # Kelly sizing with 3% cap on $50 equity: max bet is $1.50 (not $4.00)
        _, _, applied_pct, bet_usdc = GrokCharterPaperTrader.compute_kelly_sizing(
            p_est=0.98, ask_vwap=0.90, total_equity=50.0,
            max_pct=GrokCharterPaperTrader.get_max_bank_pct_for_price(0.90),
            kelly_fraction=0.40,
        )
        self.assertEqual(applied_pct, 0.03)
        self.assertEqual(bet_usdc, 1.50)

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

    def test_telegram_alert_deduplication_suppresses_rapid_duplicates(self):
        """
        Direction N (Notification & CLI Idempotency):
        Verifies that send_telegram_alert suppresses identical duplicate text messages
        within the deduplication window.
        """
        import telegram_notify
        import tempfile
        from unittest.mock import patch, MagicMock

        with tempfile.TemporaryDirectory() as tmpdir:
            test_cache = Path(tmpdir) / "notified_alerts_cache.json"
            
            with patch.dict("os.environ", {"TELEGRAM_BOT_TOKEN": "mock_token", "ALLOWED_CHAT_ID": "123", "TESTING": "0"}):
                with patch("telegram_notify.urllib.request.urlopen") as mock_url:
                    mock_resp = MagicMock()
                    mock_resp.status = 200
                    mock_url.return_value.__enter__.return_value = mock_resp

                    msg = "⚙️ ОДОБРЕНА ДОРАБОТКА #999"
                    # First send succeeds and hits HTTP API
                    first_res = telegram_notify._raw_send_telegram_alert(
                        msg, dedup=True, dedup_window_sec=3600, cache_file_override=test_cache
                    )
                    self.assertTrue(first_res)
                    self.assertEqual(mock_url.call_count, 1)

                    # Second identical send is suppressed without making HTTP API call
                    second_res = telegram_notify._raw_send_telegram_alert(
                        msg, dedup=True, dedup_window_sec=3600, cache_file_override=test_cache
                    )
                    self.assertTrue(second_res)
                    self.assertEqual(mock_url.call_count, 1)

    def test_run_sim_help_does_not_crash(self):
        """
        Direction O (CLI Stability):
        Verifies that run_sim.py argument parser expands help strings without
        raising ValueError: unsupported format character '%'.
        """
        import subprocess
        import sys
        res = subprocess.run(
            [sys.executable, "run_sim.py", "--help"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).resolve().parent,
        )
        self.assertEqual(res.returncode, 0)
        self.assertIn("Polymarket Autonomous Paper-Trading Simulator", res.stdout)
        self.assertIn("--reset-halt", res.stdout)

    def test_weather_oracle_date_parsing_with_year_and_rollover(self):
        """
        Direction P (Oracles Hardening):
        Verifies that WeatherOracle correctly parses explicit 4-digit years
        and rolls over to next year when month difference exceeds 6 months.
        """
        from oracles import WeatherOracle
        from polymarket_api import MarketInfo

        oracle = WeatherOracle()
        # Mock weather forecasts cache to avoid network calls
        oracle._cache["chicago"] = {
            "2027-01-05": 30.0,
        }

        # Market with explicit year 2027
        m_explicit = MarketInfo(
            id="m_weath_1",
            question="Will the highest temperature in Chicago be 20°F or lower on January 5, 2027?",
            slug="chicago-weather-jan-2027",
            description="",
            resolution_source="NOAA KORD",
            has_official_source=True,
            end_date_iso="2027-01-05T23:59:59Z",
            hours_to_close=24.0,
            liquidity_usd=10000.0,
            volume_24h_usd=20000.0,
            outcomes=["Yes", "No"],
            gamma_prices=[0.5, 0.5],
            clob_token_ids=["tok1", "tok2"],
            order_min_size=1.0,
            tick_size=0.01,
            category="Weather",
        )
        res = oracle.evaluate(m_explicit)
        self.assertIsNotNone(res)
        self.assertEqual(res.supporting_data["target_date"], "2027-01-05")

        # Market with rollover (no year specified, but in Nov/Dec target is Jan)
        m_rollover = MarketInfo(
            id="m_weath_2",
            question="Will the highest temperature in Chicago be 20°F or lower on January 5?",
            slug="chicago-weather-jan-rollover",
            description="",
            resolution_source="NOAA KORD",
            has_official_source=True,
            end_date_iso="2027-01-05T23:59:59Z",
            hours_to_close=24.0,
            liquidity_usd=10000.0,
            volume_24h_usd=20000.0,
            outcomes=["Yes", "No"],
            gamma_prices=[0.5, 0.5],
            clob_token_ids=["tok1", "tok2"],
            order_min_size=1.0,
            tick_size=0.01,
            category="Weather",
        )
        res_roll = oracle.evaluate(m_rollover)
        self.assertIsNotNone(res_roll)
        self.assertEqual(res_roll.supporting_data["target_date"], "2027-01-05")

    def test_notify_position_closed_resolved_loss_explanation(self):
        """
        Direction Q (Notification Precision):
        Verifies that when a position settles at $0.00 (loss), the notification
        accurately explains the loss instead of claiming a 100% win.
        """
        import telegram_notify
        import tempfile
        from unittest.mock import patch

        with tempfile.TemporaryDirectory() as tmpdir:
            test_state = Path(tmpdir) / "notified_exits.json"
            captured_messages = []
            with patch("telegram_notify.send_telegram_alert") as mock_alert:
                mock_alert.side_effect = lambda text, *args, **kwargs: (captured_messages.append(text), True)[1]
                pos = {
                    "id": 99999,
                    "question": "Will BTC reach $100k?",
                    "side": "YES",
                    "cost_usdc": 3.00,
                }
                res = telegram_notify.notify_position_closed(
                    pos=pos,
                    pnl=-3.00,
                    exit_vwap=0.0,
                    exit_reason="MARKET RESOLVED on Polymarket: YES settled at $0.00/share",
                    total_equity=35.00,
                    state_file_override=test_state,
                )
                self.assertTrue(res)
                self.assertEqual(len(captured_messages), 1)
                msg = captured_messages[0]
                self.assertIn("Защитный выход: -3.00$", msg)
                self.assertIn("исходом против нас", msg)
                self.assertNotIn("победой", msg)

    def test_daily_digest_blocks_midnight_early_trigger(self):
        """
        Direction N (Notification & CLI Idempotency):
        Verifies that check_and_send_daily_digest blocks early midnight triggers (< 07:00 UTC)
        and only sends at or after the target morning hour.
        """
        from datetime import datetime, timezone
        import telegram_notify
        from unittest.mock import MagicMock, patch

        mock_db = MagicMock()
        mock_db.recalculate_portfolio.return_value = {
            "total_equity": 38.0,
            "cash_usdc": 35.0,
            "locked_usdc": 3.0,
        }

        # 1. At 00:05 UTC (02:05 local time), digest must be blocked
        early_dt = datetime(2026, 11, 11, 0, 5, 0, tzinfo=timezone.utc)
        with patch("telegram_notify.datetime") as mock_dt:
            mock_dt.now.return_value = early_dt
            mock_dt.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)
            res = telegram_notify.check_and_send_daily_digest(mock_db, force=False, target_hour_utc=7)
            self.assertFalse(res)

        # 2. At 07:15 UTC (09:15 local time), target hour has arrived
        morning_dt = datetime(2026, 11, 11, 7, 15, 0, tzinfo=timezone.utc)
        with patch("telegram_notify.datetime") as mock_dt:
            mock_dt.now.return_value = morning_dt
            mock_dt.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)
            with patch("telegram_notify.send_telegram_alert", return_value=True):
                with patch("telegram_notify.Path.exists", return_value=False):
                    res = telegram_notify.check_and_send_daily_digest(mock_db, force=False, target_hour_utc=7)
                    self.assertTrue(res)

    def test_esports_probability_discounting(self) -> None:
        """Verify that esports high-consensus favorites are capped at 84% to account for upset risk."""
        from oracles import HighConvictionFactOracle, is_esports_market
        from polymarket_api import MarketInfo

        oracle = HighConvictionFactOracle()

        # Esports market (Counter-Strike)
        m_esports = MarketInfo(
            id="m_cs",
            question="Counter-Strike: MOUZ vs G2 (BO3) - BLAST Rivals",
            slug="m-cs",
            description="",
            resolution_source="https://hltv.org",
            has_official_source=True,
            end_date_iso="2026-11-12T00:00:00Z",
            hours_to_close=10.0,
            liquidity_usd=12000.0,
            volume_24h_usd=25000.0,
            outcomes=["Yes", "No"],
            gamma_prices=[0.92, 0.08],
            clob_token_ids=["tok_yes", "tok_no"],
            order_min_size=1.0,
            tick_size=0.01,
            category="Sports",
            closed=False,
        )
        self.assertTrue(is_esports_market(m_esports))
        res_esports = oracle.evaluate(m_esports)
        self.assertIsNotNone(res_esports)
        self.assertEqual(res_esports.p_yes, 0.84)
        self.assertEqual(res_esports.oracle_used, "EsportsDiscountedConsensusOracle")

        # Non-esports mature market (e.g. general Sports or Geopolitics)
        m_general = MarketInfo(
            id="m_gen",
            question="Will Team USA win the International Match?",
            slug="m-gen",
            description="",
            resolution_source="Official Scoreboard",
            has_official_source=True,
            end_date_iso="2026-11-12T00:00:00Z",
            hours_to_close=10.0,
            liquidity_usd=12000.0,
            volume_24h_usd=25000.0,
            outcomes=["Yes", "No"],
            gamma_prices=[0.92, 0.08],
            clob_token_ids=["tok_yes", "tok_no"],
            order_min_size=1.0,
            tick_size=0.01,
            category="Sports",
            closed=False,
        )
        self.assertFalse(is_esports_market(m_general))
        res_general = oracle.evaluate(m_general)
        self.assertIsNotNone(res_general)
        self.assertEqual(res_general.p_yes, 0.955)
        self.assertEqual(res_general.oracle_used, "MatureMarketConsensusOracle")

    def test_value_sweet_spot_selection_priority(self) -> None:
        """Verify that markets in the 70-80 cent value sweet spot are prioritized ahead of 80-87 cent favorites."""
        from unittest.mock import MagicMock
        from polymarket_api import MarketInfo
        from trader import GrokCharterPaperTrader

        m_value = MarketInfo(
            id="m_val", question="Match A", slug="m-val", description="",
            resolution_source="https://official.org", has_official_source=True,
            end_date_iso="2026-11-12T00:00:00Z", hours_to_close=10.0,
            liquidity_usd=10000.0, volume_24h_usd=50000.0, outcomes=["Yes", "No"],
            gamma_prices=[0.74, 0.26], clob_token_ids=["t1", "t2"],
            order_min_size=1.0, tick_size=0.01, category="Sports", closed=False,
        )
        m_favorite = MarketInfo(
            id="m_fav", question="Match B", slug="m-fav", description="",
            resolution_source="https://official.org", has_official_source=True,
            end_date_iso="2026-11-12T00:00:00Z", hours_to_close=10.0,
            liquidity_usd=20000.0, volume_24h_usd=100000.0, outcomes=["Yes", "No"],
            gamma_prices=[0.84, 0.16], clob_token_ids=["t3", "t4"],
            order_min_size=1.0, tick_size=0.01, category="Sports", closed=False,
        )

        trader = GrokCharterPaperTrader(db=MagicMock())
        candidates, _ = trader.partition_markets(
            all_markets=[m_favorite, m_value],
            open_real_market_ids=set(),
            open_shadow_market_ids=set(),
            cat_filter="ALL",
            min_liq=5000.0,
        )
        # Value market [0.70, 0.80) MUST be sorted first despite having lower volume than [0.80, 0.87]
        self.assertEqual(candidates[0].id, "m_val")
        self.assertEqual(candidates[1].id, "m_fav")

    def test_extract_event_key_bracket_and_mention_deduplication(self) -> None:
        """Verify that multi-strike brackets and social mentions share the same canonical event key."""
        # 1. Social mentions with numeric tweet/post count brackets
        k1 = extract_event_key("Will Elon Musk post 280-299 tweets from November 6 to November 13, 2026?", "Geopolitics")
        k2 = extract_event_key("Will Elon Musk post 220-239 tweets from November 6 to November 13, 2026?", "Geopolitics")
        k3 = extract_event_key("Will Elon Musk post 200-219 tweets from November 6 to November 13, 2026?", "Geopolitics")
        self.assertEqual(k1, k2)
        self.assertEqual(k2, k3)
        self.assertIn("mentions:elon_musk", k1)

        # 2. General multi-strike bracket questions across dates
        b1 = extract_event_key("Will inflation rate be between 2.5-2.7% in November 2026?", "Macro")
        b2 = extract_event_key("Will inflation rate be between 2.8-3.0% in November 2026?", "Macro")
        self.assertEqual(b1, b2)

    def test_esports_excluded_from_clob_orderbook_oracle(self) -> None:
        """Verify that esports markets categorized as 'Other' are excluded from CLOB book imbalance trading."""
        from oracles import NewsAndOrderbookOracle
        from polymarket_api import MarketInfo

        oracle = NewsAndOrderbookOracle()
        m_esports = MarketInfo(
            id="m_blast",
            question="Will Vitality Win the BLAST Rivals Hong Kong 2026?",
            slug="vitality-blast",
            description="",
            resolution_source="https://www.hltv.org/events/8251/blast-rivals-2026-season-2",
            has_official_source=True,
            end_date_iso="2026-11-17T00:00:00Z",
            hours_to_close=96.0,
            liquidity_usd=15000.0,
            volume_24h_usd=25000.0,
            outcomes=["Yes", "No"],
            gamma_prices=[0.26, 0.74],
            clob_token_ids=["tok_yes", "tok_no"],
            order_min_size=1.0,
            tick_size=0.01,
            category="Other",
            closed=False,
        )
        bids = [(0.25, 500.0), (0.24, 600.0)]
        asks = [(0.27, 2000.0), (0.28, 3000.0)]
        # Orderbook oracle must strictly return None for esports
        res = oracle.evaluate_with_orderbook(m_esports, bids, asks)
        self.assertIsNone(res)

    def test_orderbook_oracle_damps_unconfirmed_obi(self) -> None:
        """Verify that shallow depth (<$1500) returns None, and unconfirmed OBI without news is damped."""
        from oracles import NewsAndOrderbookOracle
        from polymarket_api import MarketInfo

        oracle = NewsAndOrderbookOracle()
        m_general = MarketInfo(
            id="m_macro",
            question="Will President sign Bill X in November 2026?",
            slug="bill-x",
            description="",
            resolution_source="https://whitehouse.gov",
            has_official_source=True,
            end_date_iso="2026-11-20T00:00:00Z",
            hours_to_close=120.0,
            liquidity_usd=20000.0,
            volume_24h_usd=30000.0,
            outcomes=["Yes", "No"],
            gamma_prices=[0.50, 0.50],
            clob_token_ids=["tok_yes", "tok_no"],
            order_min_size=1.0,
            tick_size=0.01,
            category="Macro",
            closed=False,
        )
        # Shallow book: near depth = $100 + $500 = $600 < $1500 threshold
        shallow_bids = [(0.49, 200.0)]
        shallow_asks = [(0.51, 1000.0)]
        self.assertIsNone(oracle.evaluate_with_orderbook(m_general, shallow_bids, shallow_asks))

    def test_sweet_spot_early_take_profit(self) -> None:
        """Verify that sweet spot trades [0.60, 0.80) can lock in +25% gains early when Bid >= 0.88."""
        import tempfile
        from unittest.mock import patch
        from database import SimDatabase
        from trader import GrokCharterPaperTrader

        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db_path = Path(tmp_dir) / "test_tp.db"
            trades_path = Path(tmp_dir) / "trades.txt"
            db = SimDatabase(db_path=db_path, initial_capital=50.0)
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=trades_path)

            # 1. Sweet spot position entered at 0.66, now Bid reaches 0.88 (+33.3% gain)
            pos_id = db.open_position(
                market_id="m_sweet", question="Sweet Spot Market", category="Crypto", side="YES",
                token_id="tok_sweet", shares=10.0, entry_vwap=0.66, cost_usdc=6.60, current_bid=0.66,
                p_est=0.72, entry_edge=0.06, kelly_full_pct=0.15, kelly_half_pct=0.06,
                applied_size_pct=0.06, roundtrip_slippage_pct=0.01, official_source="Binance",
                exit_condition="TP", rationale="Test", end_date_iso="2026-11-20T00:00:00Z"
            )

            # Mock CLOB sell: returns 0.88 VWAP ($8.80 proceeds)
            with patch("trader.fetch_market_by_id", return_value=None), \
                 patch("trader.simulate_clob_sell_shares", return_value=(0.88, 8.80, 0.88)):
                closed_count = trader.monitor_and_manage_open_positions()

            self.assertEqual(closed_count, 1)
            pos = db.get_all_positions()[0]
            self.assertEqual(pos["status"], "CLOSED")
            self.assertIn("TAKE PROFIT (Sweet Spot +25% Lock)", pos["exit_reason"])
            self.assertAlmostEqual(float(pos["realized_pnl"]), 2.20, places=2)

    def test_standard_twelve_percent_take_profit(self) -> None:
        """Verify that live trades lock in +12% net return early even below sweet spot 0.88 bid threshold."""
        import tempfile
        from unittest.mock import patch
        from database import SimDatabase
        from trader import GrokCharterPaperTrader

        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db_path = Path(tmp_dir) / "test_tp12.db"
            trades_path = Path(tmp_dir) / "trades.txt"
            db = SimDatabase(db_path=db_path, initial_capital=50.0)
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=trades_path)

            # Open position at 0.70
            db.open_position(
                market_id="m_tp12", question="BTC Dip Market", category="Crypto", side="NO",
                token_id="tok_tp12", shares=10.0, entry_vwap=0.70, cost_usdc=7.00, current_bid=0.70,
                p_est=0.78, entry_edge=0.08, kelly_full_pct=0.15, kelly_half_pct=0.06,
                applied_size_pct=0.06, roundtrip_slippage_pct=0.01, official_source="Binance",
                exit_condition="TP", rationale="Test", end_date_iso="2026-11-20T00:00:00Z"
            )

            # Mock CLOB sell: returns 0.79 VWAP ($7.90 proceeds, +12.8% return)
            with patch("trader.fetch_market_by_id", return_value=None), \
                 patch("trader.simulate_clob_sell_shares", return_value=(0.79, 7.90, 0.79)):
                closed_count = trader.monitor_and_manage_open_positions()

            self.assertEqual(closed_count, 1)
            pos = db.get_all_positions()[0]
            self.assertEqual(pos["status"], "CLOSED")
            self.assertIn("TAKE-PROFIT TRIGGERED: Net return", pos["exit_reason"])
            self.assertAlmostEqual(float(pos["realized_pnl"]), 0.90, places=2)

    def test_prob_shift_noise_protection_when_price_above_entry(self) -> None:
        """Verify THESIS INVALIDATED never dumps +EV holds (latest_p >= Bid) or positions at/above entry."""
        import tempfile
        from unittest.mock import patch
        from database import SimDatabase
        from trader import GrokCharterPaperTrader

        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db_path = Path(tmp_dir) / "test_ps_noise.db"
            trades_path = Path(tmp_dir) / "trades.txt"
            db = SimDatabase(db_path=db_path, initial_capital=50.0)
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=trades_path)

            # Open at 0.70, initial_p=0.82
            db.open_position(
                market_id="m_noise", question="ETH Market", category="Crypto", side="YES",
                token_id="tok_noise", shares=10.0, entry_vwap=0.70, cost_usdc=7.00, current_bid=0.71,
                p_est=0.82, entry_edge=0.12, kelly_full_pct=0.20, kelly_half_pct=0.08,
                applied_size_pct=0.08, roundtrip_slippage_pct=0.01, official_source="Kraken",
                exit_condition="Hold", rationale="Test", end_date_iso="2026-11-20T00:00:00Z"
            )

            from polymarket_api import MarketInfo
            m_live = MarketInfo(
                id="m_noise", question="ETH Market", slug="eth-market", description="",
                resolution_source="Kraken", has_official_source=True, end_date_iso="2026-11-20T00:00:00Z",
                hours_to_close=10.0, liquidity_usd=10000.0, volume_24h_usd=20000.0, outcomes=["YES", "NO"],
                gamma_prices=[0.71, 0.29], clob_token_ids=["tok_noise", "tok_no"], order_min_size=1.0,
                tick_size=0.01, category="Crypto", closed=False
            )
            from oracles import EvaluationResult
            mock_eval_pos_ev = EvaluationResult(
                market_id="m_noise", question="ETH Market", category="Crypto", oracle_used="Kraken",
                official_source="Kraken", p_yes=0.68, p_no=0.32, confidence=0.8, rationale="Shift"
            )

            # Case A: Model dropped to 0.68 (-14 pp), Bid is 0.71 (>= entry 0.70). Must NOT exit!
            with patch("trader.fetch_market_by_id", return_value=m_live), \
                 patch.object(trader, "_evaluate_market_probability", return_value=(mock_eval_pos_ev, None)), \
                 patch("trader.simulate_clob_sell_shares", return_value=(0.71, 7.10, 0.71)):
                closed = trader.monitor_and_manage_open_positions()
            self.assertEqual(closed, 0)

            # Case B: Bid dropped to 0.66 (< entry 0.70), BUT model is 0.68 > 0.66 (+EV to hold!). Must NOT dump!
            with patch("trader.fetch_market_by_id", return_value=m_live), \
                 patch.object(trader, "_evaluate_market_probability", return_value=(mock_eval_pos_ev, None)), \
                 patch("trader.simulate_clob_sell_shares", return_value=(0.66, 6.60, 0.66)):
                closed = trader.monitor_and_manage_open_positions()
            self.assertEqual(closed, 0)
            self.assertEqual(len(db.get_open_positions()), 1)

            # Case C: Model collapses to 0.58 (< Bid 0.66 -> holding is now -EV!). THESIS INVALIDATED triggers!
            mock_eval_neg_ev = EvaluationResult(
                market_id="m_noise", question="ETH Market", category="Crypto", oracle_used="Kraken",
                official_source="Kraken", p_yes=0.58, p_no=0.42, confidence=0.8, rationale="Broken thesis"
            )
            with patch("trader.fetch_market_by_id", return_value=m_live), \
                 patch.object(trader, "_evaluate_market_probability", return_value=(mock_eval_neg_ev, None)), \
                 patch("trader.simulate_clob_sell_shares", return_value=(0.66, 6.60, 0.66)):
                closed = trader.monitor_and_manage_open_positions()

            self.assertEqual(closed, 1)
            pos = db.get_all_positions()[0]
            self.assertEqual(pos["status"], "CLOSED")
            self.assertIn("THESIS INVALIDATED", pos["exit_reason"])

    def test_net_edge_rejects_slippage_eaten_entries(self) -> None:
        """Verify entries where (gross_edge - slippage) < MIN_NET_EDGE_PP (1.5pp) are rejected."""
        import tempfile
        from unittest.mock import patch
        from polymarket_api import MarketInfo, OrderBookSimulation
        from oracles import EvaluationResult

        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db = SimDatabase(db_path=Path(tmp_dir) / "test_ne.db", initial_capital=50.0)
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=Path(tmp_dir) / "trades.txt")

            mkt = MarketInfo(
                id="mkt_ne_1", question="Will ETH be above $1,800 on November 20?", slug="eth-1800",
                description="", resolution_source="Kraken", has_official_source=True,
                end_date_iso="2026-11-20T17:00:00Z", hours_to_close=20.0,
                liquidity_usd=20000.0, volume_24h_usd=50000.0, outcomes=["YES", "NO"],
                gamma_prices=[0.78, 0.22], clob_token_ids=["t_yes", "t_no"],
                order_min_size=1.0, tick_size=0.01, category="Crypto", closed=False,
            )
            # Gross edge = 0.822 - 0.780 = +4.2pp (>= 2.5pp), BUT slippage = 2.9% -> Net edge = +1.3pp (< 1.5pp)!
            ev = EvaluationResult(
                market_id="mkt_ne_1", question=mkt.question, category="Crypto", oracle_used="Kraken",
                official_source="Kraken", p_yes=0.822, p_no=0.178, confidence=0.82, rationale="GBM"
            )
            ob_sim = OrderBookSimulation(
                token_id="t_yes", side_label="YES", best_bid=0.751, best_ask=0.780,
                midpoint=0.765, spread_pct=0.029, bet_usdc=2.0, shares_filled=2.56,
                vwap_buy_price=0.780, vwap_sell_price=0.751, entry_slippage_pct=0.0145,
                exit_slippage_pct=0.0145, roundtrip_slippage_pct=0.029,
                sufficient_depth=True, passes_slippage_limit=True,
            )

            with patch("trader.fetch_active_markets", return_value=[mkt]), \
                 patch.object(trader, "_evaluate_market_probability", return_value=(ev, None)), \
                 patch("trader.simulate_clob_buy_and_exit_check", return_value=ob_sim), \
                 patch.object(trader, "monitor_and_manage_open_positions", return_value=0), \
                 patch.object(trader, "monitor_and_manage_shadow_positions", return_value=0):
                res = trader.run_cycle(max_markets_to_scan=10)

            self.assertEqual(res["trades_opened"], 0)
            cands = db.get_recent_candidates(limit=5)
            self.assertEqual(len(cands), 1)
            self.assertIn("REJECTED: Net EV edge", cands[0]["decision"])

    def test_first_passage_barrier_uses_135x_fat_tail_multiplier(self) -> None:
        """Verify First-Passage barrier model prices fat-tail touch probability conservatively (~14-15% vs old ~8%)."""
        from unittest.mock import patch
        from polymarket_api import MarketInfo
        from oracles import CryptoOracle

        oracle = CryptoOracle()
        mkt = MarketInfo(
            id="m_eth_reach", question="Will Ethereum reach $1,850 on November 17?", slug="eth-reach",
            description="", resolution_source="Binance", has_official_source=True,
            end_date_iso="2026-11-18T05:00:00Z", hours_to_close=11.8,
            liquidity_usd=20000.0, volume_24h_usd=50000.0, outcomes=["YES", "NO"],
            gamma_prices=[0.11, 0.89], clob_token_ids=["ty", "tn"],
            order_min_size=1.0, tick_size=0.01, category="Crypto", closed=False,
        )
        fake_stats = {
            "source": "Kraken", "current_price": 1773.05, "hourly_vol": 0.0063,
            "annual_vol": 0.59, "today_high": 1790.0, "today_low": 1750.0,
            "month_high": 2100.0, "month_low": 1650.0, "high_24h": 1790.0, "low_24h": 1750.0,
        }
        with patch.object(oracle, "_get_symbol_stats", return_value=fake_stats):
            res = oracle.evaluate(mkt)

        self.assertIsNotNone(res)
        # With 1.35x barrier vol, raw P(touch) ~ 14.6%, calibrated p_no must be < 0.89 (no false NO edge!)
        self.assertLess(res.p_no, 0.89)

    def test_recently_closed_market_cooldown_prevents_churn(self) -> None:
        """Verify get_recently_closed_market_ids blocks immediate re-entry into just-closed markets."""
        import tempfile
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db = SimDatabase(db_path=Path(tmp_dir) / "test_cd.db", initial_capital=50.0)
            pos_id = db.open_position(
                market_id="mkt_churn_1", question="Test Market", category="Crypto", side="YES",
                token_id="t1", shares=5.0, entry_vwap=0.75, cost_usdc=3.75, current_bid=0.75,
                p_est=0.82, entry_edge=0.07, kelly_full_pct=0.20, kelly_half_pct=0.08,
                applied_size_pct=0.08, roundtrip_slippage_pct=0.01, official_source="Kraken",
                exit_condition="Hold", rationale="Test", end_date_iso="2026-11-20T00:00:00Z"
            )
            db.close_position(pos_id=pos_id, status="CLOSED", exit_vwap=0.74, proceeds_usdc=3.70, exit_reason="TIME EXIT", latest_p_est=0.80)
            recent_ids = db.get_recently_closed_market_ids(hours=12.0)
            self.assertIn("mkt_churn_1", recent_ids)

    def test_partition_markets_rejects_sub_two_hour_expiry(self) -> None:
        """Verify that markets with hours_to_close < 2.0 (Charter Rule #1) are never admitted into active or shadow pipelines."""
        from polymarket_api import MarketInfo
        db = SimDatabase(db_path=Path(":memory:"), initial_capital=50.0)
        trader = GrokCharterPaperTrader(db=db)

        mkts = [
            MarketInfo(
                id=f"mkt_h_{h}", question=f"Market with {h}h left", slug=f"mkt-{h}",
                description="", resolution_source="https://official.org", has_official_source=True,
                end_date_iso="2026-11-13T00:00:00Z", hours_to_close=float(h),
                liquidity_usd=10000.0, volume_24h_usd=20000.0, outcomes=["YES", "NO"],
                gamma_prices=[0.70, 0.30], clob_token_ids=["tok_yes", "tok_no"],
                order_min_size=1.0, tick_size=0.01, category="Crypto", closed=False,
            )
            for h in [0.5, 0.8, 1.2, 1.9, 2.5, 5.0]
        ]

        active, shadow = trader.partition_markets(
            mkts, open_real_market_ids=set(), open_shadow_market_ids=set(), cat_filter="ALL", min_liq=5000.0
        )
        active_hours = [m.hours_to_close for m in active]
        self.assertEqual(active_hours, [2.5, 5.0])
        self.assertTrue(all(h >= 2.0 for h in active_hours))

    def test_time_exit_requires_positive_bid_vwap(self) -> None:
        """Verify that Time Exit (< 1.0h to expiry) does NOT dump non-Sports positions for $0.00 when CLOB bids are zero."""
        from unittest.mock import patch
        from polymarket_api import MarketInfo
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db = SimDatabase(db_path=Path(tmp_dir) / "test_te.db", initial_capital=50.0)
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=Path(tmp_dir) / "trades.txt")

            db.open_position(
                market_id="mkt_te_1", question="Will BTC be above $66,000?", category="Crypto", side="YES",
                token_id="tok_btc", shares=10.0, entry_vwap=0.82, cost_usdc=8.20, current_bid=0.82,
                p_est=0.88, entry_edge=0.06, kelly_full_pct=0.20, kelly_half_pct=0.08,
                applied_size_pct=0.08, roundtrip_slippage_pct=0.01, official_source="Kraken",
                exit_condition="Hold", rationale="GBM", end_date_iso="2026-11-12T15:00:00Z"
            )

            m_live = MarketInfo(
                id="mkt_te_1", question="Will BTC be above $66,000?", slug="btc-66k",
                description="", resolution_source="Kraken", has_official_source=True,
                end_date_iso="2026-11-12T15:00:00Z", hours_to_close=0.5,
                liquidity_usd=10000.0, volume_24h_usd=20000.0, outcomes=["YES", "NO"],
                gamma_prices=[0.83, 0.17], clob_token_ids=["tok_btc", "tok_no"],
                order_min_size=1.0, tick_size=0.01, category="Crypto", closed=False,
            )

            # Case A: Zero bids in CLOB -> Must NOT dump for $0.00! Position remains open waiting for settlement.
            with patch("trader.fetch_market_by_id", return_value=m_live), \
                 patch.object(trader, "_evaluate_market_probability", return_value=(None, None)), \
                 patch("trader.simulate_clob_sell_shares", return_value=(0.0, 0.0, 0.0)):
                closed = trader.monitor_and_manage_open_positions()

            self.assertEqual(closed, 0)
            open_pos = db.get_open_positions()
            self.assertEqual(len(open_pos), 1)

            # Case B: Positive bid in CLOB ($0.83) -> Time Exit triggers and executes safely at $0.83
            with patch("trader.fetch_market_by_id", return_value=m_live), \
                 patch.object(trader, "_evaluate_market_probability", return_value=(None, None)), \
                 patch("trader.simulate_clob_sell_shares", return_value=(0.83, 8.30, 0.83)):
                closed = trader.monitor_and_manage_open_positions()

            self.assertEqual(closed, 1)
            self.assertEqual(len(db.get_open_positions()), 0)
            closed_pos = db.get_all_positions()[0]
            self.assertEqual(closed_pos["status"], "CLOSED")
            self.assertIn("TIME EXIT", closed_pos["exit_reason"])
            self.assertAlmostEqual(float(closed_pos["realized_pnl"]), 0.10, places=2)

    def test_shadow_time_exit_requires_positive_bid_vwap(self) -> None:
        """Verify that shadow Time Exit also requires positive bid VWAP to prevent simulated $0 liquidations."""
        from unittest.mock import patch
        from polymarket_api import MarketInfo
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db = SimDatabase(db_path=Path(tmp_dir) / "test_ste.db", initial_capital=50.0)
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=Path(tmp_dir) / "trades.txt")

            db.open_shadow_position(
                market_id="mkt_ste_1", question="Shadow ETH > 4k", category="Crypto", side="YES",
                token_id="tok_seth", shares=5.0, entry_vwap=0.80, cost_usdc=4.00,
                initial_p_est=0.85, entry_edge=0.05, kelly_full_pct=0.15, kelly_half_pct=0.05,
                applied_size_pct=0.05, roundtrip_slippage_pct=0.01,
                official_source="Binance", exit_condition="Hold", rationale="Shadow test",
                end_date_iso="2026-11-12T15:00:00Z"
            )

            m_live = MarketInfo(
                id="mkt_ste_1", question="Shadow ETH > 4k", slug="shadow-eth",
                description="", resolution_source="Binance", has_official_source=True,
                end_date_iso="2026-11-12T15:00:00Z", hours_to_close=0.6,
                liquidity_usd=10000.0, volume_24h_usd=20000.0, outcomes=["YES", "NO"],
                gamma_prices=[0.80, 0.20], clob_token_ids=["tok_yes", "tok_no"],
                order_min_size=1.0, tick_size=0.01, category="Crypto", closed=False,
            )

            # Case A: Zero bid -> does not exit
            with patch("trader.fetch_market_by_id", return_value=m_live), \
                 patch("trader.simulate_clob_sell_shares", return_value=(0.0, 0.0, 0.0)):
                closed = trader.monitor_and_manage_shadow_positions()
            self.assertEqual(closed, 0)
            self.assertEqual(len(db.get_open_shadow_positions()), 1)

            # Case B: Real bid -> exits
            with patch("trader.fetch_market_by_id", return_value=m_live), \
                 patch("trader.simulate_clob_sell_shares", return_value=(0.85, 4.25, 0.85)):
                closed = trader.monitor_and_manage_shadow_positions()
            self.assertEqual(closed, 1)
            self.assertEqual(len(db.get_open_shadow_positions()), 0)

    def test_canonical_date_range_event_key_deduplication(self) -> None:
        """Verify that all syntactic variants of date ranges produce an identical canonical event key."""
        variants = [
            "Will Elon Musk post 200-219 tweets from November 6 to November 13, 2026?",
            "Will Elon Musk post 220-239 tweets November 6 to November 13?",
            "Will Elon Musk post 240-259 tweets November 6-13?",
            "Will Elon Musk post 260-279 tweets between November 6 and November 13, 2026?",
            "Will Elon Musk post 280-299 tweets from November 6 to 13?",
        ]
        keys = {extract_event_key(q, "Geopolitics") for q in variants}
        self.assertEqual(len(keys), 1)
        self.assertEqual(keys.pop(), "mentions:elon_musk:november 6 - november 13")

        # Crypto weekly date range deduplication
        c1 = extract_event_key("Will Bitcoin dip to $72,000 November 9-15?", "Crypto")
        c2 = extract_event_key("Will Bitcoin dip to $70,000 from November 9 to November 15, 2026?", "Crypto")
        self.assertEqual(c1, c2)
        self.assertEqual(c1, "crypto:bitcoin:november 9 - november 15")

    def test_shadow_take_profit_near_ceiling(self) -> None:
        """Verify that shadow positions exit on near-ceiling 98.5%+ bids even when bought at high price."""
        from unittest.mock import patch
        from polymarket_api import MarketInfo
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db = SimDatabase(db_path=Path(tmp_dir) / "test_stp.db", initial_capital=50.0)
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=Path(tmp_dir) / "trades.txt")

            db.open_shadow_position(
                market_id="mkt_stp_1", question="High Price Favorite", category="Crypto", side="YES",
                token_id="tok_stp", shares=10.0, entry_vwap=0.90, cost_usdc=9.00,
                initial_p_est=0.95, entry_edge=0.05, kelly_full_pct=0.10, kelly_half_pct=0.05,
                applied_size_pct=0.05, roundtrip_slippage_pct=0.01, official_source="Binance",
                exit_condition="Hold", rationale="Consensus", end_date_iso="2026-11-20T00:00:00Z"
            )

            m_live = MarketInfo(
                id="mkt_stp_1", question="High Price Favorite", slug="hpf",
                description="", resolution_source="Binance", has_official_source=True,
                end_date_iso="2026-11-20T00:00:00Z", hours_to_close=20.0,
                liquidity_usd=10000.0, volume_24h_usd=20000.0, outcomes=["YES", "NO"],
                gamma_prices=[0.985, 0.015], clob_token_ids=["tok_yes", "tok_no"],
                order_min_size=1.0, tick_size=0.01, category="Crypto", closed=False,
            )

            with patch("trader.fetch_market_by_id", return_value=m_live), \
                 patch("trader.simulate_clob_sell_shares", return_value=(0.988, 9.88, 0.988)):
                closed = trader.monitor_and_manage_shadow_positions()

            self.assertEqual(closed, 1)
            pos = db.get_all_shadow_positions()[0]
            self.assertEqual(pos["status"], "CLOSED")
            self.assertIn("TAKE PROFIT (98.5%+ Bid Reached)", pos["exit_reason"])
            self.assertAlmostEqual(float(pos["realized_pnl"]), 0.88, places=2)

    def test_shadow_deduplication_and_contract_price_bounds(self) -> None:
        """Verify that shadow candidate evaluation deduplicates same event key and rejects out-of-bounds contract prices."""
        from unittest.mock import patch, MagicMock
        from polymarket_api import MarketInfo, OrderBookSimulation
        from oracles import EvaluationResult

        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db = SimDatabase(db_path=Path(tmp_dir) / "test_sdedup.db", initial_capital=50.0)
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=Path(tmp_dir) / "trades.txt")

            mkt1 = MarketInfo(
                id="mkt_dup_1", question="Will Elon Musk post 200-219 tweets November 6-13?", slug="m1",
                description="", resolution_source="https://x.com", has_official_source=True,
                end_date_iso="2026-11-13T17:00:00Z", hours_to_close=10.0,
                liquidity_usd=10000.0, volume_24h_usd=20000.0, outcomes=["YES", "NO"],
                gamma_prices=[0.30, 0.70], clob_token_ids=["tok_1_y", "tok_1_n"],
                order_min_size=1.0, tick_size=0.01, category="Geopolitics", closed=False,
            )
            mkt2 = MarketInfo(
                id="mkt_dup_2", question="Will Elon Musk post 220-239 tweets from November 6 to November 13, 2026?", slug="m2",
                description="", resolution_source="https://x.com", has_official_source=True,
                end_date_iso="2026-11-13T17:00:00Z", hours_to_close=10.0,
                liquidity_usd=10000.0, volume_24h_usd=20000.0, outcomes=["YES", "NO"],
                gamma_prices=[0.30, 0.70], clob_token_ids=["tok_2_y", "tok_2_n"],
                order_min_size=1.0, tick_size=0.01, category="Geopolitics", closed=False,
            )

            eval_res = EvaluationResult(
                market_id="mkt_dup_1", question=mkt1.question, category="Geopolitics",
                oracle_used="TestOracle", official_source="X", p_yes=0.20, p_no=0.80,
                confidence=0.90, rationale="Test",
            )
            ob_good = OrderBookSimulation(
                token_id="tok_1_n", side_label="NO", best_bid=0.69, best_ask=0.70, midpoint=0.695,
                spread_pct=0.015, bet_usdc=2.00, shares_filled=2.857, vwap_buy_price=0.70,
                vwap_sell_price=0.69, entry_slippage_pct=0.005, exit_slippage_pct=0.005,
                roundtrip_slippage_pct=0.01, sufficient_depth=True, passes_slippage_limit=True,
            )

            with patch.object(trader, "_evaluate_market_probability", return_value=(eval_res, None)), \
                 patch("trader.simulate_clob_buy_and_exit_check", return_value=ob_good):
                opened = trader.evaluate_and_execute_shadow_candidates([mkt1, mkt2], open_shadow_market_ids=set())

            # Only 1 position should open; mkt2 shares the exact same canonical event key!
            self.assertEqual(opened, 1)
            self.assertEqual(len(db.get_open_shadow_positions()), 1)

    def test_warsaw_station_registered_in_weather_oracle(self) -> None:
        """Verify that Warsaw station is present in WeatherOracle.STATIONS."""
        from oracles import WeatherOracle
        wo = WeatherOracle()
        self.assertIn("warsaw", wo.STATIONS)
        station_info = wo.STATIONS["warsaw"]
        self.assertEqual(station_info[2], "Europe/Warsaw")
        self.assertEqual(station_info[3], "celsius")

    def test_helsinki_and_madrid_stations_registered_in_weather_oracle(self) -> None:
        """Verify that Helsinki and Madrid stations are present in WeatherOracle.STATIONS."""
        from oracles import WeatherOracle
        wo = WeatherOracle()
        self.assertIn("helsinki", wo.STATIONS)
        hel_info = wo.STATIONS["helsinki"]
        self.assertEqual(hel_info[2], "Europe/Helsinki")
        self.assertEqual(hel_info[3], "celsius")

        self.assertIn("madrid", wo.STATIONS)
        mad_info = wo.STATIONS["madrid"]
        self.assertEqual(mad_info[2], "Europe/Madrid")
        self.assertEqual(mad_info[3], "celsius")

    def test_hard_stop_loss_triggers_regardless_of_high_initial_p_est(self) -> None:
        """Verify that a 40%+ price drop triggers a HARD STOP-LOSS even if initial P_est was 95%."""
        import gc
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db_path = Path(tmp_dir) / "test_sim.db"
            db = SimDatabase(db_path=db_path, initial_capital=50.0)
            trades_log = Path(tmp_dir) / "trades.txt"
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=trades_log)

            # Open a virtual position with entry 0.90, high conviction p_est 0.95
            pos_id = db.open_position(
                market_id="test_high_p_mkt",
                question="Will High Conviction Event Win?",
                category="Sports",
                side="NO",
                token_id="tok_456",
                shares=1.11,
                entry_vwap=0.90,
                cost_usdc=1.00,
                current_bid=0.90,
                p_est=0.95,
                entry_edge=0.05,
                kelly_full_pct=0.50,
                kelly_half_pct=0.20,
                applied_size_pct=0.035,
                roundtrip_slippage_pct=0.01,
                official_source="Test Official",
                exit_condition="Test Exit",
                rationale="High market consensus NO",
                end_date_iso="2026-11-25T12:00:00Z",
            )

            import trader as trader_mod
            orig_sim = trader_mod.simulate_clob_sell_shares
            orig_fetch = trader_mod.fetch_market_by_id
            try:
                # Price crashes to 0.50 (44% drop from entry 0.90, exceeding 40% STOP_LOSS_PCT)
                trader_mod.simulate_clob_sell_shares = lambda tok, sh: (0.50, 0.555, 0.50)
                # Oracle returns None because consensus has dissolved
                trader_mod.fetch_market_by_id = lambda mid: None

                closed = trader.monitor_and_manage_open_positions()
                self.assertEqual(closed, 1)

                closed_pos = db.get_all_positions()[0]
                self.assertEqual(closed_pos["status"], "CLOSED")
                self.assertIn("STOP-LOSS TRIGGERED", closed_pos["exit_reason"])
                self.assertEqual(closed_pos["exit_vwap"], 0.50)
            finally:
                trader_mod.simulate_clob_sell_shares = orig_sim
                trader_mod.fetch_market_by_id = orig_fetch
                del db, trader
                gc.collect()

    def test_is_entertainment_or_meme_trap(self) -> None:
        """Verify that streamer marathons and celebrity gossip are identified as traps."""
        traps = [
            "Will Kai Cenat finish his GTA VI marathon by November 23?",
            "Will Kai Cenat finish his GTA VI marathon by November 24?",
            "Will IShowSpeed reach 40 million subscribers in 2026?",
            "Fourth Jensen Huang affair reported by November 20?",
            "Will MrBeast launch a new channel by December?",
        ]
        for q in traps:
            self.assertTrue(
                GrokCharterPaperTrader.is_entertainment_or_meme_trap(q),
                f"Expected trap detection for: {q}",
            )

        legit = [
            "Pelicans vs. Spurs",
            "Dolphins vs. Bills",
            "Israel x Iran ceasefire continues through November 22?",
            "US x Iran ceasefire continues through October 24?",
        ]
        for q in legit:
            self.assertFalse(
                GrokCharterPaperTrader.is_entertainment_or_meme_trap(q),
                f"Expected clean legit pass for: {q}",
            )

    def test_marathon_deadline_event_key_deduplication(self) -> None:
        """Verify that multi-deadline marathons/challenges produce identical event keys."""
        k1 = extract_event_key("Will Kai Cenat finish his GTA VI marathon by November 23?", "Other")
        k2 = extract_event_key("Will Kai Cenat finish his GTA VI marathon by November 24?", "Other")
        self.assertEqual(k1, k2)

    def test_live_evaluation_disallows_news_fallback(self) -> None:
        """Verify that live probability evaluation disallows news oracle by default."""
        from polymarket_api import MarketInfo
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
            db = SimDatabase(db_path=Path(tmp_dir) / "test.db", initial_capital=50.0)
            trader = GrokCharterPaperTrader(db=db, trades_txt_path=Path(tmp_dir) / "trades.txt")

            mkt = MarketInfo(
                id="other_mkt_1",
                question="Will Random Entertainment Event Occur?",
                slug="other-mkt-1",
                description="",
                resolution_source="https://example.com",
                outcomes=["YES", "NO"],
                order_min_size=1.0,
                tick_size=0.01,
                category="Other",
                end_date_iso="2026-11-25T12:00:00Z",
                hours_to_close=72.0,
                gamma_prices=[0.50, 0.50],
                volume_24h_usd=20000.0,
                liquidity_usd=10000.0,
                clob_token_ids=["tok_y", "tok_n"],
                has_official_source=True,
            )

            # In live mode (default), unmodeled Other market must return None
            eval_res, _ = trader._evaluate_market_probability(mkt)
            self.assertIsNone(eval_res)

    def test_category_classification_hurricanes_vs_weather(self) -> None:
        """Verify that sports teams named Hurricanes/Thunder/Lightning are classified as Sports, not Weather."""
        from polymarket_api import classify_market_category

        # NHL match involving Carolina Hurricanes
        self.assertEqual(
            classify_market_category("Hurricanes vs. Rangers", "https://www.nhl.com/scores"),
            "Sports"
        )
        self.assertEqual(
            classify_market_category("Canadiens vs. Hurricanes", "https://www.nhl.com/scores"),
            "Sports"
        )
        self.assertEqual(
            classify_market_category("Capitals vs. Hurricanes", "NHL Regular Season Match"),
            "Sports"
        )

        # Actual Weather markets (storms or temperature)
        self.assertEqual(
            classify_market_category("Will Hurricane Rafael make landfall in Florida?", "NOAA NHC"),
            "Weather"
        )
        self.assertEqual(
            classify_market_category("Will the highest temperature in London be 10°C or higher on November 21?", "METAR"),
            "Weather"
        )

    def test_category_classification_match_draw(self) -> None:
        """Verify that soccer draw questions are classified as Sports and deduplicated."""
        from polymarket_api import classify_market_category
        from trader import extract_event_key

        self.assertEqual(
            classify_market_category("Will the match end in a draw?", "Official match result"),
            "Sports",
        )
        self.assertEqual(
            classify_market_category("Will FC Barcelona vs. Villarreal CF end in a draw?", "La Liga match"),
            "Sports",
        )

        k_match = extract_event_key("FC Barcelona vs. Villarreal CF", "Sports")
        k_draw = extract_event_key("Will FC Barcelona vs. Villarreal CF end in a draw?", "Sports")
        self.assertEqual(k_match, k_draw)

    def test_extract_resolution_source_word_boundaries(self) -> None:
        """Verify that substring collisions like 'conflicting' do not trigger false 'NFL' resolution sources."""
        from polymarket_api import extract_resolution_source

        desc_conflict = "Where multiple sources conflict regarding the occurrence, this market will remain open."
        src, has_src = extract_resolution_source("", desc_conflict)
        self.assertNotEqual(src, "Official NFL data feed")

        desc_nfl = "Official NFL scores and statistics."
        src2, has_src2 = extract_resolution_source("", desc_nfl)
        self.assertEqual(src2, "Official NFL data feed")
        self.assertTrue(has_src2)

    def test_category_classification_laliga_exact_score_and_geopolitics(self) -> None:
        """Verify that LALIGA, Exact Score, and key Geopolitical phrasing are correctly classified."""
        from polymarket_api import classify_market_category, MarketInfo
        from oracles import is_esports_market

        self.assertEqual(
            classify_market_category("Will Real Madrid win the 2026-27 LALIGA Championship?", "Official standings"),
            "Sports"
        )
        self.assertEqual(
            classify_market_category("Exact Score: Any Other Score?", "Match Result"),
            "Sports"
        )
        self.assertEqual(
            classify_market_category("Russia military action against an EU country by December 31, 2026?", "Consensus"),
            "Geopolitics"
        )
        self.assertEqual(
            classify_market_category("Xi Jinping out before 2027?", "News"),
            "Geopolitics"
        )
        self.assertEqual(
            classify_market_category("Netanyahu out by end of 2026?", "News"),
            "Geopolitics"
        )
        self.assertEqual(
            classify_market_category("Will Nicolás Maduro be the leader of Venezuela end of 2026?", "News"),
            "Geopolitics"
        )
        self.assertEqual(
            classify_market_category("Will FURIA Win the PGL Major Singapore 2026?", "Esports match"),
            "Sports"
        )

        dummy_market = MarketInfo(
            id="test-pgl",
            question="Will FURIA Win the PGL Major Singapore 2026?",
            slug="test-pgl",
            description="",
            resolution_source="Liquipedia",
            has_official_source=True,
            end_date_iso="",
            hours_to_close=24.0,
            liquidity_usd=10000.0,
            volume_24h_usd=20000.0,
            outcomes=["Yes", "No"],
            gamma_prices=[0.9, 0.1],
            clob_token_ids=["1", "2"],
            order_min_size=1.0,
            tick_size=0.01,
            category="Sports",
        )
        self.assertTrue(is_esports_market(dummy_market))


if __name__ == "__main__":
    unittest.main()


