---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 2
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-2-7b00a1662317
note_type: source
tags: [dax, retail, time-intelligence, inventory, year-over-year]
---

# Source: Ruiz — Retail DAX Measures Pt 2

> **Type:** article (Part 2 of a series)
> **Author:** Jesse Ruiz (she/they)
> **Published:** 2026-07-20
> **URL:** https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-2-7b00a1662317
> **Routed to:** DAX Code
> **Category:** DAX, Retail Analytics, Time Intelligence

## Summary

Part 2 of a series covering time intelligence functions (TOTALMTD, TOTALYTD, SAMEPERIODLASTYEAR, DATESBETWEEN) and inventory aging analysis for retail. Topics: MTD/YTD accumulation, YoY comparisons via SAMEPERIODLASTYEAR + ALL, MAXX + ALLSELECTED for budget retrieval, inventory age buckets (0–1 wk, 1–2 wk, 5+ wk), why bucket measures return 0 not BLANK, and ALL vs ALLSELECTED. Part 3 covers production targets and best practices.

## Key Claims

1. **TOTALMTD:** cumulative January 1–N; `TOTALMTD(SUM(col), dateCol)` or `CALCULATE(..., DATESMTD(dateCol))`
2. **TOTALYTD:** cumulative January 1 through selected date
3. **SAMEPERIODLASTYEAR:** shifts date filter back one year; uses ALL(dateTable[Date]) first to clear current filter
4. **ALL vs ALLSELECTED:** ALL ignores all filters; ALLSELECTED respects current user slicer selections
5. **DATESBETWEEN:** dynamic date range inside CALCULATE; `MINX(ALLSELECTED(...))` and `MAXX(ALLSELECTED(...))` supply dynamic boundaries from slicer
6. **Inventory aging buckets:** CALCULATE + `AgeInWeeks` column per bucket; age ranges: 0, 1, 2, 3, 4, >4 weeks
7. **Return 0 for buckets:** empty age bucket → `0` (so percentages sum to 100%); single KPIs with no data → `BLANK()`
8. **YTD Budget via MAXX + ALLSELECTED:** finds latest date in user's slicer selection, retrieves that month's budget row
9. **Context transition:** CALCULATE inside AVERAGEX converts row context back to filter context so `[Sales]` evaluates correctly per store
10. **Period shape preservation:** SAMEPERIODLASTYEAR preserves the shape of the selection (days → days, months → months)

## Code Patterns Extracted

| Measure | Pattern |
|---------|---------|
| MTD Sales | `TOTALMTD(SUM(col), dateCol)` |
| YTD Sales | `TOTALYTD(SUM(col), dateCol)` |
| YoY Sales | `CALCULATE([Sales], ALL(date), SAMEPERIODLASTYEAR(date))` |
| YTD Budget | `CALCULATE(SUM(...), date = MAXX(ALLSELECTED(dateTable), date))` |
| Age bucket | `CALCULATE([Sales], AgeInWeeks = N, DATESBETWEEN(...))` |
| Bucket total | Sum of all age bucket measures |

## Notable Details

- Dataset: RetailSalesTransactions with `AgeInWeeks` column; StoreBudgets at month level
- Part 1 covered: measures vs columns, filter context, budget variance, VAR/RETURN, DIVIDE, BLANK vs 0
- Part 3 link: Production Targets + Best Practices (medium.com/@jjr8888/f152d1b500b5)
- External: SQLBI Time Intelligence article, Microsoft docs for TOTALMTD, SAMEPERIODLASTYEAR, ALLSELECTED

## Extracted Notes

- [[Time-Intelligence-Functions-Reference]] — `reference` — TOTALMTD, TOTALYTD, SAMEPERIODLASTYEAR, DATESBETWEEN, MAXX+ALLSELECTED
- [[SAMEPERIODLASTYEAR-YoY-Pattern]] — `pattern` — YoY calculation; ALL + SAMEPERIODLASTYEAR; period shape preservation
- [[Inventory-Aging-Buckets-Pattern]] — `pattern` — CALCULATE per age bucket; 0→BLANK→0 for empty buckets; sum to 100%
- [[Return-Zero-vs-BLANK-for-Buckets]] — `atomic` — buckets return 0; single KPIs return BLANK; why it matters
- [[ALL-vs-ALLSELECTED]] — `function` — ALL ignores all filters; ALLSELECTED respects current slicer; when to use each
- [[DATESBETWEEN-Dynamic-Date-Ranges]] — `function` — dynamic date range from ALLSELECTED boundaries; vs hardcoded dates

## Metadata

| Field | Value |
|-------|-------|
| Source file | Advanced Power BI DAX Measures for Retail Analytics Pt 2.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Word count | ~337 |
