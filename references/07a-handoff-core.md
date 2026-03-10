# 開發銜接 — 核心交接包

> 當使用者說「進入開發」「產出開發交接包」「幫我建專案」「接到 Claude Code」時觸發。
> 讀取此檔案，整合整個產品規劃流程的產出，生成可直接在 Claude Code CLI 中使用的開發交接包。

## 環境限制與銜接策略

**關鍵事實：Claude Chat / Cowork 和 Claude Code 是獨立的運行環境，無法從 Chat 內直接啟動 Claude Code。**

因此銜接策略是：**產出結構化的開發交接包（一組檔案）**，使用者下載後放入專案資料夾，在 Claude Code 中一句話即可啟動整個開發流程。

銜接方式視使用者環境而定：

| 使用者環境 | 銜接方式 |
|-----------|---------|
| **Claude Chat（Web/App）** | 產出 zip 檔供下載，使用者解壓到專案目錄後開啟 Claude Code |
| **Claude Cowork（Desktop）** | 同上，但可直接將檔案寫入使用者指定的本地路徑 |
| **已在 Claude Code 中** | 直接在專案目錄中建立所有檔案（此情境下此 skill 多半由 CLAUDE.md 引用） |

---

## 開發交接包組成

產出以下檔案組合，所有檔案放在專案根目錄：

```
[project-name]/
├── CLAUDE.md              # Claude Code 的專案記憶檔：產品上下文 + 開發規範
├── TASKS.md               # 功能拆解 + Phase 分期 + 逐 Task 驗收標準
├── TICKETS.md             # 開票內容：每張票的標題、描述、驗收標準，PM 可直接開票
├── docs/
│   ├── PRD.md             # 完整 PRD（從 04-develop.md 產出格式整合）
│   ├── ARCHITECTURE.md    # 技術架構：目錄結構 + DB schema + API endpoints
│   └── PRODUCT-SPEC.md    # 產品規格摘要（從 05-deliver.md → 4.6 整合）
└── scripts/
    └── setup.sh           # 一鍵初始化腳本（建立目錄 + 安裝 dependencies）
```

---

## 📄 CLAUDE.md 模板

CLAUDE.md 是 Claude Code 的專案記憶檔，Claude Code 每次啟動時會自動讀取。必須包含：

```markdown
# [產品名稱] — 專案指引

## 產品上下文

**一句話描述**：[PR-FAQ 標題]
**目標用戶**：[Persona 一句話描述]
**核心 JTBD**：[Target Customer] 想要在 [Job Context] 完成 [Job]
**Aha Moment**：當用戶完成 [行為]，他們體驗到核心價值
**北極星指標**：[指標名稱 + 定義]

## 技術棧

- **前端**：[框架 + 版本]
- **後端**：[框架 + 版本]
- **資料庫**：[類型 + 版本]
- **部署**：[平台]
- **套件管理**：[工具]

## 開發規範

- 使用 [語言] 開發
- 遵循 [風格指南/lint 規則]
- commit message 格式：`[type]: [description]`（type: feat / fix / refactor / docs / test）
- 分支策略：[main / develop / feature-xxx]
- 每個功能必須有對應的 User Story 編號（見 TASKS.md）

## MVP 邊界

**必須有（P0）**：
- [功能 1]
- [功能 2]
- [功能 3]

**明確不做**：
- [排除項 1] — 原因：[理由]
- [排除項 2] — 原因：[理由]

## 關鍵決策記錄

| 決策 | 選擇 | 理由 | 日期 |
|------|------|------|------|
| [例：資料庫選擇] | [PostgreSQL] | [需要關聯查詢 + JSON 支援] | [日期] |

## 風險警示（來自 Pre-mortem）

- ⚠️ [風險 1]：[預防措施]
- ⚠️ [風險 2]：[預防措施]

## 開發流程

請依照 `TASKS.md` 的 Phase 順序逐步執行。每完成一個 Phase：
1. 確認所有 Task 的驗收標準都通過
2. 詢問使用者是否要進入下一個 Phase
3. 如果遇到架構問題，參考 `docs/ARCHITECTURE.md`
```

---

## 技術棧確認流程

產出開發交接包前，必須確認技術棧。如果使用者沒有指定，依以下順序詢問：

### 必問（影響所有產出）

```
1. 這是什麼類型的應用？
   □ Web App（瀏覽器）
   □ Mobile App（iOS / Android / 跨平台）
   □ Desktop App
   □ API / Backend Service
   □ CLI 工具
   □ 其他

2. 你有偏好的技術棧嗎？
   （如果沒有，我會根據產品特性推薦）
```

### 推薦邏輯（使用者沒有指定時）

| 應用類型 | 推薦技術棧 | 推薦理由 |
|---------|-----------|---------|
| Web App（MVP 快速驗證） | Next.js + Tailwind + Supabase | 全端一體、部署簡單、內建 Auth |
| Web App（複雜後端邏輯） | React + Node.js/Express + PostgreSQL | 靈活性高、生態系成熟 |
| Web App（Python 團隊） | React + FastAPI/Django + PostgreSQL | Python 生態系、Django 內建 Admin |
| Mobile App（跨平台） | React Native / Flutter | 單一 Codebase 覆蓋雙平台 |
| API Service | FastAPI / Express / Go | 輕量、高效能 |

> Claude 推薦時應說明理由，並提醒使用者可以覆蓋推薦。

### 選填（根據產品需求追問）

```
3. 需要用戶認證嗎？（影響 Auth 方案選擇）
4. 有即時性需求嗎？（WebSocket / SSE）
5. 需要檔案上傳/處理嗎？（影響 Storage 選擇）
6. 預計部署在哪裡？（Vercel / Railway / AWS / 自建）
```
