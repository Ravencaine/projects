---
created: 2026-07-27
source: "Stop Building Slow Power BI Reports: A Data Pro's Checklist"
source_url: "https://medium.com/@foodarchitects/stop-building-slow-power-bi-reports-a-data-pros-checklist-53990dbe770c"
note_type: atomic
tags: [power-bi, visualisation, performance, best-practices]
---

# Power BI Visual Performance

Visualisation complexity directly impacts report rendering time. Simple design choices at the visual level prevent the performance problems that schema-level optimisation cannot fix.

## Key Points

**Reduce visual count per page:**
- Every visual on a page fires its own DAX query when filters change
- 20 visuals × 2-second queries = potential 40 seconds of per-interaction latency
- Consolidate related metrics into fewer, multi-metric visuals where possible

**Avoid tables with millions of rows:**
- Matrix and Table visuals with high-cardinality columns load all matching rows
- Use aggregations, TOPN, or paginated reports (Power BI Report Builder) for large datasets

**Conditional formatting is expensive:**
- Background colour, font colour, and data bar rules re-evaluate per cell
- A 100-row × 10-column matrix with conditional formatting = 1,000 rule evaluations

**Dense scatter plots:**
- Scatter plots with many data points slow down rendering significantly
- Use tooltips or drillthrough instead of showing all points

**Complex maps:**
- Azure Maps and ESRI integrations have rendering overhead
- Use shape maps or simple filled maps for low-cardinality geographic data

**When in doubt, benchmark:**
- Power BI Performance Analyzer (built into Power BI Desktop) shows exact DAX query time per visual
- Use it before and after changes to confirm improvements

## Related

- [[column-pruning-bravo]] — model-level optimisation that helps all visuals
- [[import-vs-directquery-performance]] — storage mode impact on visual rendering
