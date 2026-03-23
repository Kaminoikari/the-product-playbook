# 🔄 Revision Mode Step Sequence (12 Steps + Final Output)

> This file is the authoritative step definition for Revision Mode. Loaded by the SKILL.md core dispatcher.

## Step Sequence

```
Phase 0: Current State Analysis
  S1.  Existing product review (user data overview + core metrics + known issues + security status)
  S2.  Re-examine existing user JTBD (which jobs are being done well? which aren't?)

Phase 1: Problem Convergence
  S3.  User pain point collection (retention/churn analysis + user feedback synthesis + behavioral data)
  S4.  Pain point summary table → load references/03-define.md → 2.1
  S5.  Positioning re-evaluation → load references/03-define.md → 2.2 (focus: does positioning need adjustment?)
  S6.  HMW question reframing → load references/03-define.md → 2.3
  S7.  Opportunity assessment table → load references/03-define.md → 2.4

Phase 2: Solution Design
  S8.  PR-FAQ → load references/04a-prfaq.md (describe the post-revision experience)
  S9.  Pre-mortem → load references/04b-solutions.md → 3.3
  S10. MVP scope + Not Doing List → load references/04c-mvp.md (focus: what to change / what not to change)

Phase 3: Validation
  S11. North Star + Aha Moment → load references/05a-northstar-aha.md (compare pre- vs. post-revision metrics)
  S12. Hypothesis validation plan → load references/05c-validation-spec.md
────
Final Output → Product spec summary (revision edition)
```

### S1 Pre-step: Product Context Loading

Before entering S1, load `references/rules-context.md` and check `.product-context.md`:

- **Full context available (Scenario 1)**: Auto-populate PMF level, North Star, known pain points, security status, and the 3 most recent Decision History entries. S1 guidance switches to **delta mode**: "Last time we assessed, your PMF level was [X] and your North Star metric was [Y]. Has anything changed? What are the latest DAU/MAU and retention numbers?" — Previously collected decision history and known pain points do not need to be re-gathered.
- **No context available (Scenario 2)**: Trigger Context Bootstrap (`rules-context.md` Section 4, Round 1 + 3), then proceed to standard S1 data collection below.
- **Partial context (Scenario 3)**: Pull in feature change history from Decision History (know which modules were changed and what risks were identified), but ask about overall product strategy and metrics (previous work only covered feature expansion and lacks a holistic view).

### S1 Standard Guidance

> Revision Mode's S1 proactively asks the user to provide existing product data: DAU/MAU, retention rates, key user feedback, past version decisions, etc. If context already pre-fills some answers, confirm rather than re-collect.
> S1 also collects current security status: existing auth/authorization mechanisms, known security vulnerabilities or tech debt, recent security incidents. This information affects the revision's risk assessment and Pre-mortem.

### Fast Path

When the user provides sufficient data at S1 (including user feedback, metrics, and pain points), S4–S7 (pain points → positioning → HMW → opportunity assessment) can be produced in a single conversation turn, requiring only one confirmation instead of four. Trigger condition: the pain point list gathered in S3 already has clear prioritization and data support. Hard Gate rules remain unchanged — each step's output must still be fully presented; only the confirmation cadence is accelerated.

## Reference Loading Instructions

| Step | Reference File |
|------|---------------|
| S1–S3 | No external reference needed (guide the user to provide data directly) |
| S4–S7 | `references/03-define.md` |
| S8 | `references/04a-prfaq.md` |
| S9 | `references/04b-solutions.md` |
| S10 | `references/04c-mvp.md` |
| S11 | `references/05a-northstar-aha.md` |
| S12 + Final Output | `references/05c-validation-spec.md` |

## Final Output Format

**Revision Product Spec Summary**: Before/after comparison + what to change / what not to change + success metrics

Upon completion, execute end-of-flow rules per `references/rules-end-of-flow.md`.
