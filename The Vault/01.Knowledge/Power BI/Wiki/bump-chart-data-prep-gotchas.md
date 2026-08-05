---
created: 2026-08-02
source: What Bump Charts Tell You That Line Charts Hide
note_type: gotcha
tags: [powerbi, gotcha, data-visualization, bump-chart, rank, tie, missing-data, prep]
---

# Bump Chart Data Prep Gotchas: Tie-Breaking, Missing Periods, Uneven Time Intervals

Building a bump chart in Power BI (via Rankx in DAX or a calculated column) requires explicit rules for edge cases — otherwise the visual silently misleads.

**1. Define the ranking variable before anything else.**
Rank is meaningless without a specific metric. Define exactly which measure drives the rank (e.g., total sales, revenue, margin).

**2. Rank within each time period — RANKX must be scoped correctly.**
`RANKX(ALLSELECTED(table[Period]), [Measure])` — without the correct filter context, RANKX computes globally and the visual is wrong. Recalculate rank per period so each column (week/month/quarter) has its own ordering.

**3. Tie-breaking rules must be explicit and documented.**
Standard ranking designs assume a clean ladder. Ties create overlapping lines that hide each other. Document how ties are resolved: alphabetical, previous-rank order, or shared rank. Without this, identical values silently produce invisible lines.

**4. Missing periods should break the line, not fake continuity.**
If a category drops out and re-enters later, breaking the line is the honest choice. Interpolated continuity implies observations that do not exist. Power BI: use conditional visibility or a separate series for gaps.

**5. Uneven time intervals need honest treatment.**
Do not space quarterly and monthly data points equally on the X-axis without explanation — it distorts the reading of velocity. Either use a continuous date axis or explicitly annotate uneven spacing.

**Common stumbling blocks to check before publishing:**
- Rank 1 is at the **bottom** of the Y-axis (wrong — should be at top)
- Too many equally-emphasized lines (no highlight hierarchy)
- Disconnected legend instead of direct labels
- Ties left unhandled (overlapping invisible lines)
- Using a bump chart when the raw magnitude gap is the actual story
