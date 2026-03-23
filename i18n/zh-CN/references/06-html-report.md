# HTML 产品企划报告产出

当使用者说「产出报告」或确认最后一个阶段内容无误后触发。

## 设计规范

采用**现代设计风格**，单一 HTML 文件（CSS 与 JS 全部内嵌），确保离线也能阅读。

**整体风格：**
- 渐层背景的 Hero 区块（含执行模式、产出对象、日期标签）
- 卡片式排版（圆角 + 阴影），每个区块像是一张独立的资讯卡
- 清晰的字体层级和舒适的阅读间距
- 响应式设计，手机上也能顺畅阅读

**配色方案：**
- 主色调：深蓝系 `#1a1a2e` → `#16213e` → `#0f3460`
- 强调色：`#e94560` 或 `#533483`
- 内容区背景：`#f8f9fa`，卡片：白色带 `box-shadow`

**中文字体：** 优先从 Google Fonts CDN 载入 Noto Sans TC，失败时 fallback 到系统字体：
```css
/* 在 <head> 中加入 */
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">

/* CSS 中 */
font-family: "Noto Sans TC", system-ui, -apple-system, "Microsoft JhengHei", "PingFang TC", sans-serif;
```
> 这是唯一允许的外部 CDN 依赖。如果 Google Fonts 不可用，页面仍可正常显示。

## 页面结构（依已完成的阶段动态呈现）

```
┌──────────────────────────────────────────────────────────────┐
│  Hero 区块（产品名称、一句话描述、执行模式、产出对象、日期）       │
├──────────────────────────────────────────────────────────────┤
│  目录导航（Sticky，只显示已完成的区块）                          │
├──────────────────────────────────────────────────────────────┤
│  🧭 策略层区块（若有执行）                                       │
│     ├─ Strategy Blocks 层级图                                  │
│     ├─ Rumelt 好策略内核（诊断/方针/移动）                       │
│     └─ Shreyas 三层次产品工作                                   │
│  ✅ 机会评估区块（若有执行）                                     │
│  🔍 Discovery 区块（若有执行）                                   │
│     ├─ Persona Table（卡片式表格）                              │
│     ├─ Persona 卡片（每人一张）                                  │
│     ├─ JTBD 分析表（四种类型）                                   │
│     ├─ Opportunity Solution Tree（视觉化树状）                   │
│     └─ User Journey Map（概览表 + 手风琴详述）                  │
│  🎯 Define 区块（若有执行）                                      │
│     ├─ 痛点汇整表                                               │
│     ├─ April Dunford 定位框架卡片                               │
│     ├─ HMW 问题卡片（含 JTBD 类型标签）                          │
│     └─ 机会评估表（机会成本视角标注）                            │
│  💡 Develop 区块（若有执行）                                     │
│     ├─ PR-FAQ 卡片（模拟新闻稿格式）                             │
│     ├─ 解法发想（三栏平行方案卡片）                              │
│     ├─ Pre-mortem 风险表（高/中风险色彩标示）                    │
│     ├─ GEM 矩阵 + Impact/Effort 四象限图                        │
│     ├─ RICE 优先排序表（若有执行）                               │
│     ├─ User Story 表（若有执行）                                 │
│     └─ MVP 范围（三栏卡片 + Not Doing List）                    │
│  🚀 Deliver 区块（若有执行）                                     │
│     ├─ Aha Moment 定义卡片（醒目呈现）                          │
│     ├─ North Star Metric 卡片                                   │
│     ├─ 三层讯号指标表                                           │
│     ├─ PMF 等级判定（四级框架视觉化 + 目前位置标记）              │
│     ├─ GTM 策略（渠道选择 + 初始 100 位用户计划，若有执行）      │
│     ├─ 商业模式与定价（收费模式 + 定价策略，若有执行）            │
│     ├─ 假设验证计划表（若有执行）                               │
│     └─ 产品规格摘要（三区块结构：决策摘要 / 执行边界 / 深度参考）│
│  ⭐ 最佳切入点分析（完整逻辑链视觉化）                            │
├──────────────────────────────────────────────────────────────┤
│  页尾：产出日期 + 执行模式 + 框架来源说明                        │
└──────────────────────────────────────────────────────────────┘
```

## 各区块设计细节

**表格样式：** 斑马纹、深色表头、圆角、Hover 高亮

**Persona 卡片：** 每个 Persona 独立一张，痛点用红色左边框，JTBD 用蓝色/紫色色块强调

**Opportunity Solution Tree：** 用 CSS 或轻量 SVG 绘制树状结构，清楚呈现目标→机会→解法的层级关系

**PMF 等级图：** 用进度条或步骤图呈现四个等级，标注用户目前所在位置

**PR-FAQ 卡片：** 模拟新闻稿格式，有标题、副标题、引言，视觉上像真实文件

**Pre-mortem 风险表：** 高风险项目用红色警示，中风险用黄色

**最佳切入点逻辑链：** 视觉化完整推导链，每个节点一张小卡片，箭头连接

## 互动效果

- `scroll-behavior: smooth` — 目录点击平滑滚动
- Intersection Observer — 滚动时目录高亮当前区块
- 卡片 hover 微微上浮（`transform: translateY(-2px)` + `transition`）
- 手风琴展开/收合（User Journey Map 各阶段，`<details>/<summary>`）
- `@media print` — 打印时隐藏互动元素、确保表格不被截断

## 注意事项

- 所有 CSS 和 JS 内嵌在 HTML 中，除 Google Fonts CDN 载入 Noto Sans TC 外不依赖任何外部资源
- 如果某个阶段没有完成，不要放空白区块，直接跳过
- 页面 Hero 区块标明「执行模式」和「产出对象」，让阅读者一眼看到这份文件的定位
- 页面总长度可能很长，目录导航很重要，确保使用者能快速跳转

## 框架来源与延伸学习（放在页尾）

| 思想家 | 核心贡献 | 出处 |
|--------|---------|------|
| Teresa Torres | Continuous Discovery、Opportunity Solution Tree | Lenny's Podcast + 《Continuous Discovery Habits》 |
| Shreyas Doshi | LNO Framework、Pre-mortem、三层次产品工作、机会成本思维 | Lenny's Podcast Ep.3 |
| Gibson Biddle | DHM Model、GEM Prioritization | Lenny's Podcast |
| April Dunford | Positioning Framework | Lenny's Podcast + 《Obviously Awesome》 |
| Todd Jackson | 四级 PMF 框架、Four P's | Lenny's Podcast（First Round Capital） |
| Richard Rumelt | Good Strategy / Bad Strategy 好策略内核 | Lenny's Podcast + 《Good Strategy Bad Strategy》 |
| Marty Cagan | Empowered Teams、Product Discovery | Lenny's Podcast + 《Inspired》《Empowered》 |
| Chandra Janakiraman | Strategy Blocks | Lenny's Newsletter（Headspace / Meta） |
| Clayton Christensen | Jobs to Be Done | 《Competing Against Luck》 |
| Amazon | Working Backwards / PR-FAQ | 《Working Backwards》 |
| Sean Ellis | Sean Ellis Score、ICE Scoring | 《Hacking Growth》 |
| Lenny Rachitsky | Shape / Ship / Synchronize、North Star 思维 | Lenny's Newsletter + Podcast |
