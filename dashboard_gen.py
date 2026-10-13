"""
Generates an interactive HTML Dashboard (`dashboard.html`) and Markdown Status Report (`STATUS_REPORT.md`)
for the Polymarket Autonomous Paper-Trading Simulator.
"""

import html
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from database import SimDatabase
from trader import TRADES_LOG_PATH


DASHBOARD_HTML_PATH = Path(__file__).resolve().parent / "data" / "dashboard.html"
STATUS_MD_PATH = Path(__file__).resolve().parent / "data" / "STATUS_REPORT.md"


def generate_reports(
    db: SimDatabase,
    html_path: Path = DASHBOARD_HTML_PATH,
    md_path: Path = STATUS_MD_PATH,
    trades_txt_path: Path = TRADES_LOG_PATH,
) -> Dict[str, str]:
    pf = db.recalculate_portfolio()
    open_pos = db.get_open_positions()
    all_pos = db.get_all_positions(limit=100)
    closed_pos = [p for p in all_pos if p["status"] in ("CLOSED", "RESOLVED")]
    candidates = db.get_recent_candidates(limit=35)
    cycles = db.get_scan_cycles(limit=25)

    initial_cap = float(pf.get("initial_capital", 50.0))
    total_eq = float(pf.get("total_equity", 50.0))
    cash = float(pf.get("cash_usdc", 50.0))
    locked = float(pf.get("locked_usdc", 0.0))
    peak_eq = float(pf.get("peak_equity", 50.0))
    curr_dd = float(pf.get("current_drawdown_pct", 0.0)) * 100.0
    max_dd = float(pf.get("max_drawdown_pct", 0.0)) * 100.0
    target_mo = float(pf.get("monthly_target_usdc", 60.0))

    net_pnl = total_eq - initial_cap
    roi_pct = (net_pnl / initial_cap * 100.0) if initial_cap > 0 else 0.0
    sub_progress_pct = min(max((net_pnl / target_mo) * 100.0, 0.0), 100.0)

    wins = sum(1 for p in closed_pos if float(p.get("realized_pnl", 0.0)) > 0)
    win_rate = (wins / len(closed_pos) * 100.0) if closed_pos else 0.0

    # Brier score on resolved positions
    resolved_pos = [p for p in closed_pos if p["status"] == "RESOLVED"]
    brier_score_str = "N/A (ожидание экспирации)"
    if resolved_pos:
        brier_sum = 0.0
        for rp in resolved_pos:
            outcome = 1.0 if float(rp.get("exit_vwap", 0.0)) >= 0.95 else 0.0
            p_pred = float(rp.get("initial_p_est", 0.5))
            brier_sum += (p_pred - outcome) ** 2
        brier_score_str = f"{brier_sum / len(resolved_pos):.4f}"

    trades_txt_content = ""
    if trades_txt_path.exists():
        trades_txt_content = trades_txt_path.read_text(encoding="utf-8", errors="replace")

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # 1. Generate Markdown Status Report
    md_lines = [
        "# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)",
        f"**Обновлено:** `{now_str}`",
        "",
        "## 💰 Состояние виртуального портфеля",
        "| Показатель | Значение | Правило устава |",
        "| :--- | :--- | :--- |",
        f"| **Стартовый капитал** | `${initial_cap:.2f} USDC` | Не добавлять деньги |",
        f"| **Текущий баланс (Equity)** | **`${total_eq:.2f} USDC`** (`{net_pnl:+.2f}$` / `{roi_pct:+.2f}%`) | Cash + Mark-to-Market по CLOB Bid |",
        f"| **Свободный кэш / В сделках** | `${cash:.2f}` / `${locked:.2f} USDC` | До 8 открытых позиций, макс 8% банка |",
        f"| **Цель окупаемости подписки** | `${net_pnl:+.2f} / ${target_mo:.2f}` (`{sub_progress_pct:.1f}%`) | Цель: +$60.00 в месяц |",
        f"| **Просадка от пика (Текущая / Макс)** | `{curr_dd:.2f}%` / `{max_dd:.2f}%` (Пик: `${peak_eq:.2f}`) | Стоп-кран при просадке 40% |",
        f"| **Закрытых сделок / Win Rate** | `{len(closed_pos)}` / `{win_rate:.1f}%` | Brier Score: `{brier_score_str}` |",
        "",
        f"## 📂 Открытые позиции ({len(open_pos)} / 8)",
    ]

    if not open_pos:
        md_lines.append("*Нет активных позиций.*")
    else:
        md_lines.extend([
            "| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |",
            "| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
        ])
        for p in open_pos:
            upnl = float(p["unrealized_pnl"])
            md_lines.append(
                f"| #{p['id']} | {p['question'][:55]} | {p['category']} | **{p['side']}** | "
                f"`{float(p['entry_vwap']):.3f}` | `{float(p['current_bid']):.3f}` | "
                f"`{float(p['latest_p_est'])*100:.1f}%` | `${float(p['cost_usdc']):.2f}` | "
                f"`${upnl:+.2f}` | {p['official_source'][:30]} |"
            )

    md_lines.extend([
        "",
        "## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB",
        "| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ])
    for c in candidates[:18]:
        md_lines.append(
            f"| {c['question'][:50]} | {c['category']} | {c['side']} | "
            f"`{float(c['p_estimated'])*100:.1f}%` | `{float(c['ask_vwap'])*100:.1f}%` | "
            f"`{float(c['edge'])*100:+.1f} п.п.` | `{float(c['roundtrip_slippage_pct'])*100:.2f}%` | {c['decision']} |"
        )

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    # 2. Generate Interactive HTML Dashboard
    open_rows_html = ""
    for p in open_pos:
        upnl = float(p["unrealized_pnl"])
        pnl_cls = "pos" if upnl >= 0 else "neg"
        open_rows_html += f"""
        <tr>
            <td>#{p['id']}</td>
            <td><strong>{html.escape(p['question'])}</strong><br><small class="muted">{html.escape(p['rationale'])}</small></td>
            <td><span class="badge cat-{p['category'].lower()}">{html.escape(p['category'])}</span></td>
            <td><span class="side-{p['side'].lower()}">{html.escape(p['side'])}</span></td>
            <td>{float(p['shares']):.2f}</td>
            <td>${float(p['entry_vwap']):.4f}</td>
            <td>${float(p['current_bid']):.4f}</td>
            <td><strong>{float(p['latest_p_est'])*100:.1f}%</strong> <small>(+{float(p['entry_edge'])*100:.1f}pp)</small></td>
            <td>${float(p['cost_usdc']):.2f} <small>({float(p['applied_size_pct'])*100:.1f}%)</small></td>
            <td class="{pnl_cls}">${upnl:+.2f}</td>
            <td><small>{html.escape(p['exit_condition'])}</small></td>
        </tr>
        """
    if not open_rows_html:
        open_rows_html = '<tr><td colspan="11" class="empty">Нет открытых позиций</td></tr>'

    cand_rows_html = ""
    for c in candidates[:25]:
        is_exec = str(c["decision"]).startswith("EXECUTED")
        row_cls = "exec-row" if is_exec else ""
        edge_val = float(c["edge"]) * 100.0
        slip_val = float(c["roundtrip_slippage_pct"]) * 100.0
        cand_rows_html += f"""
        <tr class="{row_cls}">
            <td>{html.escape(c['question'])}<br><small class="muted">{html.escape(c['rationale'])}</small></td>
            <td><span class="badge cat-{c['category'].lower()}">{html.escape(c['category'])}</span></td>
            <td>{html.escape(c['side'])}</td>
            <td>{float(c['p_estimated'])*100:.1f}%</td>
            <td>{float(c['ask_vwap'])*100:.1f}%</td>
            <td class="{'pos' if edge_val >= 8.0 else 'muted'}">{edge_val:+.1f} п.п.</td>
            <td class="{'pos' if slip_val <= 3.0 else 'neg'}">{slip_val:.2f}%</td>
            <td>${float(c['liquidity_usd']):,.0f}</td>
            <td>{float(c['hours_to_close']):.1f}h</td>
            <td><strong>{html.escape(c['decision'])}</strong></td>
        </tr>
        """

    html_doc = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<title>Polymarket Paper Trader — Grok Charter Simulator</title>
<style>
  :root {{
    --bg: #0b0f19;
    --card: #131b2e;
    --border: #23304d;
    --text: #e2e8f0;
    --muted: #8b9bb4;
    --green: #10b981;
    --red: #ef4444;
    --blue: #3b82f6;
    --amber: #f59e0b;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; padding: 24px;
    background: var(--bg); color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace;
    line-height: 1.45;
  }}
  h1, h2, h3 {{ margin-top: 0; }}
  .header {{
    display: flex; justify-content: space-between; align-items: center;
    border-bottom: 1px solid var(--border); padding-bottom: 16px; margin-bottom: 24px;
  }}
  .grid {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 16px; margin-bottom: 24px;
  }}
  .card {{
    background: var(--card); border: 1px solid var(--border);
    border-radius: 10px; padding: 16px;
  }}
  .metric-label {{ font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }}
  .metric-val {{ font-size: 26px; font-weight: 700; margin-top: 6px; }}
  .metric-sub {{ font-size: 12px; color: var(--muted); margin-top: 4px; }}
  .pos {{ color: var(--green); font-weight: 600; }}
  .neg {{ color: var(--red); font-weight: 600; }}
  .muted {{ color: var(--muted); }}
  table {{
    width: 100%; border-collapse: collapse; font-size: 13px;
    background: var(--card); border: 1px solid var(--border); border-radius: 10px; overflow: hidden;
    margin-bottom: 24px;
  }}
  th, td {{
    padding: 10px 12px; text-align: left; border-bottom: 1px solid var(--border);
    vertical-align: top;
  }}
  th {{ background: #19233c; color: var(--muted); font-weight: 600; text-transform: uppercase; font-size: 11px; }}
  tr.exec-row {{ background: rgba(16, 185, 129, 0.08); }}
  .badge {{
    display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 11px; font-weight: 600;
    background: #1e293b; color: #cbd5e1;
  }}
  .cat-weather {{ background: rgba(59, 130, 246, 0.2); color: #60a5fa; }}
  .cat-crypto {{ background: rgba(245, 158, 11, 0.2); color: #fbbf24; }}
  .side-yes {{ color: var(--green); font-weight: 700; }}
  .side-no {{ color: var(--red); font-weight: 700; }}
  pre.log-box {{
    background: #070a12; border: 1px solid var(--border); border-radius: 10px;
    padding: 16px; font-size: 12px; color: #a5b4fc; overflow-x: auto; max-height: 450px;
  }}
  .empty {{ text-align: center; color: var(--muted); padding: 20px; }}
</style>
</head>
<body>
  <div class="header">
    <div>
      <h1>🤖 Polymarket Paper-Trading Simulator (Устав Grok Bot)</h1>
      <div class="muted">Реальный стакан CLOB • Фактические оракулы (Binance 1m/1h, NOAA/METAR Погода, News RSS) • Без риска реальными деньгами</div>
    </div>
    <div style="text-align:right">
      <div class="badge" style="background:rgba(16,185,129,0.2);color:#34d399;padding:6px 12px;font-size:13px;">
        STATUS: {"HALTED (STOP-LOSS)" if pf.get("halted") else "ACTIVE DEMO ACCOUNT"}
      </div>
      <div class="metric-sub">Обновлено: {now_str}</div>
    </div>
  </div>

  <div class="grid">
    <div class="card">
      <div class="metric-label">Текущий капитал (Equity)</div>
      <div class="metric-val">${total_eq:.2f} <span style="font-size:15px" class="{'pos' if net_pnl >= 0 else 'neg'}">({net_pnl:+.2f}$ / {roi_pct:+.2f}%)</span></div>
      <div class="metric-sub">Старт: ${initial_cap:.2f} USDC (Оценка по Bid стакана!)</div>
    </div>
    <div class="card">
      <div class="metric-label">Свободный кэш / В позициях</div>
      <div class="metric-val">${cash:.2f} <span class="muted" style="font-size:16px">/ ${locked:.2f}</span></div>
      <div class="metric-sub">Открыто позиций: {len(open_pos)} из 8 (макс 8% банка)</div>
    </div>
    <div class="card">
      <div class="metric-label">Цель подписки ($60 / мес)</div>
      <div class="metric-val">${net_pnl:+.2f} <span class="muted" style="font-size:16px">/ $60.00</span></div>
      <div class="metric-sub">Прогресс окупаемости: {sub_progress_pct:.1f}%</div>
    </div>
    <div class="card">
      <div class="metric-label">Просадка от пика (Drawdown)</div>
      <div class="metric-val {'neg' if curr_dd >= 20 else ''}">{curr_dd:.2f}% <span class="muted" style="font-size:15px">(Макс: {max_dd:.2f}%)</span></div>
      <div class="metric-sub">Пик: ${peak_eq:.2f} | Лимит остановки: 40.0%</div>
    </div>
    <div class="card">
      <div class="metric-label">Закрытые сделки / Win Rate</div>
      <div class="metric-val">{len(closed_pos)} <span class="muted" style="font-size:16px">({win_rate:.1f}%)</span></div>
      <div class="metric-sub">Brier Score: {brier_score_str}</div>
    </div>
  </div>

  <h2>📂 Открытые виртуальные позиции ({len(open_pos)} / 8)</h2>
  <table>
    <thead>
      <tr>
        <th>ID</th><th>Рынок и обоснование</th><th>Кат.</th><th>Исход</th><th>Доли</th>
        <th>Вход (Ask VWAP)</th><th>Текущий Bid</th><th>Оценка (Edge)</th><th>Размер (% банка)</th>
        <th>Нереализ. PnL</th><th>Условие выхода</th>
      </tr>
    </thead>
    <tbody>
      {open_rows_html}
    </tbody>
  </table>

  <h2>🔍 Журнал фильтрации кандидатов и проверка стакана CLOB (последние оценки)</h2>
  <table>
    <thead>
      <tr>
        <th>Рынок и сигнал оракула</th><th>Кат.</th><th>Сторона</th><th>Оценка бота</th>
        <th>Цена Ask VWAP</th><th>Перекос (Edge)</th><th>Проскальзывание вх/вых</th>
        <th>Ликвидность</th><th>До закрытия</th><th>Вердикт фильтра</th>
      </tr>
    </thead>
    <tbody>
      {cand_rows_html}
    </tbody>
  </table>

  <h2>📜 Лог сделок и циклов (trades.txt)</h2>
  <pre class="log-box">{html.escape(trades_txt_content[-15000:])}</pre>
</body>
</html>
"""
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html_doc, encoding="utf-8")

    return {"html": str(html_path), "markdown": str(md_path), "trades_txt": str(trades_txt_path)}
