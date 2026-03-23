# 产品策略层

> **注意：各模式应执行哪些步骤，以 SKILL.md 中「各模式步骤序列」为权威定义。以下仅供参考。**

**适用于：完整模式、高完整性、产出对象为老板/跨部门对齐**
**可跳过：快速模式、直接实作模式、低完整性**

## Strategy Blocks（Chandra Janakiraman / Headspace / Meta）

好策略的层级结构，从上到下每一层都是下一层的基础：

```
Mission（使命）
  └→ Vision（愿景）— 5-10 年后你希望世界变成什么样？
       └→ Strategy（策略）— 你如何达到那个愿景？（关键选择和取舍）
            └→ Goals / OKRs（目标）— 接下来 6-12 个月的优先事项
                 └→ Roadmap（路线图）— 具体要做什么？
                      └→ Tasks（任务）— 谁做什么、何时完成？
```

## Richard Rumelt 的「好策略内核（Kernel of Good Strategy）」

- **诊断（Diagnosis）**：清楚定义你面临的挑战（不是所有问题，而是最关键的那个）
- **指导方针（Guiding Policy）**：你的整体应对方向（不是目标，而是方法）
- **连贯移动（Coherent Actions）**：相互强化的具体移动，而不是各自独立的计划

> 坏策略的特征：只有宏大目标、没有诊断；用漂亮的措辞掩盖思维的空洞；把所有计划都称为「策略」。

## Shreyas Doshi 的三层次产品工作

在处理任何产品问题时，先确认你在哪个层次工作：

```
Level 3：Product Excellence（卓越执行）— 把正确的事情做得非常好
Level 2：Product Strategy（产品策略）— 做正确的事情
Level 1：Product Foundation（产品根基）— 有能力做事情的基础（文化、流程、人才）
```

> 大多数 PM 花太多时间在 Level 3，却忽略了 Level 2 的问题。大多数所谓的「执行问题」，追根究底都是「策略问题」。

## Shreyas Doshi 的 LNO 时间分配框架

每周的工作项目，先问：这件事对产品的影响属于哪一类？

```
L（Leverage，高杠杆）：策略、愿景、文化 → 投入充足时间，精益求精
N（Neutral，中性）：一般协作、普通沟通 → 做好即可，不必追求完美
O（Overhead，负担）：行政、会议、文书 → 尽快完成，不要过度投入
```

> 把节省下来的 O 时间，投入到被忽视的 L 工作中。

## OKR 撰写指引

Strategy Blocks 中 Goals/OKRs 是策略往下展开的关键层。写好 OKR 的最小规则：

**Objective（目标）**：定性、有激励性、可理解。描述一个你想达到的状态，不是一个待办事项。
- ✅ 好的 O：「让新用户在第一天就感受到产品核心价值」
- ❌ 坏的 O：「完成 Onboarding 改版」（这是任务不是目标）

**Key Results（关键结果）**：定量、可衡量、有时限。描述你如何知道自己达到了目标。
- ✅ 好的 KR：「新用户 D1 核心动作完成率从 20% 提升到 40%」
- ❌ 坏的 KR：「上线新版 Onboarding 流程」（这是 Output 不是 Outcome）

**常见陷阱：**
- 把任务清单伪装成 OKR（「完成 X 功能」不是 KR）
- OKR 太多（每季 2-3 个 Objective，每个 O 下 3-5 个 KR）
- KR 之间相互矛盾或不相关
- 只有滞后指标（Lagging），没有领先指标（Leading）

**范例：**
```
O：让目标用户爱上我们的产品（PMF Level 2 → Level 3）
  KR1：D28 留存率从 12% → 20%
  KR2：Sean Ellis Score 从 28% → 40%
  KR3：每月自然推荐新增用户占比从 10% → 25%
```

## 产品核心三问（贯穿整个流程）

这三个问题必须依序厘清，**顺序不可对调**：

> **Q1：如何吸引顾客进来？（How to get people in the front door?）**
> **Q2：如何最快让他们感受到「哇啊！」？（How to reach the Aha Moment?）**
> **Q3：如何高频率地传递出产品的核心价值？（How to deliver core value repeatedly?）**

在 Define 阶段，具体转化为：
- **Who is it for?** — 为谁做的？
- **Why build it?** — 为什么要做？
- **What is it?** — 做什么？
