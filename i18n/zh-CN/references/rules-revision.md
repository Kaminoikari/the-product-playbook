# 🔄 改版模式步骤序列（共 12 步 + 最终产出）

> 此文件为改版模式的权威步骤定义。由 SKILL.md 核心派发载入。

## 步骤序列

```
Phase 0：现况分析
  S1.  既有产品现况回顾（用户数据概览 + 核心指标 + 已知问题 + 安全现况）
  S2.  现有用户 JTBD 重新检验（哪些 Job 做得好？哪些做不好？）

Phase 1：问题收敛
  S3.  用户痛点收集（留存/流失分析 + 用户反馈汇整 + 行为数据）
  S4.  痛点汇整表 → 读取 references/03-define.md → 2.1
  S5.  Positioning 重新评估 → 读取 references/03-define.md → 2.2（焦点：定位是否需要调整？）
  S6.  HMW 问题转化 → 读取 references/03-define.md → 2.3
  S7.  机会评估表 → 读取 references/03-define.md → 2.4

Phase 2：解法设计
  S8.  PR-FAQ → 读取 references/04a-prfaq.md（描述改版后的体验）
  S9.  Pre-mortem → 读取 references/04b-solutions.md → 3.3
  S10. MVP 范围 + Not Doing List → 读取 references/04c-mvp.md（焦点：改什么 / 不改什么）

Phase 3：验证
  S11. North Star + Aha Moment → 读取 references/05a-northstar-aha.md（比较改版前后指标）
  S12. 假设验证计划 → 读取 references/05c-validation-spec.md
────
最终产出 → 产品规格摘要（改版版）
```

### S1 前置：产品上下文载入

进入 S1 前，读取 `references/rules-context.md` 并检查 `.product-context.md`：

- **有完整上下文（情境 1）**：自动带入 PMF 等级、North Star、已知痛点、安全现况、近 3 笔 Decision History。S1 引导改为**差异式**：「上次评估时，你的 PMF 等级为 [X]，北极星指标为 [Y]。目前这些有变化吗？最新的 DAU/MAU 和留存率是多少？」— 已有的历史决策和已知痛点不需要重新收集
- **无上下文（情境 2）**：触发 Context Bootstrap（`rules-context.md` Section 4，Round 1 + 3），完成后再进入下方标准 S1 数据收集
- **部分上下文（情境 3）**：从 Decision History 带入功能变更历史（知道哪些模组被改过、有哪些风险被识别过），但需询问整体产品策略和指标（之前只做过功能扩充，缺全局视角）

### S1 标准引导

> 改版模式的 S1 会主动询问使用者提供既有产品数据：DAU/MAU、留存率、主要用户反馈、过去版本的关键决策等。若 context 已预填部分答案，改为确认而非重新收集。
> S1 同时收集安全现况：现有认证/授权机制、已知安全漏洞或技术债、近期安全事件。这些资讯会影响改版的风险评估和 Pre-mortem。

### 快速路径

当使用者在 S1 已提供充分数据（含用户反馈、指标、痛点），S4-S7（痛点→定位→HMW→机会评估）可在单次对话中连续产出，中间只需一次确认而非四次。触发条件：S3 收集到的痛点清单已有明确的优先级和数据支持。Hard Gate 规则不变 — 每个步骤的产出仍须完整呈现，只是确认节奏加快。

## Reference 载入指示

| 步骤 | Reference 文件 |
|------|---------------|
| S1-S3 | 无需外部 reference（直接引导使用者提供数据） |
| S4-S7 | `references/03-define.md` |
| S8 | `references/04a-prfaq.md` |
| S9 | `references/04b-solutions.md` |
| S10 | `references/04c-mvp.md` |
| S11 | `references/05a-northstar-aha.md` |
| S12 + 最终产出 | `references/05c-validation-spec.md` |

## 最终产出格式

**改版产品规格摘要**：改版前后对照 + 改什么/不改什么 + 成功指标

完成后，依 `references/rules-end-of-flow.md` 执行流程结束规则。
