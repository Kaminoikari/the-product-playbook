# ✏️ Custom Mode Step Sequence

> This file is the authoritative step definition for Custom Mode. Loaded by the SKILL.md core dispatcher.

Based on the user's selected completeness level:

## 🔴 Low (Lean) — 4 Steps

```
S1. JTBD statement → load references/02b-jtbd.md
S2. One HMW → load references/03-define.md → 2.3
S3. PR-FAQ → load references/04a-prfaq.md
S4. North Star → load references/05a-northstar-aha.md
(Any step can be swapped by the user for a different framework)
────
Final Output → Product spec summary (unexecuted fields marked "Not executed")
```

## 🟡 Medium (Standard) — 10 Steps

```
S1.  Persona Table + Persona Card → load references/02a-persona.md
S2.  JTBD Analysis → load references/02b-jtbd.md
S3.  Pain Point Summary Table → load references/03-define.md
S4.  HMW Question Reframing → load references/03-define.md
S5.  April Dunford Positioning → load references/03-define.md
S6.  PR-FAQ → load references/04a-prfaq.md
S7.  Parallel Solutions + MVP + Not Doing List → load references/04b-solutions.md + references/04c-mvp.md
S8.  North Star + Three-Layer Signals + Aha Moment → load references/05a-northstar-aha.md
S9.  PMF Level Assessment → load references/05b-pmf-gtm.md
S10. Product Spec Summary → load references/05c-validation-spec.md
```

## 🟢 High (Comprehensive) — 16 Steps

```
S1.  Strategy Blocks + Rumelt → load references/01-strategy.md
S2.  Persona Table + Persona Card → load references/02a-persona.md
S3.  JTBD Analysis → load references/02b-jtbd.md
S4.  OST Opportunity Solution Tree → load references/02c-ost-journey.md
S5.  User Journey Map → load references/02c-ost-journey.md
S6.  Pain Point Summary Table → load references/03-define.md
S7.  HMW + April Dunford Positioning → load references/03-define.md
S8.  Opportunity Assessment Table → load references/03-define.md
S9.  PR-FAQ → load references/04a-prfaq.md
S10. Parallel Prototypes → load references/04b-solutions.md
S11. Pre-mortem → load references/04b-solutions.md
S12. GEM + RICE → load references/04b-solutions.md
S13. MVP + Not Doing List → load references/04c-mvp.md
S14. North Star + Three-Layer Signals + Aha Moment → load references/05a-northstar-aha.md
S15. Hypothesis Validation Plan → load references/05c-validation-spec.md
S16. Product Spec Summary → load references/05c-validation-spec.md
```

## Reference Loading Rules

When entering each step, only load the corresponding reference file (do not pre-load all files). Each step above has its reference path annotated.

## Final Output Format

**Product Spec Summary** (only integrates completed steps; unexecuted fields are marked "Not executed")

Upon completion, execute end-of-flow rules per `references/rules-end-of-flow.md`.
