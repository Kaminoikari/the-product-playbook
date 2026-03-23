# ✏️ カスタムモード ステップ順序

> このファイルはカスタムモードの正式なステップ定義です。SKILL.mdコアディスパッチャーにより読み込まれます。

ユーザーが選択した完成度レベルに基づく：

## 🔴 低（リーン）— 4ステップ

```
S1. JTBD statement → references/02b-jtbd.md を読み込み
S2. 1つのHMW → references/03-define.md → 2.3 を読み込み
S3. PR-FAQ → references/04a-prfaq.md を読み込み
S4. North Star → references/05a-northstar-aha.md を読み込み
（各ステップはユーザーの希望で別のフレームワークに入れ替え可能）
────
最終出力 → プロダクトスペックサマリー（未実行フィールドは「未実行」と記載）
```

## 🟡 中（スタンダード）— 10ステップ

```
S1.  ペルソナ表 + ペルソナカード → references/02a-persona.md を読み込み
S2.  JTBD分析 → references/02b-jtbd.md を読み込み
S3.  ペインポイントサマリー表 → references/03-define.md を読み込み
S4.  HMW質問リフレーミング → references/03-define.md を読み込み
S5.  April Dunfordポジショニング → references/03-define.md を読み込み
S6.  PR-FAQ → references/04a-prfaq.md を読み込み
S7.  並行ソリューション + MVP + Not Doing List → references/04b-solutions.md + references/04c-mvp.md を読み込み
S8.  North Star + 3層シグナル + Aha Moment → references/05a-northstar-aha.md を読み込み
S9.  PMFレベル評価 → references/05b-pmf-gtm.md を読み込み
S10. プロダクトスペックサマリー → references/05c-validation-spec.md を読み込み
```

## 🟢 高（包括的）— 16ステップ

```
S1.  Strategy Blocks + Rumelt → references/01-strategy.md を読み込み
S2.  ペルソナ表 + ペルソナカード → references/02a-persona.md を読み込み
S3.  JTBD分析 → references/02b-jtbd.md を読み込み
S4.  OST Opportunity Solution Tree → references/02c-ost-journey.md を読み込み
S5.  ユーザージャーニーマップ → references/02c-ost-journey.md を読み込み
S6.  ペインポイントサマリー表 → references/03-define.md を読み込み
S7.  HMW + April Dunfordポジショニング → references/03-define.md を読み込み
S8.  機会評価表 → references/03-define.md を読み込み
S9.  PR-FAQ → references/04a-prfaq.md を読み込み
S10. 並行プロトタイプ → references/04b-solutions.md を読み込み
S11. Pre-mortem → references/04b-solutions.md を読み込み
S12. GEM + RICE → references/04b-solutions.md を読み込み
S13. MVP + Not Doing List → references/04c-mvp.md を読み込み
S14. North Star + 3層シグナル + Aha Moment → references/05a-northstar-aha.md を読み込み
S15. 仮説検証プラン → references/05c-validation-spec.md を読み込み
S16. プロダクトスペックサマリー → references/05c-validation-spec.md を読み込み
```

## リファレンス読み込みルール

各ステップに入る時にのみ対応するリファレンスファイルを読み込みます（すべてのファイルを事前読み込みしない）。上記の各ステップにリファレンスパスが注記されています。

## 最終出力フォーマット

**プロダクトスペックサマリー**（完了したステップのみ統合；未実行フィールドは「未実行」と記載）

完了後、`references/rules-end-of-flow.md`に従ってエンドオブフロールールを実行してください。
