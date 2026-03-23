# 开发衔接 — 核心交接包

> 当使用者说「进入开发」「产出开发交接包」「帮我建专案」「接到 Claude Code」时触发。
> 读取此文件，整合整个产品规划流程的产出，生成可直接在 Claude Code CLI 中使用的开发交接包。

## 环境限制与衔接策略

**关键事实：Claude Chat / Cowork 和 Claude Code 是独立的运行环境，无法从 Chat 内直接启动 Claude Code。**

因此衔接策略是：**产出结构化的开发交接包（一组文件）**，使用者下载后放入专案数据夹，在 Claude Code 中一句话即可启动整个开发流程。

衔接方式视使用者环境而定：

| 使用者环境 | 衔接方式 |
|-----------|---------|
| **Claude Chat（Web/App）** | 产出 zip 档供下载，使用者解压到专案目录后开启 Claude Code |
| **Claude Cowork（Desktop）** | 同上，但可直接将文件写入使用者指定的本地路径 |
| **已在 Claude Code 中** | 直接在专案目录中建立所有文件（此情境下此 skill 多半由 CLAUDE.md 引用） |

---

## 开发交接包组成

产出以下文件组合，所有文件放在专案根目录：

```
[project-name]/
├── .gitignore             # 版控排除清单（.env、secrets、进度档等，模板见 references/07c-architecture-setup.md）
├── CLAUDE.md              # Claude Code 的专案记忆档：产品上下文 + 开发规范
├── TASKS.md               # 功能拆解 + Phase 分期 + 逐 Task 验收标准
├── TICKETS.md             # 开票内容：每张票的标题、描述、验收标准，PM 可直接开票
├── docs/
│   ├── PRD.md             # 完整 PRD（从 04-develop.md 产出格式整合）
│   ├── ARCHITECTURE.md    # 技术架构：目录结构 + DB schema + API endpoints + 安全架构
│   └── PRODUCT-SPEC.md    # 产品规格摘要（从 05-deliver.md → 4.6 整合）
└── scripts/
    └── setup.sh           # 一键初始化脚本（建立目录 + 安装 dependencies）
```

---

## 📄 CLAUDE.md 模板

CLAUDE.md 是 Claude Code 的专案记忆档，Claude Code 每次启动时会自动读取。必须包含：

```markdown
# [产品名称] — 专案指引

## 产品上下文

**一句话描述**：[PR-FAQ 标题]
**目标用户**：[Persona 一句话描述]
**核心 JTBD**：[Target Customer] 想要在 [Job Context] 完成 [Job]
**Aha Moment**：当用户完成 [行为]，他们体验到核心价值
**北极星指标**：[指标名称 + 定义]

## 技术栈

- **前端**：[框架 + 版本]
- **后端**：[框架 + 版本]
- **数据库**：[类型 + 版本]
- **部署**：[平台]
- **套件管理**：[工具]

## 开发规范

- 使用 [语言] 开发
- 遵循 [风格指南/lint 规则]
- commit message 格式：`[type]: [description]`（type: feat / fix / refactor / docs / test）
- 分支策略：[main / develop / feature-xxx]
- 每个功能必须有对应的 User Story 编号（见 TASKS.md）

## MVP 边界

**必须有（P0）**：
- [功能 1]
- [功能 2]
- [功能 3]

**明确不做**：
- [排除项 1] — 原因：[理由]
- [排除项 2] — 原因：[理由]

## 关键决策记录

| 决策 | 选择 | 理由 | 日期 |
|------|------|------|------|
| [例：数据库选择] | [PostgreSQL] | [需要关联查询 + JSON 支持] | [日期] |

## 风险警示（来自 Pre-mortem）

- ⚠️ [风险 1]：[预防措施]
- ⚠️ [风险 2]：[预防措施]

## 安全性备注

> 完整安全性检查清单见 `references/08-security-checklist.md`，以下为本产品的关键安全性决策：

- 认证方式：[JWT / Session / OAuth]
- CORS 政策：[允许的 Origins]
- Rate Limiting：[策略摘要]
- 敏感数据：[处理方式]

## 开发流程

请依照 `TASKS.md` 的 Phase 顺序逐步执行。每完成一个 Phase：
1. 确认所有 Task 的验收标准都通过
2. 询问使用者是否要进入下一个 Phase
3. 如果遇到架构问题，参考 `docs/ARCHITECTURE.md`
```

---

## 技术栈确认流程

产出开发交接包前，必须确认技术栈。如果使用者没有指定，依以下顺序询问：

### 必问（影响所有产出）

```
1. 这是什么类型的应用？
   □ Web App（浏览器）
   □ Mobile App（iOS / Android / 跨平台）
   □ Desktop App
   □ API / Backend Service
   □ CLI 工具
   □ 其他

2. 你有偏好的技术栈吗？
   （如果没有，我会根据产品特性推荐）
```

### 推荐逻辑（使用者没有指定时）

| 应用类型 | 推荐技术栈 | 推荐理由 |
|---------|-----------|---------|
| Web App（MVP 快速验证） | Next.js + Tailwind + Supabase | 全端一体、部署简单、内建 Auth |
| Web App（复杂后端逻辑） | React + Node.js/Express + PostgreSQL | 灵活性高、生态系成熟 |
| Web App（Python 团队） | React + FastAPI/Django + PostgreSQL | Python 生态系、Django 内建 Admin |
| Mobile App（跨平台） | React Native / Flutter | 单一 Codebase 覆盖双平台 |
| API Service | FastAPI / Express / Go | 轻量、高效能 |

> Claude 推荐时应说明理由，并提醒使用者可以覆盖推荐。

### 选填（根据产品需求追问）

```
3. 需要用户认证吗？（影响 Auth 方案选择）
4. 有即时性需求吗？（WebSocket / SSE）
5. 需要文件上传/处理吗？（影响 Storage 选择）
6. 预计部署在哪里？（Vercel / Railway / AWS / 自建）
```
