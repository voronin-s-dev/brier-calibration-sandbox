"""
CLI & Background Daemon Runner for Polymarket Autonomous Paper Trader (Grok Charter).
Usage:
  python run_sim.py --once                  # Run one full 10-min cycle & update dashboard
  python run_sim.py --loop --interval 600   # Run autonomously every 10 minutes
  python run_sim.py --status                # Show current portfolio & open positions
  python run_sim.py --set-category Weather  # Switch category filter (ALL, Weather, Crypto, etc.)
"""

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

sys.path.insert(0, str(Path(__file__).resolve().parent))

from dashboard_gen import generate_reports
from database import SimDatabase
from trader import GrokCharterPaperTrader


def git_sync_snapshot(commit_msg: str = "chore: update calibration snapshot [skip ci]") -> bool:
    """Safely stages data/ files, commits, and pushes to origin/main."""
    try:
        subprocess.run(["git", "add", "data/"], check=True)
        res = subprocess.run(["git", "diff", "--staged", "--quiet"])
        if res.returncode != 0:
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)
            subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print(f"🚀 [GIT SYNC] Snapshot successfully pushed: {commit_msg}")
            return True
        else:
            print("ℹ️ [GIT SYNC] No new file modifications in data/ to push.")
    except Exception as e:
        print(f"⚠️ [GIT SYNC WARNING]: {e}", file=sys.stderr)
    return False


def print_console_summary(db: SimDatabase) -> None:
    pf = db.recalculate_portfolio()
    open_pos = db.get_open_positions()
    candidates = db.get_recent_candidates(limit=10)

    init_cap = float(pf["initial_capital"])
    eq = float(pf["total_equity"])
    cash = float(pf["cash_usdc"])
    locked = float(pf["locked_usdc"])
    pnl = eq - init_cap
    dd = float(pf["current_drawdown_pct"]) * 100.0

    print("=" * 82)
    print(f"🤖 POLYMARKET DEMO ACCOUNT (УСТАВ GROK) | STATUS: {'HALTED' if pf['halted'] else 'ACTIVE'}")
    print(
        f"💰 Баланс (Equity): ${eq:.2f} USDC ({pnl:+.2f}$ / {pnl/init_cap*100:+.2f}%) | "
        f"Кэш: ${cash:.2f} | В сделках (по Bid): ${locked:.2f}"
    )
    print(
        f"📉 Просадка от пика: {dd:.2f}% (Лимит стоп-крана: 40%) | "
        f"Фильтры: Cat={pf['active_category_filter']}, Liq>=${pf['min_liquidity_filter']:,.0f}, "
        f"Slippage<={pf['max_slippage_filter']*100:.1f}%"
    )
    print("-" * 82)
    print(f"📂 ОТКРЫТЫЕ ПОЗИЦИИ ({len(open_pos)} / {GrokCharterPaperTrader.MAX_OPEN_POSITIONS}):")
    if not open_pos:
        print("   (пока нет открытых позиций)")
    else:
        for p in open_pos:
            print(
                f"   #{p['id']} [{p['category']}] {p['side']} | {p['question'][:55]}\n"
                f"      Вход Ask VWAP: ${p['entry_vwap']:.4f} | Текущий Bid VWAP: ${p['current_bid']:.4f} | "
                f"Оценка: {p['latest_p_est']*100:.1f}% (Edge +{p['entry_edge']*100:.1f}pp) | "
                f"Сумма: ${p['cost_usdc']:.2f} | MTM PnL: ${p['unrealized_pnl']:+.2f}"
            )
    print("-" * 82)
    if pf.get("active_category_filter") != "ALL":
        spf = db.get_shadow_portfolio()
        s_open = db.get_open_shadow_positions()
        s_stats = db.get_shadow_category_stats()
        print(f"🧪 ТЕНЕВАЯ ПЕСОЧНИЦА (Shadow Sandbox):")
        print(
            f"   Эквити: ${float(spf.get('total_equity', 50)):.2f} USDC | "
            f"Кэш: ${float(spf.get('cash_usdc', 50)):.2f} | Открыто: {len(s_open)}/5"
        )
        if s_stats:
            stats_str = ", ".join(f"{c}: {int(s['count'])} сд. (${s['pnl']:+.2f})" for c, s in s_stats.items())
            print(f"   Результаты по замороженным категориям: {stats_str}")
        print("-" * 82)
    print("🔍 ПОСЛЕДНИЕ ОЦЕНЕННЫЕ РЫНКИ И ПРОВЕРКА СТАКАНА CLOB:")
    for c in candidates[:8]:
        print(
            f"   • [{c['category']}] {c['question'][:52]} ({c['side']})\n"
            f"     Оценка={c['p_estimated']*100:.1f}% vs Ask={c['ask_vwap']*100:.1f}% "
            f"(Edge={c['edge']*100:+.1f}pp) | CLOB Slippage={c['roundtrip_slippage_pct']*100:.2f}% -> {c['decision']}"
        )
    print("=" * 82)


def main() -> None:
    parser = argparse.ArgumentParser(description="Polymarket Autonomous Paper-Trading Simulator")
    parser.add_argument("--once", action="store_true", help="Run a single scan & trade cycle")
    parser.add_argument("--loop", action="store_true", help="Run continuously in a loop")
    parser.add_argument("--cycles", type=int, default=1, help="Number of cycles to run in this session (e.g. 3 or 4)")
    parser.add_argument("--interval", type=int, default=600, help="Loop interval in seconds (default 600s = 10m)")
    parser.add_argument("--git-sync", action="store_true", help="Auto-commit and push data/ snapshot to GitHub after each cycle")
    parser.add_argument("--status", action="store_true", help="Show current status and regenerate dashboard")
    parser.add_argument("--scan-limit", type=int, default=800, help="Number of active Gamma markets to scan per cycle")
    parser.add_argument("--set-category", type=str, help="Set category filter (ALL, Weather, Crypto, Sports, Macro)")
    parser.add_argument("--set-liquidity", type=float, help="Set minimum liquidity filter in USD (e.g. 5000 or 10000)")
    parser.add_argument("--set-slippage", type=float, help="Set max round-trip CLOB slippage (e.g. 0.03 or 0.02)")
    parser.add_argument("--governor", action="store_true", help="Run 3-tier Auto-Governor audit and generate GOVERNANCE_REPORT.md")
    parser.add_argument("--approve", type=int, help="Approve and apply a pending Semi-Auto proposal by ID")
    parser.add_argument("--dismiss", type=int, help="Dismiss a pending Semi-Auto proposal by ID")
    parser.add_argument("--reset-halt", action="store_true", help="Reset 40% kill-switch and re-baseline peak equity to current equity")
    args = parser.parse_args()

    db = SimDatabase(initial_capital=50.0)
    from auto_governor import AutoGovernor
    gov = AutoGovernor(db)

    if args.approve is not None:
        ok, msg = gov.approve_proposal(args.approve)
        print(msg)
        generate_reports(db)
        return

    if args.dismiss is not None:
        ok, msg = gov.dismiss_proposal(args.dismiss)
        print(msg)
        generate_reports(db)
        return

    if args.reset_halt:
        trader = GrokCharterPaperTrader(db=db)
        trader.monitor_and_manage_open_positions()
        pf = db.reset_kill_switch()
        gov.generate_governance_report()
        paths = generate_reports(db)
        print_console_summary(db)
        print(f"🔄 Стоп-кран 40% сброшен. Базовый пик перенесён на ${pf['peak_equity']:.2f} USDC.")
        return

    if args.set_category or args.set_liquidity is not None or args.set_slippage is not None:
        with db._connect() as conn:
            if args.set_category:
                conn.execute("UPDATE portfolio_state SET active_category_filter = ? WHERE id = 1", (args.set_category,))
            if args.set_liquidity is not None:
                conn.execute("UPDATE portfolio_state SET min_liquidity_filter = ? WHERE id = 1", (args.set_liquidity,))
            if args.set_slippage is not None:
                conn.execute("UPDATE portfolio_state SET max_slippage_filter = ? WHERE id = 1", (args.set_slippage,))
            conn.commit()
        gov.generate_governance_report()

    if args.governor and not args.once and not args.loop:
        res_gov = gov.evaluate_portfolio_and_rules()
        rep_path = gov.generate_governance_report()
        print(f"🧠 Auto-Governor проверил портфель (новых событий: {len(res_gov['triggered_event_ids'])}).")
        print(f"📄 Отчёт решений: {rep_path}")
        return

    trader = GrokCharterPaperTrader(db=db)

    if args.status and not args.once and not args.loop:
        trader.monitor_and_manage_open_positions()
        gov.evaluate_portfolio_and_rules()
        paths = generate_reports(db)
        print_console_summary(db)
        print(f"📊 Дашборд обновлён: {paths['html']}")
        return

    if args.cycles > 1:
        print(f"🚀 Запуск сессионного облачного цикла: {args.cycles} итераций с интервалом {args.interval} сек...")
        for i in range(1, args.cycles + 1):
            try:
                print(f"\n--- [ОБЛАЧНАЯ СЕССИЯ: ИТЕРАЦИЯ {i}/{args.cycles}] ---")
                res = trader.run_cycle(max_markets_to_scan=args.scan_limit)
                paths = generate_reports(db)
                print_console_summary(db)
                print(f"✅ Цикл #{res.get('cycle_id')} завершён.")
                if args.git_sync or os.getenv("GITHUB_ACTIONS") == "true":
                    git_sync_snapshot(f"chore: calibration cycle #{res.get('cycle_id')} [skip ci]")
            except Exception as e:
                print(f"⚠️ Ошибка в итерации {i}: {e}", file=sys.stderr)
            if i < args.cycles:
                time.sleep(args.interval)
        return

    if args.loop:
        print(f"🚀 Запуск автономного цикла симуляции (интервал: {args.interval} сек / {args.interval/60:.1f} мин)...")
        while True:
            try:
                res = trader.run_cycle(max_markets_to_scan=args.scan_limit)
                paths = generate_reports(db)
                print_console_summary(db)
                print(f"✅ Цикл #{res.get('cycle_id')} завершён. Дашборд: {paths['html']}")
                if args.git_sync or os.getenv("GITHUB_ACTIONS") == "true":
                    git_sync_snapshot(f"chore: calibration cycle #{res.get('cycle_id')} [skip ci]")
            except Exception as e:
                print(f"⚠️ Ошибка в цикле: {e}", file=sys.stderr)
            time.sleep(args.interval)
    else:
        # Default to running one cycle
        res = trader.run_cycle(max_markets_to_scan=args.scan_limit)
        paths = generate_reports(db)
        print_console_summary(db)
        print(f"✅ Цикл #{res.get('cycle_id')} завершён.")
        print(f"📄 Лог сделок: {paths['trades_txt']}")
        print(f"📊 Отчёт (MD): {paths['markdown']}")
        print(f"🌐 Интерактивный дашборд: {paths['html']}")
        if args.git_sync or os.getenv("GITHUB_ACTIONS") == "true":
            git_sync_snapshot(f"chore: calibration cycle #{res.get('cycle_id')} [skip ci]")


if __name__ == "__main__":
    main()
