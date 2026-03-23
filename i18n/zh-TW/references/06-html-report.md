# HTML 產品企劃報告產出

當使用者說「產出報告」或確認最後一個階段內容無誤後觸發。

## 設計規範

採用**現代設計風格**，單一 HTML 檔案（CSS 與 JS 全部內嵌），確保離線也能閱讀。

**整體風格：**
- 漸層背景的 Hero 區塊（含執行模式、產出對象、日期標籤）
- 卡片式排版（圓角 + 陰影），每個區塊像是一張獨立的資訊卡
- 清晰的字體層級和舒適的閱讀間距
- 響應式設計，手機上也能順暢閱讀

**配色方案：**
- 主色調：深藍系 `#1a1a2e` → `#16213e` → `#0f3460`
- 強調色：`#e94560` 或 `#533483`
- 內容區背景：`#f8f9fa`，卡片：白色帶 `box-shadow`

**中文字體：** 優先從 Google Fonts CDN 載入 Noto Sans TC，失敗時 fallback 到系統字體：
```css
/* 在 <head> 中加入 */
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">

/* CSS 中 */
font-family: "Noto Sans TC", system-ui, -apple-system, "Microsoft JhengHei", "PingFang TC", sans-serif;
```
> 這是唯一允許的外部 CDN 依賴。如果 Google Fonts 不可用，頁面仍可正常顯示。

## 頁面結構（依已完成的階段動態呈現）

```
┌──────────────────────────────────────────────────────────────┐
│  Hero 區塊（產品名稱、一句話描述、執行模式、產出對象、日期）       │
├──────────────────────────────────────────────────────────────┤
│  目錄導航（Sticky，只顯示已完成的區塊）                          │
├──────────────────────────────────────────────────────────────┤
│  🧭 策略層區塊（若有執行）                                       │
│     ├─ Strategy Blocks 層級圖                                  │
│     ├─ Rumelt 好策略內核（診斷/方針/行動）                       │
│     └─ Shreyas 三層次產品工作                                   │
│  ✅ 機會評估區塊（若有執行）                                     │
│  🔍 Discovery 區塊（若有執行）                                   │
│     ├─ Persona Table（卡片式表格）                              │
│     ├─ Persona 卡片（每人一張）                                  │
│     ├─ JTBD 分析表（四種類型）                                   │
│     ├─ Opportunity Solution Tree（視覺化樹狀）                   │
│     └─ User Journey Map（概覽表 + 手風琴詳述）                  │
│  🎯 Define 區塊（若有執行）                                      │
│     ├─ 痛點彙整表                                               │
│     ├─ April Dunford 定位框架卡片                               │
│     ├─ HMW 問題卡片（含 JTBD 類型標籤）                          │
│     └─ 機會評估表（機會成本視角標注）                            │
│  💡 Develop 區塊（若有執行）                                     │
│     ├─ PR-FAQ 卡片（模擬新聞稿格式）                             │
│     ├─ 解法發想（三欄平行方案卡片）                              │
│     ├─ Pre-mortem 風險表（高/中風險色彩標示）                    │
│     ├─ GEM 矩陣 + Impact/Effort 四象限圖                        │
│     ├─ RICE 優先排序表（若有執行）                               │
│     ├─ User Story 表（若有執行）                                 │
│     └─ MVP 範圍（三欄卡片 + Not Doing List）                    │
│  🚀 Deliver 區塊（若有執行）                                     │
│     ├─ Aha Moment 定義卡片（醒目呈現）                          │
│     ├─ North Star Metric 卡片                                   │
│     ├─ 三層訊號指標表                                           │
│     ├─ PMF 等級判定（四級框架視覺化 + 目前位置標記）              │
│     ├─ GTM 策略（渠道選擇 + 初始 100 位用戶計畫，若有執行）      │
│     ├─ 商業模式與定價（收費模式 + 定價策略，若有執行）            │
│     ├─ 假設驗證計畫表（若有執行）                               │
│     └─ 產品規格摘要（三區塊結構：決策摘要 / 執行邊界 / 深度參考）│
│  ⭐ 最佳切入點分析（完整邏輯鏈視覺化）                            │
├──────────────────────────────────────────────────────────────┤
│  頁尾：產出日期 + 執行模式 + 框架來源說明                        │
└──────────────────────────────────────────────────────────────┘
```

## 各區塊設計細節

**表格樣式：** 斑馬紋、深色表頭、圓角、Hover 高亮

**Persona 卡片：** 每個 Persona 獨立一張，痛點用紅色左邊框，JTBD 用藍色/紫色色塊強調

**Opportunity Solution Tree：** 用 CSS 或輕量 SVG 繪製樹狀結構，清楚呈現目標→機會→解法的層級關係

**PMF 等級圖：** 用進度條或步驟圖呈現四個等級，標注用戶目前所在位置

**PR-FAQ 卡片：** 模擬新聞稿格式，有標題、副標題、引言，視覺上像真實文件

**Pre-mortem 風險表：** 高風險項目用紅色警示，中風險用黃色

**最佳切入點邏輯鏈：** 視覺化完整推導鏈，每個節點一張小卡片，箭頭連接

## 互動效果

- `scroll-behavior: smooth` — 目錄點擊平滑滾動
- Intersection Observer — 滾動時目錄高亮當前區塊
- 卡片 hover 微微上浮（`transform: translateY(-2px)` + `transition`）
- 手風琴展開/收合（User Journey Map 各階段，`<details>/<summary>`）
- `@media print` — 列印時隱藏互動元素、確保表格不被截斷

## 注意事項

- 所有 CSS 和 JS 內嵌在 HTML 中，除 Google Fonts CDN 載入 Noto Sans TC 外不依賴任何外部資源
- 如果某個階段沒有完成，不要放空白區塊，直接跳過
- 頁面 Hero 區塊標明「執行模式」和「產出對象」，讓閱讀者一眼看到這份文件的定位
- 頁面總長度可能很長，目錄導航很重要，確保使用者能快速跳轉

## 框架來源與延伸學習（放在頁尾）

| 思想家 | 核心貢獻 | 出處 |
|--------|---------|------|
| Teresa Torres | Continuous Discovery、Opportunity Solution Tree | Lenny's Podcast + 《Continuous Discovery Habits》 |
| Shreyas Doshi | LNO Framework、Pre-mortem、三層次產品工作、機會成本思維 | Lenny's Podcast Ep.3 |
| Gibson Biddle | DHM Model、GEM Prioritization | Lenny's Podcast |
| April Dunford | Positioning Framework | Lenny's Podcast + 《Obviously Awesome》 |
| Todd Jackson | 四級 PMF 框架、Four P's | Lenny's Podcast（First Round Capital） |
| Richard Rumelt | Good Strategy / Bad Strategy 好策略內核 | Lenny's Podcast + 《Good Strategy Bad Strategy》 |
| Marty Cagan | Empowered Teams、Product Discovery | Lenny's Podcast + 《Inspired》《Empowered》 |
| Chandra Janakiraman | Strategy Blocks | Lenny's Newsletter（Headspace / Meta） |
| Clayton Christensen | Jobs to Be Done | 《Competing Against Luck》 |
| Amazon | Working Backwards / PR-FAQ | 《Working Backwards》 |
| Sean Ellis | Sean Ellis Score、ICE Scoring | 《Hacking Growth》 |
| Lenny Rachitsky | Shape / Ship / Synchronize、North Star 思維 | Lenny's Newsletter + Podcast |
