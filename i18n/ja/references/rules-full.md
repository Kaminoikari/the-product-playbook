# 📦 フルモード ステップ順序（20ステップ + 最終出力）

> このファイルはフルモードの正式なステップ定義です。SKILL.mdコアディスパッチャーにより読み込まれます。

## ステップ順序

```
Phase 0：前提条件
  S1.  機会評価 + DHM → references/00-opportunity-check.md を読み込み
  S2.  Strategy Blocks + Rumelt戦略の核心 → references/01-strategy.md を読み込み

Phase 1：ディスカバリー
  S3.  ペルソナ表 → references/02a-persona.md を読み込み
  S4.  ペルソナカード → references/02a-persona.md を読み込み
  S5.  JTBD分析 → references/02b-jtbd.md を読み込み
  S6.  Opportunity Solution Tree（OST） → references/02c-ost-journey.md を読み込み
  S7.  ユーザージャーニーマップ → references/02c-ost-journey.md を読み込み

Phase 2：Define
  S8.  ペインポイントサマリー表 → references/03-define.md を読み込み
  S9.  April Dunfordポジショニング → references/03-define.md を読み込み
  S10. HMWリフレーミング → references/03-define.md を読み込み
  S11. 機会評価表 → references/03-define.md を読み込み

Phase 3：Develop
  S12. PR-FAQ → references/04a-prfaq.md を読み込み
  S13. 並行プロトタイプ → references/04b-solutions.md を読み込み
  S14. Pre-mortem → references/04b-solutions.md を読み込み
  S15. GEM + RICE優先順位付け → references/04b-solutions.md を読み込み
  S16. User Story → references/04b-solutions.md を読み込み
  S17. MVP + Not Doing List → references/04c-mvp.md を読み込み

Phase 4：Deliver
  S18. North Star + 3層シグナル + Aha Moment → references/05a-northstar-aha.md を読み込み
  S19. PMFレベル評価 + GTM戦略 + ビジネスモデル → references/05b-pmf-gtm.md を読み込み
  S20. 仮説検証プラン → references/05c-validation-spec.md を読み込み
────
最終出力 → プロダクトスペックサマリー（references/05c-validation-spec.md → 4.6） + 最適エントリーポイント分析
```

> フルモードでは、ターゲットオーディエンスが経営層またはクロスファンクショナルチームの場合、S18の前にセクション4.1 Empowered Teamsを追加します；それ以外はスキップ。

## リファレンス読み込み指示

各ステップに入る時にのみ対応するリファレンスファイルを読み込みます（すべてのファイルを事前読み込みしない）：

| ステップ | リファレンスファイル |
|------|---------------|
| S1 | `references/00-opportunity-check.md` |
| S2 | `references/01-strategy.md` |
| S3-S4 | `references/02a-persona.md` |
| S5 | `references/02b-jtbd.md` |
| S6-S7 | `references/02c-ost-journey.md` |
| S8-S11 | `references/03-define.md` |
| S12 | `references/04a-prfaq.md` |
| S13-S16 | `references/04b-solutions.md` |
| S17 | `references/04c-mvp.md` |
| S18 | `references/05a-northstar-aha.md` |
| S19 | `references/05b-pmf-gtm.md` |
| S20 + 最終出力 | `references/05c-validation-spec.md` |

## 最終出力フォーマット

**最適エントリーポイント分析**（完全ロジックチェーン）+ **プロダクトスペックサマリー**

完了後、`references/rules-end-of-flow.md`に従ってエンドオブフロールールを実行してください。
