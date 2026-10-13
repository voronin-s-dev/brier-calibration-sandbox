"""
Trigger GitHub Actions workflow via REST API / Webhook (Pure Python 3.12, 0 dependencies).
Usage:
    py trigger_cloud.py                      # Uses GITHUB_TOKEN from .env if present
    py trigger_cloud.py <YOUR_GITHUB_TOKEN>  # Passes token directly as argument
"""

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO_OWNER = "voronin-s-dev"
REPO_NAME = "brier-calibration-sandbox"
WORKFLOW_FILE = "sync.yml"
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/{WORKFLOW_FILE}/dispatches"
ACTIONS_URL = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/actions"


def load_token_from_env() -> str:
    env_path = Path(__file__).resolve().parent / ".env"
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("GITHUB_TOKEN=") or line.startswith("GITHUB_PAT="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    return os.getenv("GITHUB_TOKEN") or os.getenv("GITHUB_PAT") or ""


def trigger_workflow(token: str, cycles: int = 3, interval: int = 540) -> bool:
    if not token:
        print("❌ Ошибка: GitHub Token не найден!")
        print("Укажите токен аргументом: py trigger_cloud.py ghp_your_token")
        print("Или добавьте строку в .env: GITHUB_TOKEN=ghp_your_token")
        return False

    payload = {
        "ref": "main",
        "inputs": {
            "cycles": str(cycles),
            "interval": str(interval)
        }
    }
    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "Polymarket-Cloud-Trigger",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    print(f"📡 Отправка вебхук-запроса в GitHub Actions...")
    print(f"🎯 URL: {API_URL}")
    print(f"⚙️ Параметры: cycles={cycles}, interval={interval}s")

    try:
        with urllib.request.urlopen(req) as resp:
            status = resp.status
            if status in (200, 201, 204):
                print(f"✅ УСПЕХ! (HTTP {status}) — Запуск инициирован мгновенно.")
                print(f"🔗 Следить за выполнением можно здесь:")
                print(f"   {ACTIONS_URL}")
                return True
            else:
                print(f"⚠️ Неожиданный ответ сервера: HTTP {status}")
                return False
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Ошибка {e.code}: {e.reason}")
        try:
            err_body = e.read().decode("utf-8")
            print(f"Детали ошибки от GitHub:\n{err_body}")
        except Exception:
            pass
        if e.code == 401:
            print("\n💡 Подсказка: Токен недействителен или истек.")
        elif e.code == 403:
            print("\n💡 Подсказка: У токена нет разрешения 'workflow' или 'repo'.")
        elif e.code == 404:
            print("\n💡 Подсказка: Проверьте имя репозитория или файл воркфлоу.")
        return False
    except Exception as e:
        print(f"❌ Сетевая ошибка: {e}")
        return False


if __name__ == "__main__":
    cli_token = sys.argv[1] if len(sys.argv) > 1 else load_token_from_env()
    trigger_workflow(cli_token)
