# HTMLプロダクト企画レポート出力

ユーザーが「レポートを作成して」と言った時、または最終ステージの内容が正しいと確認した時にトリガーされます。

## デザイン仕様

**モダンデザインスタイル**を使用 — 単一HTMLファイル（CSSとJSは完全インライン）で、オフラインでの閲覧を保証。

**全体スタイル：**
- グラデーション背景のHeroセクション（モード、オーディエンス、日付ラベル付き）
- カードベースレイアウト（角丸 + シャドウ）、各セクションが独立した情報カード
- 明確なタイポグラフィ階層と快適な読み込み間隔
- レスポンシブデザイン、モバイルでもスムーズな閲覧

**配色：**
- プライマリ：ディープブルー `#1a1a2e` → `#16213e` → `#0f3460`
- アクセント：`#e94560` または `#533483`
- コンテンツエリア背景：`#f8f9fa`、カード：白に `box-shadow`

**フォント：** Google Fonts CDNからNoto Sans JPを最優先で読み込み、システムフォントにフォールバック：
```css
/* <head>内 */
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap');

/* CSS内 */
font-family: "Noto Sans JP", "Hiragino Sans", system-ui, -apple-system, sans-serif;
```
> これが唯一許可される外部CDN依存です。Google Fontsが利用できなくても、ページは正しくレンダリングされます。

## ページ構造（完了済みステージに基づいて動的レンダリング）

```
┌──────────────────────────────────────────────────────────────┐
│  Heroセクション（プロダクト名、ワンライナー、モード、オーディエンス、日付）│
├──────────────────────────────────────────────────────────────┤
│  目次ナビゲーション（Sticky、完了済みのみ表示）                    │
├──────────────────────────────────────────────────────────────┤
│  🧭 戦略セクション（完了している場合）                            │
│     ├─ Strategy Blocks階層図                                  │
│     ├─ Rumeltの良い戦略の核心（診断/方針/行動）                  │
│     └─ Shreyasのプロダクトワーク3レベル                         │
│  ✅ 機会チェックセクション（完了している場合）                     │
│  🔍 ディスカバリーセクション（完了している場合）                   │
│     ├─ ペルソナ表（カードスタイルテーブル）                      │
│     ├─ ペルソナカード（ペルソナごとに1枚）                      │
│     ├─ JTBD分析表（4タイプ）                                   │
│     ├─ Opportunity Solution Tree（ビジュアルツリー）             │
│     └─ ユーザージャーニーマップ（概要 + アコーディオン詳細）       │
│  🎯 Defineセクション（完了している場合）                         │
│     ├─ ペインポイントサマリー表                                 │
│     ├─ April Dunfordポジショニングフレームワークカード             │
│     ├─ HMW質問カード（JTBDタイプタグ付き）                      │
│     └─ 機会評価表（機会コストビュー）                           │
│  💡 Developセクション（完了している場合）                        │
│     ├─ PR-FAQカード（模擬プレスリリースフォーマット）             │
│     ├─ ソリューション構想（3列並行カード）                      │
│     ├─ Pre-mortemリスク表（高/中リスクを色分け）                 │
│     ├─ GEMマトリクス + Impact/Effort象限チャート                │
│     ├─ RICE優先順位表（完了している場合）                       │
│     ├─ ユーザーストーリー表（完了している場合）                   │
│     └─ MVPスコープ（3列カード + Not Doing List）                │
│  🚀 Deliverセクション（完了している場合）                        │
│     ├─ Aha Moment定義カード（目立つ表示）                       │
│     ├─ North Star Metricカード                                 │
│     ├─ 3層シグナルメトリクス表                                  │
│     ├─ PMFレベル評価（4レベルビジュアル + 現在位置マーカー）     │
│     ├─ GTM戦略（チャネル選択 + 最初の100ユーザープラン、         │
│     │  完了している場合）                                       │
│     ├─ ビジネスモデル＆プライシング（収益モデル + プライシング    │
│     │  戦略、完了している場合）                                  │
│     ├─ 仮説検証プラン表（完了している場合）                     │
│     └─ プロダクトスペックサマリー（3セクション構造：             │
│        意思決定サマリー / 実行境界 / ディープリファレンス）        │
│  ⭐ 最適エントリーポイント分析（完全ロジックチェーンビジュアル）   │
├──────────────────────────────────────────────────────────────┤
│  フッター：出力日 + モード + フレームワーク出典                    │
└──────────────────────────────────────────────────────────────┘
```

## セクションデザイン詳細

**テーブルスタイリング：** ゼブラストライプ、ダークヘッダー、角丸、ホバーハイライト

**ペルソナカード：** ペルソナごとに1カード、ペインポイントは赤い左ボーダー、JTBDは青/紫のカラーブロックで強調

**Opportunity Solution Tree：** CSSまたは軽量SVGでツリー構造を描画、Goal → Opportunity → Solutionの階層を明確に表示

**PMFレベルチャート：** プログレスバーまたはステップダイアグラムで4レベルを表示、ユーザーの現在位置をマーク

**PR-FAQカード：** 模擬プレスリリースフォーマット（見出し、サブタイトル、リード段落）— 実際のドキュメントに見えるように

**Pre-mortemリスク表：** 高リスク項目は赤いアラート、中リスクは黄色

**最適エントリーポイントロジックチェーン：** 完全な推論チェーンを可視化、各ノードを小さなカードとし、矢印で接続

## インタラクティブエフェクト

- `scroll-behavior: smooth` — 目次クリック時のスムーズスクロール
- Intersection Observer — スクロール中に目次の現在のセクションをハイライト
- カードホバー時の微小リフト（`transform: translateY(-2px)` + `transition`）
- アコーディオン展開/折りたたみ（ユーザージャーニーマップのステージ、`<details>/<summary>`）
- `@media print` — 印刷時にインタラクティブ要素を非表示、テーブルが切れないことを保証

## 重要な注意事項

- すべてのCSSとJSはHTML内にインライン — Google Fonts CDNのNoto Sans JP以外に外部依存なし
- 完了していないステージは空セクションをレンダリングしない — スキップする
- HeroセクションにはModerとAudienceを表示し、読者がドキュメントのコンテキストをすぐに理解できるように
- ページは非常に長くなる可能性がある — 目次ナビゲーションはクイックジャンプに不可欠

## フレームワーク出典＆参考文献（フッター）

| ソートリーダー | 主要貢献 | ソース |
|---------|-----------------|--------|
| Teresa Torres | Continuous Discovery、Opportunity Solution Tree | Lenny's Podcast + *Continuous Discovery Habits* |
| Shreyas Doshi | LNOフレームワーク、Pre-mortem、プロダクトワーク3レベル、機会コスト思考 | Lenny's Podcast Ep.3 |
| Gibson Biddle | DHMモデル、GEM優先順位付け | Lenny's Podcast |
| April Dunford | ポジショニングフレームワーク | Lenny's Podcast + *Obviously Awesome* |
| Todd Jackson | 4段階PMFフレームワーク、Four P's | Lenny's Podcast（First Round Capital） |
| Richard Rumelt | 良い戦略 / 悪い戦略、良い戦略の核心 | Lenny's Podcast + *Good Strategy Bad Strategy* |
| Marty Cagan | Empowered Teams、Product Discovery | Lenny's Podcast + *Inspired*、*Empowered* |
| Chandra Janakiraman | Strategy Blocks | Lenny's Newsletter（Headspace / Meta） |
| Clayton Christensen | Jobs to Be Done | *Competing Against Luck* |
| Amazon | Working Backwards / PR-FAQ | *Working Backwards* |
| Sean Ellis | Sean Ellis Score、ICE Scoring | *Hacking Growth* |
| Lenny Rachitsky | Shape / Ship / Synchronize、North Star Thinking | Lenny's Newsletter + Podcast |
