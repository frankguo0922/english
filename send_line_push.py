import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

import requests


LINE_PUSH_URL = "https://api.line.me/v2/bot/message/push"


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        print(f"Missing required environment variable: {name}", file=sys.stderr)
        sys.exit(1)
    return value


def build_message() -> str:
    tz = ZoneInfo("Asia/Taipei")
    now = datetime.now(tz)
    date_str = now.strftime("%Y-%m-%d (%a)")

    return "\n".join(
        [
            f"📌 英文打卡提醒｜{date_str}",
            "1) 🎧 聽力+跟讀 15 分鐘（shadowing）",
            "2) 🗣️ 口說 15 分鐘：用英文講今天做了什麼 + 研究進度",
            "3) 📄 閱讀 10–15 分鐘：論文 Intro/Related Work 抓『問題/方法/貢獻』",
            "4) 🧠 單字 5–10 分鐘：記 3 個句子（不要背表）",
            "",
            "✅ 回覆我：用英文 1–2 分鐘講你今天做了什麼（可錄音/打字都行）",
        ]
    )


def push_message(token: str, user_id: str, message: str) -> None:
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {
        "to": user_id,
        "messages": [{"type": "text", "text": message}],
    }

    try:
        resp = requests.post(LINE_PUSH_URL, headers=headers, json=payload, timeout=20)
    except requests.RequestException as e:
        print(f"HTTP request failed: {e}", file=sys.stderr)
        sys.exit(1)

    if resp.status_code >= 400:
        # LINE often returns JSON error details; print raw text for debugging.
        print(f"LINE push failed: {resp.status_code}", file=sys.stderr)
        print(resp.text, file=sys.stderr)
        sys.exit(1)

    print("OK: pushed message")


def main() -> None:
    token = require_env("LINE_CHANNEL_ACCESS_TOKEN")
    user_id = require_env("LINE_USER_ID")
    message = build_message()
    push_message(token, user_id, message)


if __name__ == "__main__":
    main()
