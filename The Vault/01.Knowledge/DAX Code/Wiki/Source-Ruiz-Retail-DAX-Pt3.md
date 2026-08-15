---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 3
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-3-f152d1b500b5
note_type: source
tags: [dax, retail, production, goals, time-intelligence, best-practices]
---

# Source: Ruiz — Retail DAX Measures Pt 3

> **Type:** article (Part 3 of a series)
> **Author:** Jesse Ruiz (she/they)
> **Published:** 2026-08-03
> **URL:** https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-3-f152d1b500b5
> **Routed to:** DAX Code
> **Category:** DAX, Retail Analytics, Production Targets, Best Practices

## Summary

Final part of the Jesse Ruiz three-part DAX retail analytics series. Covers dynamic goal selection via `SELECTEDVALUE` (detecting day/month/year granularity), range targets for custom date slicers, `STARTOFMONTH` for monthly target anchoring, five common DAX pitfalls (circular dependencies, implicit measures, division by zero, wrong context in iterators, NUMERIC vs AnyRef), sell-through rate pattern, KPI card clean display with `" - "` for blank, and a matrix with multiple variance levels (Day, MTD, YTD, YoY).

## Key Claims

1. **SELECTEDVALUE cascade:** nested `IF(SELECTEDVALUE(date), daily, IF(SELECTEDVALUE(month), monthly, annual))` selects the right target for the current granularity
2. **STARTOFMONTH:** anchors CALCULATE to the first of the month regardless of which day is selected — needed when targets are stored as one row per month
3. **Range targets:** `CALCULATE(SUM(daily_targets))` sums daily targets across a custom date range
4. **Five pitfalls:** circular dependencies (self-reference), implicit vs explicit measures, DIVIDE vs /, wrong context in iterators (need CALCULATE inside SUMX), NUMERIC vs AnyRef for UDFs
5. **KPI cards:** `IF(ISBLANK(val), " - ", val)` for clean blank display
6. **Sell-through rate:** `DIVIDE(COUNT(Sales), COUNT(Production))` filtered by CatGroup; returns BLANK when production = 0

## Series Summary (All 3 Parts)

| Part | Topics |
|------|--------|
| Pt 1 | Measures vs columns, filter/row context, budget variance, VAR/RETURN, DIVIDE, BLANK vs 0 |
| Pt 2 | TOTALMTD, TOTALYTD, SAMEPERIODLASTYEAR, ALL vs ALLSELECTED, DATESBETWEEN, inventory aging buckets, 0 for empty buckets |
| Pt 3 | SELECTEDVALUE granularity detection, STARTOFMONTH, range targets, 5 pitfalls, sell-through rate, KPI card display |

## External Resources

- DAX Formatter: daxformatter.com
- SQLBI DAX patterns: sqlbi.com/dax-patterns/
- SELECTEDVALUE docs: learn.microsoft.com/dax/selectedvalue-function
- CALCULATE deep dive: sqlbi.com/articles/introducing-calculate-in-dax/
- Performance Analyzer: learn.microsoft.com/power-bi/create-reports/desktop-performance-analyzer

## Extracted Notes

- [[Dynamic-Goal-Selection-via-SELECTEDVALUE]] — `pattern` — SELECTEDVALUE cascade; day/month/annual target selection
- [[STARTOFMONTH-Date-Anchoring]] — `function` — anchors to first-of-month for monthly target lookups
- [[Five-DAX-Pitfalls-and-Fixes]] — `gotcha` — circular deps, implicit/explicit, DIVIDE vs /, iterator context, NUMERIC vs AnyRef
- [[DAX-Measure-Best-Practices]] — `workflow` — explicit measures, DIVIDE, VAR/RETURN, no self-reference, context transition
- [[Sell-Through-Rate-Pattern]] — `pattern` — DIVIDE COUNT(Sales) by COUNT(Production); BLANK on zero production
- [[KPI-Card-Clean-Display-Dash-for-Blank]] — `pattern` — `" - "` for blank in KPI cards

## Metadata

| Field | Value |
|-------|-------|
| Source file | Advanced Power BI DAX Measures for Retail Analytics Pt 3.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Word count | ~354 |
