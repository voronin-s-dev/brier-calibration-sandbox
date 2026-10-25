"""
Telegram Notifier for Polymarket Paper-Trading Simulator.
Reads TELEGRAM_BOT_TOKEN and ALLOWED_CHAT_ID from environment or local `.env`.
Focuses exclusively on actionable, human-readable information:
1. PnL Result Alerts (when positions close with profit or loss)
2. Daily Digest (once per 24 hours: balance, 24h PnL, win rate, and upcoming expirations)
"""

import json
import os
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, Dict, Optional


def _load_env_fallback() -> Dict[str, str]:
    env_vars: Dict[str, str] = {}
    env_file = Path(__file__).resolve().parent / ".env"
    if env_file.exists():
        try:
            for line in env_file.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                env_vars[k.strip()] = v.strip().strip('"').strip("'")
        except Exception:
            pass
    return env_vars


def _plural_deals(n: int) -> str:
    if 11 <= n % 100 <= 19:
        return f"{n} сделок"
    rem = n % 10
    if rem == 1:
        return f"{n} сделка"
    elif 2 <= rem <= 4:
        return f"{n} сделки"
    return f"{n} сделок"


def send_telegram_alert(text: str) -> bool:
    """Sends a message via Telegram Bot API if token and chat_id are configured."""
    fallback = _load_env_fallback()
    token = os.getenv("TELEGRAM_BOT_TOKEN") or fallback.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.getenv("ALLOWED_CHAT_ID") or fallback.get("ALLOWED_CHAT_ID", "")

    if not token or token == "your_bot_token_here" or not chat_id:
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = json.dumps({
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=8.0) as resp:
            return resp.status == 200
    except Exception:
        return False


def notify_position_closed(
    pos: Dict[str, Any],
    pnl: float,
    exit_vwap: float,
    exit_reason: str,
    total_equity: float,
) -> bool:
    """
    Sends a concise, human-readable notification when a position is closed or resolved.
    Focuses on the financial outcome ($ PnL, ROI%, total portfolio equity).
    """
    cost = float(pos.get("cost_usdc", 0.0))
    roi = (pnl / cost * 100.0) if cost > 0 else 0.0
    side = pos.get("side", "")
    question = pos.get("question", "")

    if pnl > 0.005:
        icon = "✅"
        title = "Фиксация прибыли"
    elif pnl < -0.005:
        icon = "⚠️"
        title = "Защитный выход"
    else:
        icon = "⚪"
        title = "Выход в безубыток"

    # Friendly Russian explanation of the exit trigger
    if "TAKE PROFIT" in exit_reason or exit_vwap >= 0.98:
        reason_ru = f"Достигнута целевая цена (${exit_vwap:.3f}) — прибыль зафиксирована досрочно"
    elif "MARKET RESOLVED" in exit_reason or exit_vwap >= 0.999:
        reason_ru = "Событие завершилось победой (выплата 100%)"
    elif "THESIS INVALIDATED" in exit_reason:
        reason_ru = "Вероятность события снизилась — позиция закрыта во избежание просадки"
    elif "STOP-LOSS" in exit_reason:
        reason_ru = "Сработал защитный стоп-лосс для ограничения потерь"
    else:
        reason_ru = "Позиция закрыта по правилам стратегии"

    msg = (
        f"{icon} <b>{title}: {pnl:+.2f}$ ({roi:+.1f}%)</b>\n"
        f"📌 <b>{question}</b> (Исход: <b>{side}</b>)\n"
        f"💡 {reason_ru}\n"
        f"💰 Баланс портфеля: <b>${total_equity:.2f} USDC</b>"
    )
    return send_telegram_alert(msg)


def check_and_send_daily_digest(db: Any, force: bool = False) -> bool:
    """
    Sends a consolidated daily summary once per calendar day (UTC), or if forced.
    """
    state_file = Path(__file__).resolve().parent / "data" / "last_digest.json"
    today_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if not force and state_file.exists():
        try:
            data = json.loads(state_file.read_text(encoding="utf-8"))
            if data.get("last_digest_date") == today_utc:
                return False
        except Exception:
            pass

    pf = db.recalculate_portfolio()
    total_equity = float(pf["total_equity"])
    cash = float(pf["cash_usdc"])
    locked = float(pf["locked_usdc"])

    # Calculate 24h stats
    since_24h = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()
    with db._connect() as conn:
        row = conn.execute("""
            SELECT COUNT(*), COALESCE(SUM(pnl_usdc), 0.0),
                   COALESCE(SUM(CASE WHEN pnl_usdc > 0 THEN 1 ELSE 0 END), 0)
            FROM trades_ledger
            WHERE action IN ('SELL_EXIT', 'SETTLE_RESOLVE') AND timestamp >= ?
        """, (since_24h,)).fetchone()
        closed_count = int(row[0]) if row else 0
        pnl_24h = float(row[1]) if row else 0.0
        wins_24h = int(row[2]) if row else 0

        open_rows = conn.execute("""
            SELECT id, question, side, category, cost_usdc, end_date_iso
            FROM positions
            WHERE status = 'OPEN'
            ORDER BY end_date_iso ASC
        """).fetchall()

    now_dt = datetime.now(timezone.utc)
    upcoming_lines = []
    for r in open_rows[:4]:
        end_str = r["end_date_iso"]
        try:
            end_dt = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
            hours_left = max(0.0, (end_dt - now_dt).total_seconds() / 3600.0)
            time_label = f"через {hours_left:.0f}ч" if hours_left >= 1.0 else f"через {int(hours_left*60)} мин"
        except Exception:
            time_label = "скоро"
        short_q = r["question"][:40] + ("…" if len(r["question"]) > 40 else "")
        upcoming_lines.append(f"  • {short_q} (<b>{r['side']}</b>) — {time_label}")

    upcoming_text = "\n".join(upcoming_lines) if upcoming_lines else "  • Нет активных позиций"
    deals_label = _plural_deals(closed_count)
    win_rate_str = f" ({wins_24h}/{closed_count} побед)" if closed_count > 0 else ""

    date_title = now_dt.strftime("%d.%m.%Y")
    msg = (
        f"📊 <b>Дневной дайджест Polymarket ({date_title})</b>\n\n"
        f"💰 Баланс: <b>${total_equity:.2f} USDC</b> (За 24ч: <b>{pnl_24h:+.2f}$</b>)\n"
        f"🎯 Закрыто за сутки: <b>{deals_label}</b>{win_rate_str}\n"
        f"💼 В сделках: <b>${locked:.2f}</b> ({len(open_rows)}/8) | Кэш: <b>${cash:.2f}</b>\n\n"
        f"⏳ <b>Ближайшие исходы:</b>\n"
        f"{upcoming_text}"
    )

    sent = send_telegram_alert(msg)
    if sent:
        try:
            state_file.parent.mkdir(parents=True, exist_ok=True)
            state_file.write_text(json.dumps({"last_digest_date": today_utc}), encoding="utf-8")
        except Exception:
            pass
    return sent
