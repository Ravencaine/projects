---
created: 2026-08-02
updated: 2026-08-05
source: Why a Waterfall Chart is a Diagnostic Tool, Not Just a Dashboard Decoration
note_type: pattern
tags: [powerbi, pattern, data-visualization, waterfall-chart, diagnostic, drill-down, constraint]
---

# Waterfall Diagnostic Playbook: Largest Downward Bar = Constraint; Drill-Down by Segment/Cohort

The waterfall's diagnostic power comes from making the *mechanism* visible — not just the net result.

**Finding the constraint:** The largest downward bar in a waterfall is the constraint. It is not noise — it is the leverage point. If you only fix the top of the funnel while churn erases gains, you stay on a treadmill. Fixing retention makes the same sales effort compound.

**Drill-down playbook:**
1. Identify the largest downward block (e.g., $3.6M in cancellations)
2. Name and quantify the constraint explicitly
3. Break that single brick open into a second waterfall — segmented by cohort, segment, or reason code
4. The second-level waterfall reveals whether the problem is concentrated (one segment) or distributed

**Example:** Top-level waterfall shows SMB = ~50% of total churn. Drill-down waterfall by segment confirms SMB onboarding is the constraint. Concrete playbook: audit the SMB onboarding process. Not vague "improve retention."

**Design principle:** The diagnostic waterfall teaches you how to act. A vague insight ("we lost a lot to churn") is not a plan. A quantified, segmented insight ("SMB cohort lost $1.8M, Enterprise is stable") is a plan.

**Rule:** Waterfall → identify constraint → drill down by one dimension → repeat until the action is specific and segmented.
