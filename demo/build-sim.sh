#!/bin/bash
# Simulates /product-build command output for demo GIF

sleep 0.3
printf "\033[1m\033[35m⚡ 直接實作模式啟動中...\033[0m\n"
sleep 0.4
printf "\033[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m\n"

sleep 0.5
printf "\033[36m📂 掃描專案目錄...\033[0m\n"
sleep 0.7
printf "   \033[32m✓\033[0m \033[34mpackage.json\033[0m         → Node.js 18 · Express 4.18 · PostgreSQL\n"
sleep 0.8
printf "   \033[32m✓\033[0m \033[34mprisma/schema.prisma\033[0m → 偵測到 \033[33mUser\033[0m、\033[33mOrder\033[0m、\033[33mProduct\033[0m 資料表\n"
sleep 0.7
printf "   \033[32m✓\033[0m \033[34msrc/api/routes/\033[0m      → 找到 12 個 REST endpoints\n"
sleep 0.8
printf "   \033[32m✓\033[0m \033[34msrc/services/\033[0m        → WebSocket \033[31m✗ 尚未設定\033[0m\n"
sleep 0.7
printf "   \033[32m✓\033[0m \033[34msrc/services/\033[0m        → 通知系統 \033[31m✗ 尚未設定\033[0m\n"
printf "\n"

sleep 0.4
printf "\033[1m\033[36m🔍 技術棧確認\033[0m\n"
sleep 0.35
printf "   框架      \033[33mExpress.js 4.18\033[0m\n"
sleep 0.3
printf "   資料庫    \033[33mPostgreSQL via Prisma ORM\033[0m\n"
sleep 0.3
printf "   即時通訊  \033[31m未建置\033[0m\n"
sleep 0.3
printf "   通知系統  \033[31m未建置\033[0m\n"
printf "\n"

sleep 0.4
printf "\033[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m\n"
sleep 0.3
printf "\033[1m📍 直接實作模式  ｜  進度 S1 / S7\033[0m\n"
sleep 0.25
printf "\033[32m▶️  S1：確認問題陳述\033[0m\033[90m（進行中）\033[0m\n"
sleep 0.2
printf "\033[90m⬜ S2：PR-FAQ\033[0m\n"
sleep 0.2
printf "\033[90m⬜ S3：平行解法\033[0m\n"
sleep 0.2
printf "\033[90m⬜ S4：Pre-mortem（基於你的架構）\033[0m\n"
sleep 0.2
printf "\033[90m⬜ S5：GEM + RICE 優先排序\033[0m\n"
sleep 0.2
printf "\033[90m⬜ S6：MVP + Not Doing List\033[0m\n"
sleep 0.2
printf "\033[90m⬜ S7：North Star + Aha Moment\033[0m\n"
sleep 0.3
printf "\033[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m\n"
sleep 0.6
printf "\n"

sleep 0.4
printf "根據掃描結果，你的系統目前有完整的 \033[33mUser ↔ Order\033[0m 關聯，\n"
sleep 0.6
printf "但缺少 WebSocket 和推播機制。\n"
sleep 0.7
printf "\n"
sleep 0.5
printf "「即時通知」這個功能有幾個方向，我需要先確認邊界：\n"
sleep 0.7
printf "\n"
sleep 0.6
printf "  \033[1m\033[36m1️⃣  訂單狀態更新通知\033[0m（推播至前端 UI）\n"
sleep 0.7
printf "  \033[1m\033[36m2️⃣  系統事件觸發通知\033[0m（Email / SMS）\n"
sleep 0.7
printf "  \033[1m\033[36m3️⃣  兩者都要\033[0m，統一通知中樞\n"
sleep 0.8
printf "\n"
sleep 0.5
printf "\033[90m（輸入 1 / 2 / 3，或直接描述）\033[0m "

# Hold cursor here until VHS stops recording
sleep 5
