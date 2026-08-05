---
created: 2026-07-29
updated: 2026-08-02
source: "The 3–30–300 Rule That Changed The Way I Build Dashboards.md" · [[Author-Md-Mizanur-Rahman-Nayan]]"
note_type: atomic
tags: [dashboard-design, information-density, UX, time-budget]
related: [Data-Narratives-Report-Design, Visual-Information-Seeking-Mantira]
---

# The 3-30-300 Rule (Dashboard Design)

A UX design heuristic borrowed from urban planning that allocates a user's time budget when reading a dashboard.

## The Framework

| Tier | Time | Purpose |
|------|------|---------|
| **3 seconds** | What is the headline? | Overview — can the user immediately see the key metric or status? |
| **30 seconds** | What is the context and trend? | Exploration — can the user understand patterns, comparisons, and changes? |
| **300 seconds** | Why is this happening? | Analysis — can the user drill into root causes? |

## Application in Power BI

### 3 Seconds — The Overview Page

- Dominant KPI card or scorecard at the top.
- Traffic light status indicators (green/amber/red) visible immediately.
- No interaction required to understand the page.
- Single question answered: "Are we on track?"

### 30 Seconds — The Exploration Page

- Trend charts (line, area) with contextual annotations.
- Comparison against target (color-coded bars).
- Filter panel visible for quick slicing.
- Multiple perspectives (product, region, time) without scrolling.
- Single question answered: "What changed and where?"

### 300 Seconds — The Detail Page

- Drill-through pages or detail tables.
- Cross-join of dimensions for root cause analysis.
- Ability to export data for further investigation.
- Links to source data or underlying reports.
- Single question answered: "Why did this happen?"

## Design Principles Derived from the Rule

- **Page 1 = Overview**: never require scrolling; never require interaction to read.
- **Page 2 = Context**: assume the user is now engaged; show comparisons and trends.
- **Page 3 = Detail**: assume the user is committed; provide full data access.
- Each page should be **answerable in its allocated time budget**.

## Notes

- The rule is a heuristic, not a law — some reports may need only 3-second pages; others may skip the detail page.
- Bittar applies this framework to all her client dashboard projects, particularly HR and financial dashboards.
- [[Data-Narratives-Report-Design]] provides the 7-step process that implements this rule in practice.
- [[Visual-Information-Seeking-Mantira]] provides the per-visual equivalent of the 3-30-300 idea.

## Related

- [[Data-Narratives-Report-Design]] — 7-step process implementing this rule
- [[Visual-Information-Seeking-Mantira]] — visual design framework
- [[Accessibility-for-Charts]] — accessibility applies across all three tiers
