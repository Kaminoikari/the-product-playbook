# Phase 1: Discovery — JTBD Analysis

## 1.3 JTBD (Jobs to Be Done) Analysis

> "The unit of analysis is not the consumer, but the job the consumer is trying to get done." — Clayton Christensen

**JTBD Statement Formula:**
```
[Target customer] + wants to, in [what job context] + get [what job] done
```

Example: A first-time homebuyer comparing mortgage options wants to quickly estimate monthly payments late at night when they can't reach a bank, so they can walk their partner through their financial plan.

**JTBD Four-Type Analysis Table:**

```
| JTBD Type | Definition | Persona 1 | Persona 2 |
|-----------|------------|-----------|-----------|
| Functional Job | Completing a specific task or achieving a functional goal | | |
| Emotional Job | How they feel or want to feel | | |
| Social Job | How they want to be perceived by others | | |
| Job Context | Under what circumstances they need to get this job done | | |
```

**JTBD Deep-Dive Five Questions:**
1. **Root Problem**: Behind what users express as their need, what are they really trying to solve?
2. **Current Constraints**: What solutions have been ruled out due to certain limitations?
3. **Current Workarounds**: How are users coping today? What workarounds have they built?
4. **Gap**: Where do current workarounds fall short? (This gap is your opportunity)
5. **Ideal Solution**: If constraints were removed, what would their ideal solution look like?

**Teresa Torres User Interview Best Practices:**
- Focus on users' **actual past behavior**, not hypothetical future behavior
- Ask "Last time you ran into this problem, what did you do?" instead of "What features would you like?"
- Most common mistakes: asking hypothetical questions, introducing solution bias, not probing for details

### 📝 JTBD Quality Checklist

Claude must self-check after producing JTBD output (each item must be marked ✅ or ❌; ❌ items must include how to improve):
- [ ] Does it include a specific context? (Not "anytime, anywhere" — but "late at night when they can't reach a bank")
- [ ] Does it focus on a single core job? (Not three jobs crammed into one sentence)
- [ ] Are functional, emotional, and social jobs all identified?
- [ ] Can it be used to evaluate "Does this solution actually address this job?"
- [ ] Does it include "current workarounds" and "gap"? (Gap = opportunity)
- [ ] Does Q5 of the Deep-Dive reach emotional motivation / professional identity / psychological fear? (Not just functional descriptions)

**Execution Rules (Hard Gate):**
- Must mark each item ✅ or ❌ — blank [ ] or unexplained ✅ lists are not allowed
- If all items are ✅, must additionally state "What is the weakest part of this analysis and how to strengthen it"
- ❌ Common issues: too abstract, too many jobs merged, missing context, substituting product features for job descriptions, Q5 staying at the functional level

---

### 🏢 B2B Product Deep-Dive Requirements

**B2B products (including B2B2C) must complete the following analysis:**

#### Organizational-Level Job Analysis (Required — cover at least 2 levels)

| Level | Description | Examples |
|-------|-------------|----------|
| **Strategic Job** | Cross-departmental needs at the org/management level | Compliance audits, cost control, workforce optimization |
| **Operational Job** | Coordination needs at the process/department manager level | Approval workflow management, cross-team information sync |
| **Task Job** | Day-to-day operational needs of individual users | Filling out forms, checking status, exporting reports |

#### Buyer vs. User Analysis (Required)

If the buyer and user are different people, analyze their JTBD separately:
- **Buyer Job**: Jobs that influence the purchasing decision (ROI justification, risk reduction, compliance requirements)
- **User Job**: Jobs that need to get done during daily operations (efficiency gains, error reduction)
- If they are the same person, explain "why the decision-maker is also the user in this scenario"

#### Deep-Dive Five Questions — B2B Enhanced Version

**Q5 must reach at least one of the following levels** (examples):
- ✅ Professional identity: "She's afraid of looking incompetent in front of leadership, because this report represents her department's credibility"
- ✅ Emotional motivation: "He wants to demonstrate to his direct reports that he has a firm grasp of the numbers"
- ✅ Psychological fear: "Her biggest fear is the auditor catching a process gap — she was already warned once before"
- ❌ Failing example: "He needs a better tool to improve efficiency" (stays at the functional level)

#### Competitive Alternatives Analysis (Required)

List the alternatives users are actually using today:
- At least 2 named existing tools (e.g., Slack / Excel / paper forms / email / verbal communication)
- For each tool, explain its "fundamental flaw": not that the features are weak, but "why this flaw has been accepted and left unsolved" (organizational inertia? switching costs? leadership doesn't care?)

### 📋 User Interview Plan Template

```
## User Interview Plan

**Research Goal**: Understand how [target Persona] deals with [specific problem] in [Job Context]
**Screening Criteria**:
  - Must have experienced [specific behavior] within the past [X days/weeks]
  - Exclude: [who is not a fit — e.g., internal employees, known power users]

**Core Questions (5–7)**:
1. Last time you ran into [problem], can you walk me through how you handled it? (Behavioral recall)
2. During that process, what was the most frustrating or time-consuming part? (Pain point identification)
3. Have you tried other approaches? Why or why not? (Current alternatives)
4. If that part could be better, what would "better" look like to you? (Ideal state)
5. How often does this happen? When was the last time? (Frequency and urgency)
6. Besides you, who else is affected by this problem? (Stakeholder mapping)
7. On a scale of 1–10, how severe is this problem for you? Why? (Quantifying the pain)

**Follow-up Strategies**:
  - When the interviewee says "Usually I..." → Ask "What specifically happened last time?"
  - When the interviewee mentions an emotion → Ask "Can you describe that feeling more specifically?"
  - When the interviewee mentions a tool/method → Ask "What made you choose that approach?"

**Documentation Format**:
  - Verbatim transcript or recording
  - Within 24 hours post-interview, tag: key quotes / pain points / surprising findings / contradictions to assumptions
```

---

## 📎 File Integration Notes for This Phase

If the user uploads files during this phase, Claude integrates them as follows:

| Uploaded Content | Integrate Into | Integration Action |
|-----------------|----------------|-------------------|
| User interview transcripts / recording text | 1.1 Persona + 1.3 JTBD | Extract: user background → Persona fields; pain points + current workarounds → JTBD Deep-Dive Five Questions; emotional reactions → Emotional / Social Jobs |
| Competitor app screenshots | 1.3 JTBD (current workarounds) | Identify as user's "current alternative," analyze workarounds and gaps |
