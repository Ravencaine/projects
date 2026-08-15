---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 1
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-1-297936931171
note_type: source
tags: [dax, retail, variance, measures, budget, year-over-year]
---

# Source: Ruiz — Retail DAX Measures Pt 1

> **Type:** article (Part 1 of a series)
> **Author:** Jesse Ruiz (she/they)
> **Published:** 2026-07-06
> **URL:** https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-1-297936931171
> **Routed to:** DAX Code
> **Category:** DAX, Retail Analytics

## Summary

Part 1 of a series covering DAX fundamentals and sales variance measures for retail analytics. Topics: measures vs calculated columns, filter context vs row context, budget-vs-actual variance formula with conditional -100% hiding, and teaching points on VAR/RETURN, DIVIDE, and BLANK() vs 0. Part 2 covers time intelligence and inventory aging.

## Key Claims

1. **Measures vs Calculated Columns:** Measure = query-time aggregation responding to filter context; Calculated Column = refresh-time row-by-row computation. Rule: use measure for aggregated numbers that change with context; use column for values needed per row.
2. **Filter Context:** The set of active filters when a measure is evaluated. `SUM(Sales[NetAmount])` with `Store = "STORE001"` returns only that store's sales.
3. **Row Context:** Iteration over each row in a table. `SUMX(Sales, [Quantity] * [UnitPrice])` multiplies per-row, then sums.
4. **Variance formula:** `DIVIDE([Total Sales], [Budget]) - 1` — returns 0.25 (+25%), 0 (on budget), -0.10 (-10%), -1 (-100%)
5. **Conditional variance display:** If budget is BLANK → return BLANK; if variance ≤ -1 → return BLANK. Hides -100% from missing budgets.
6. **BLANK() vs 0:** BLANK is excluded from averages (denominator counts non-blank rows only); 0 is included.
7. **DIVIDE vs /:** DIVIDE returns BLANK on division by zero or blank; `/` throws an error.
8. **VAR/RETURN pattern:** Name each intermediate calculation; readable top-to-bottom; avoids repeated expressions.

## Code Patterns Extracted

| Pattern | Use |
|---------|-----|
| `_CONDITIONAL_VAR %_` | Hide -100% variance for missing budgets |
| `_CONDITIONAL_Day %_` | Day-level variance with same hiding logic |
| `_CONDITIONAL_MTD %_` | Month-to-date variance |
| `_CONDITIONAL_YOY %_` | Year-over-year variance |

## Teaching Points

- `SUM` operates on a column within filter context; `SUMX` iterates row-by-row with row context
- Variables make logic readable and debuggable — name each step
- `BLANK()` is DAX's representation of missing data; not the same as 0
- `DIVIDE(a, b, BLANK())` returns BLANK on divide-by-zero instead of error
- Average with BLANK: store C (BLANK) excluded from both sum and count → `(100+0)/2 = 50` not `(100+0+0)/3`

## Notable Details

- Dataset: RetailSalesTransactions (11,000+ records)
- Author self-describes as covering "conversational technical guide"
- Part 2 link: Time Intelligence + Inventory Aging (medium.com/@jjr8888/7b00a1662317)
- External resources: DAX Formatter (daxformatter.com), SQLBI DAX patterns library

## Extracted Notes

- [[Conditional-Variance-Display-Hide-Minus-100]] — `pattern` — variance pattern with ISBLANK guard and raw_variance <= -1 hiding
- [[DAX-VAR-RETURN-Pattern]] — `pattern` — VAR/RETURN for readable, debuggable measures
- [[DIVIDE-Safe-Division]] — `function` — safe division, BLANK on zero, vs / operator
- [[BLANK-vs-Zero]] — `function` — BLANK excluded from aggregations; 0 included; average example

## Metadata

| Field | Value |
|-------|-------|
| Source file | Advanced Power BI DAX Measures for Retail Analytics Pt 1.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Word count | ~305 |
