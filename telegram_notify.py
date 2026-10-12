"""
Optional Telegram Notifier for Polymarket Paper-Trading Simulator.
Reads TELEGRAM_BOT_TOKEN and ALLOWED_CHAT_ID from environment or local `.env`
and sends instant alerts when virtual positions are opened, closed, resolved, or halted.
Uses pure Python standard library (`urllib.request`) — zero external dependencies required.
"""

import json
import os
import urllib.request
from pathlib import Path
from typing import Dict


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
