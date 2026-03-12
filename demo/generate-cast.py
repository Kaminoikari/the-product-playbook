#!/usr/bin/env python3
"""
Generate asciinema cast file from the demo script.
"""
import json

events = [
    # === 0.0s：Prompt 出現 ===
    (600, "\033[32m❯\033[0m "),

    # === 逐字輸入指令 ===
    (350, "/"),
    (90,  "p"),
    (75,  "r"),
    (80,  "o"),
    (75,  "d"),
    (80,  "u"),
    (75,  "c"),
    (80,  "t"),
    (75,  "-"),
    (80,  "b"),
    (75,  "u"),
    (80,  "i"),
    (75,  "l"),
    (80,  "d"),
    (220, " "),
    (120, "我想在現有電商系統加上即時通知功能"),

    # === Enter，啟動 ===
    (700, "\r\n"),
    (300, "\033[1m\033[35m⚡ 直接實作模式啟動中...\033[0m\r\n"),
    (400, "\033[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m\r\n"),

    # === 掃描 codebase ===
    (500, "\033[36m📂 掃描專案目錄...\033[0m\r\n"),
    (700, "   \033[32m✓\033[0m \033[34mpackage.json\033[0m         → Node.js 18 · Express 4.18 · PostgreSQL\r\n"),
    (800, "   \033[32m✓\033[0m \033[34mprisma/schema.prisma\033[0m → 偵測到 \033[33mUser\033[0m、\033[33mOrder\033[0m、\033[33mProduct\033[0m 資料表\r\n"),
    (700, "   \033[32m✓\033[0m \033[34msrc/api/routes/\033[0m      → 找到 12 個 REST endpoints\r\n"),
    (800, "   \033[32m✓\033[0m \033[34msrc/services/\033[0m        → WebSocket \033[31m✗ 尚未設定\033[0m\r\n"),
    (700, "   \033[32m✓\033[0m \033[34msrc/services/\033[0m        → 通知系統 \033[31m✗ 尚未設定\033[0m\r\n"),
    (500, "\r\n"),

    # === 技術棧摘要 ===
    (400, "\033[1m\033[36m🔍 技術棧確認\033[0m\r\n"),
    (350, "   框架      \033[33mExpress.js 4.18\033[0m\r\n"),
    (300, "   資料庫    \033[33mPostgreSQL via Prisma ORM\033[0m\r\n"),
    (300, "   即時通訊  \033[31m未建置\033[0m\r\n"),
    (300, "   通知系統  \033[31m未建置\033[0m\r\n"),
    (500, "\r\n"),

    # === 進度指示器 + S1 ===
    (400, "\033[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m\r\n"),
    (300, "\033[1m📍 直接實作模式  ｜  進度 S1 / S7\033[0m\r\n"),
    (250, "\033[32m▶️  S1：確認問題陳述\033[0m\033[90m（進行中）\033[0m\r\n"),
    (200, "\033[90m⬜ S2：PR-FAQ\033[0m\r\n"),
    (200, "\033[90m⬜ S3：平行解法\033[0m\r\n"),
    (200, "\033[90m⬜ S4：Pre-mortem（基於你的架構）\033[0m\r\n"),
    (200, "\033[90m⬜ S5：GEM + RICE 優先排序\033[0m\r\n"),
    (200, "\033[90m⬜ S6：MVP + Not Doing List\033[0m\r\n"),
    (200, "\033[90m⬜ S7：North Star + Aha Moment\033[0m\r\n"),
    (300, "\033[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m\r\n"),
    (600, "\r\n"),

    # === 第一個問題 ===
    (400, "根據掃描結果，你的系統目前有完整的 \033[33mUser ↔ Order\033[0m 關聯，\r\n"),
    (600, "但缺少 WebSocket 和推播機制。\r\n"),
    (700, "\r\n"),
    (500, "「即時通知」這個功能有幾個方向，我需要先確認邊界：\r\n"),
    (700, "\r\n"),
    (600, "  \033[1m\033[36m1️⃣  訂單狀態更新通知\033[0m（推播至前端 UI）\r\n"),
    (700, "  \033[1m\033[36m2️⃣  系統事件觸發通知\033[0m（Email / SMS）\r\n"),
    (700, "  \033[1m\033[36m3️⃣  兩者都要\033[0m，統一通知中樞\r\n"),
    (800, "\r\n"),
    (500, "\033[90m（輸入 1 / 2 / 3，或直接描述）\033[0m "),

    # === 等待游標 ===
    (3000, ""),
]

header = {
    "version": 2,
    "width": 88,
    "height": 30,
    "timestamp": 1741723200,
    "title": "claude — ~/my-ecommerce-project",
    "env": {"TERM": "xterm-256color", "SHELL": "/bin/zsh"}
}

output_lines = [json.dumps(header, ensure_ascii=False)]

current_time = 0.0
for delay_ms, content in events:
    current_time += delay_ms / 1000.0
    if content:  # skip empty content events
        event = [round(current_time, 3), "o", content]
        output_lines.append(json.dumps(event, ensure_ascii=False))

cast_content = "\n".join(output_lines) + "\n"

with open("demo/build-demo.cast", "w", encoding="utf-8") as f:
    f.write(cast_content)

print(f"Generated {len(output_lines)-1} events")
print(f"Total duration: {current_time:.2f}s")
print("Saved to demo/build-demo.cast")
