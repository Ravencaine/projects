---
created: 2026-08-02
updated: 2026-08-05
source: Why a Waterfall Chart is a Diagnostic Tool, Not Just a Dashboard Decoration
note_type: pattern
tags: [powerbi, pattern, data-visualization, waterfall-chart, use-cases]
---

# Waterfall Use Cases + Constraints: When to Use, When to Skip

**Use waterfall when:**
- **Build-up:** showing how smaller pieces add up to a total market size
- **Movement over time:** bridging headcount or revenue from January to December
- **Diagnosing a gap:** missed or beat a target; need to show exactly which categories drove the difference

**Skip waterfall when:**
- Just comparing final values — the journey doesn't matter → simple bar chart
- Too many tiny drivers — more than ~10 steps makes the chart unreadable → group into "Other" or switch chart type
- Factors are independent and don't naturally sum to a total → horizontal dot plot instead
- Comparing multiple groups → waterfall is single-story; use small multiples grid
- Volatility is the story → waterfall shows net change only, hides swings within the period → line chart for temporal variability, waterfall as attribution summary

**Key constraint:** A waterfall is an additive contract. The steps must reconcile exactly to the net change. If they don't, fix the underlying model — don't try to fix it with formatting.
