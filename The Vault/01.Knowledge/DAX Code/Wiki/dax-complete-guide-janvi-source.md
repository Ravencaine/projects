---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
source_url: "https://medium.com/microsoft-power-bi/master-power-bi-introduction-to-dax-the-complete-guide-93d52ce1846c"
note_type: source
tags: [dax, power-bi, beginner, tutorial, time-intelligence, measures, calculated-columns, filters]
---

# DAX — The Complete Guide — Janvi Gupta

> **Type:** tutorial / beginner guide
> **Author:** Janvi Gupta
> **Published:** 2026-01-05
> **URL:** https://medium.com/microsoft-power-bi/master-power-bi-introduction-to-dax-the-complete-guide-93d52ce1846c
> **Routed to:** DAX Code
> **KB:** DAX Code

## Summary

Definitive beginner's guide covering the full DAX learning path: foundations (vs Excel), basic aggregation measures, measures vs calculated columns with context, CALCULATE and filter context modification, time intelligence (YTD, MTD, PY, YoY), logical functions (IF/SWITCH), filter functions (ALL/ALLSELECTED/ALLEXCEPT/FILTER/KEEPFILTERS), iterator functions (SUMX/AVERAGEX/COUNTX), advanced patterns (running totals, ranking, ABC analysis, Pareto, churn), and DAX optimisation best practices.

## The Three Building Blocks

| Element | Evaluated | Stored | Use |
|---------|-----------|--------|-----|
| **Field** | In data source | Yes (compressed) | Raw data; filter/slice by column values |
| **Calculated Column** | Row-by-row at refresh | Yes (adds to model size) | Categorisations, text combinations, properties that need to be filtered |
| **Measure** | At query time, per visual | No (formula only) | Aggregations, ratios, dynamic calculations |

## The Critical Distinction: Context

**Row context**: evaluated one row at a time. Calculated columns iterate through each row independently. Think Excel: a formula in cell C1 looks at columns A1 and B1 in the same row.

**Filter context**: evaluated based on what is currently filtered in the report. Measures look at the set of rows visible under all active filters and aggregate them. The measure has no single-row access.

## Decision Framework

Use a calculated column when: you need to filter/slice by the result; you need to create a relationship key; you're combining data from multiple columns into one; the result is a row-level property.

Use a measure when: you are aggregating values (SUM, AVERAGE, COUNT); you need dynamic calculations that respond to filters; you are calculating ratios or percentages; the result belongs in a visual, not as a filterable attribute.

## The Implicit Measure Trap

Dragging a numeric field directly into a visual creates an implicit measure — Power BI auto-selects a summarisation (usually SUM). Implicit measures are not reusable, have no controlled logic, don't work with calculation groups, and can change unexpectedly if someone changes the default summarisation. **Always create explicit measures, even for simple SUMs.**

## Common Mistakes

1. SUMX in calculated columns (wrong context — use a measure or direct multiplication)
2. Measures in calculated columns (no filter context available in a column)
3. Calculated column percentages summed to >100% in totals (percentage at row level ≠ percentage at total level)
4. Overusing calculated columns — a 50 MB source file producing an 800 MB .pbix is a calculated column bloat problem

## Performance Contrast

| | Calculated Column | Measure |
|-|------------------|---------|
| Storage | Adds to model size (compressed) | Zero (formula bytes only) |
| Refresh time | Evaluated at every refresh | N/A (evaluated at query time) |
| Query speed | Fast for filtering; slower to load | Fast — Power BI only computes for visible data |
| Optimisation | Better compression if done in Power Query first | Better DAX usually solves slow measures |

## Extracted Notes

- [[dax-vs-excel-mindset-difference]] — `atomic` — Excel references cells; DAX references columns; context is the key difference
- [[basic-aggregation-measures]] — `atomic` — SUM, COUNTROWS, AVERAGE, DISTINCTCOUNT; COUNTROWS over COUNT
- [[row-context-vs-filter-context]] — `atomic` — row context: one row at a time (columns); filter context: set of visible rows (measures)
- [[calculate-context-modifier]] — `atomic` — CALCULATE modifies filter context; most important DAX function
- [[calculate-pattern-library]] — `atomic` — 6 CALCULATE patterns: specific value, greater than, between, IN list, NOT equal, combining
- [[time-intelligence-functions]] — `atomic` — TOTALYTD, TOTALMTD, SAMEPERIODLASTYEAR, DATEADD, PREVIOUSMONTH, DATESINPERIOD
- [[time-intelligence-common-mistakes]] — `atomic` — no Date table, multiple active relationships, BLANK in growth measures
- [[logical-functions-switc]] — `atomic` — IF, nested IF, SWITCH, AND, OR, NOT, ISBLANK, IFERROR, DIVIDE third parameter
- [[filter-functions-all-allselected]] — `atomic` — ALL removes all filters; ALLSELECTED respects visual filters; % of total pattern
- [[filter-functions-allexcept-keepfilters]] — `atomic` — ALLEXCEPT keeps specific filters; KEEPFILTERS combines instead of replacing
- [[iterator-functions-sumx]] — `atomic` — SUMX, AVERAGEX, COUNTX, MINX, MAXX; when iterators are necessary
- [[iterator-performance-warning]] — `atomic` — iterators are expensive; calculated columns as alternative; avoiding repeated calculations
- [[advanced-patterns-ranking-abc-pareto]] — `atomic` — running total, RANKX, ABC analysis, Pareto 80/20, dynamic segmentation, churn
- [[dax-optimization-best-practices]] — `atomic` — VAR usage, filter on dimensions not facts, DIVIDE vs /, calculated column decision tree

## Metadata

| Field | Value |
|-------|-------|
| Source file | Master Power BI Introduction to DAX — The Complete Guide.md |
| Ingestion date | 2026-08-01 |
| Word count | ~8,000 |
| Level | Beginner |
| Category | DAX |
