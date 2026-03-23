# 📦 Full Mode Step Sequence (20 Steps + Final Output)

> This file is the authoritative step definition for Full Mode. Loaded by the SKILL.md core dispatcher.

## Step Sequence

```
Phase 0: Prerequisites
  S1.  Opportunity Assessment + DHM → Read references/00-opportunity-check.md
  S2.  Strategy Blocks + Rumelt Strategy Kernel → Read references/01-strategy.md

Phase 1: Discovery
  S3.  Persona Table → Read references/02a-persona.md
  S4.  Persona Cards → Read references/02a-persona.md
  S5.  JTBD Analysis → Read references/02b-jtbd.md
  S6.  Opportunity Solution Tree (OST) → Read references/02c-ost-journey.md
  S7.  User Journey Map → Read references/02c-ost-journey.md

Phase 2: Define
  S8.  Pain Points Summary Table → Read references/03-define.md
  S9.  April Dunford Positioning → Read references/03-define.md
  S10. HMW Reframing → Read references/03-define.md
  S11. Opportunity Assessment Table → Read references/03-define.md

Phase 3: Develop
  S12. PR-FAQ → Read references/04a-prfaq.md
  S13. Parallel Prototypes → Read references/04b-solutions.md
  S14. Pre-mortem → Read references/04b-solutions.md
  S15. GEM + RICE Prioritization → Read references/04b-solutions.md
  S16. User Story → Read references/04b-solutions.md
  S17. MVP + Not Doing List → Read references/04c-mvp.md

Phase 4: Deliver
  S18. North Star + Three-Layer Signals + Aha Moment → Read references/05a-northstar-aha.md
  S19. PMF Level Assessment + GTM Strategy + Business Model → Read references/05b-pmf-gtm.md
  S20. Hypothesis Validation Plan → Read references/05c-validation-spec.md
────
Final Output → Product Spec Summary (references/05c-validation-spec.md → 4.6) + Best Entry Point Analysis
```

> In Full Mode, section 4.1 Empowered Teams is added before S18 when the target audience is executives or cross-functional teams; otherwise it is skipped.

## Reference Loading Instructions

When entering each step, only read the corresponding reference file (do not preload all files):

| Step | Reference File |
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
| S20 + Final Output | `references/05c-validation-spec.md` |

## Final Output Format

**Best Entry Point Analysis** (full logic chain) + **Product Spec Summary**

After completion, follow `references/rules-end-of-flow.md` to execute the end-of-flow rules.
