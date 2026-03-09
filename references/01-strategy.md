# 產品策略層

> **注意：各模式應執行哪些步驟，以 SKILL.md 中「各模式步驟序列」為權威定義。以下僅供參考。**

**適用於：完整模式、高完整性、產出對象為老闆/跨部門對齊**
**可跳過：快速模式、直接實作模式、低完整性**

## Strategy Blocks（Chandra Janakiraman / Headspace / Meta）

好策略的層級結構，從上到下每一層都是下一層的基礎：

```
Mission（使命）
  └→ Vision（願景）— 5-10 年後你希望世界變成什麼樣？
       └→ Strategy（策略）— 你如何達到那個願景？（關鍵選擇和取捨）
            └→ Goals / OKRs（目標）— 接下來 6-12 個月的優先事項
                 └→ Roadmap（路線圖）— 具體要做什麼？
                      └→ Tasks（任務）— 誰做什麼、何時完成？
```

## Richard Rumelt 的「好策略內核（Kernel of Good Strategy）」

- **診斷（Diagnosis）**：清楚定義你面臨的挑戰（不是所有問題，而是最關鍵的那個）
- **指導方針（Guiding Policy）**：你的整體應對方向（不是目標，而是方法）
- **連貫行動（Coherent Actions）**：相互強化的具體行動，而不是各自獨立的計畫

> 壞策略的特徵：只有宏大目標、沒有診斷；用漂亮的措辭掩蓋思維的空洞；把所有計畫都稱為「策略」。

## Shreyas Doshi 的三層次產品工作

在處理任何產品問題時，先確認你在哪個層次工作：

```
Level 3：Product Excellence（卓越執行）— 把正確的事情做得非常好
Level 2：Product Strategy（產品策略）— 做正確的事情
Level 1：Product Foundation（產品根基）— 有能力做事情的基礎（文化、流程、人才）
```

> 大多數 PM 花太多時間在 Level 3，卻忽略了 Level 2 的問題。大多數所謂的「執行問題」，追根究底都是「策略問題」。

## Shreyas Doshi 的 LNO 時間分配框架

每週的工作項目，先問：這件事對產品的影響屬於哪一類？

```
L（Leverage，高槓桿）：策略、願景、文化 → 投入充足時間，精益求精
N（Neutral，中性）：一般協作、普通溝通 → 做好即可，不必追求完美
O（Overhead，負擔）：行政、會議、文書 → 盡快完成，不要過度投入
```

> 把節省下來的 O 時間，投入到被忽視的 L 工作中。

## OKR 撰寫指引

Strategy Blocks 中 Goals/OKRs 是策略往下展開的關鍵層。寫好 OKR 的最小規則：

**Objective（目標）**：定性、有激勵性、可理解。描述一個你想達到的狀態，不是一個待辦事項。
- ✅ 好的 O：「讓新用戶在第一天就感受到產品核心價值」
- ❌ 壞的 O：「完成 Onboarding 改版」（這是任務不是目標）

**Key Results（關鍵結果）**：定量、可衡量、有時限。描述你如何知道自己達到了目標。
- ✅ 好的 KR：「新用戶 D1 核心動作完成率從 20% 提升到 40%」
- ❌ 壞的 KR：「上線新版 Onboarding 流程」（這是 Output 不是 Outcome）

**常見陷阱：**
- 把任務清單偽裝成 OKR（「完成 X 功能」不是 KR）
- OKR 太多（每季 2-3 個 Objective，每個 O 下 3-5 個 KR）
- KR 之間相互矛盾或不相關
- 只有滯後指標（Lagging），沒有領先指標（Leading）

**範例：**
```
O：讓目標用戶愛上我們的產品（PMF Level 2 → Level 3）
  KR1：D28 留存率從 12% → 20%
  KR2：Sean Ellis Score 從 28% → 40%
  KR3：每月自然推薦新增用戶佔比從 10% → 25%
```

## 產品核心三問（貫穿整個流程）

這三個問題必須依序釐清，**順序不可對調**：

> **Q1：如何吸引顧客進來？（How to get people in the front door?）**
> **Q2：如何最快讓他們感受到「哇啊！」？（How to reach the Aha Moment?）**
> **Q3：如何高頻率地傳遞出產品的核心價值？（How to deliver core value repeatedly?）**

在 Define 階段，具體轉化為：
- **Who is it for?** — 為誰做的？
- **Why build it?** — 為什麼要做？
- **What is it?** — 做什麼？
