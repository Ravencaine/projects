---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Working with Fields and Measures.md"
source_url: "https://medium.com/microsoft-power-bi/master-power-bi-working-with-fields-and-measures-d0148fc37893"
note_type: source
tags: [dax, power-bi, fields, measures, calculated-columns, beginner, tutorial]
---

# Fields, Measures, and Calculated Columns — Janvi Gupta

> **Type:** tutorial / beginner guide
> **Author:** Janvi Gupta
> **Published:** 2025-12-04
> **URL:** https://medium.com/microsoft-power-bi/master-power-bi-working-with-fields-and-measures-d0148fc37893
> **Routed to:** DAX Code
> **KB:** DAX Code

## Summary

Definitive beginner's guide to the three foundational building blocks in Power BI: Fields (raw columns), Calculated Columns, and Measures. Core distinction: calculated columns operate in row context; measures operate in filter context. Covers the implicit measure trap, a decision framework for choosing between calculated columns and measures, and a comparison between Power Query M and DAX for column creation.

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

- [[field-as-raw-data-column]] — `atomic` — native columns from data source; sigma (Σ) auto-aggregation; implicit measures
- [[calculated-column-row-context]] — `atomic` — row context evaluates one row at a time; examples that work and fail
- [[measure-filter-context]] — `atomic` — filter context; measures aggregate visible rows under active filters
- [[calculated-column-vs-measure-decision-tree]] — `atomic` — 4-question decision tree for choosing correctly
- [[implicit-measure-trap]] — `atomic` — implicit vs explicit measures; why implicit measures cause problems
- [[calculated-column-performance-impact]] — `atomic` — model size, compression, refresh time; when columns are worth it
- [[calculated-column-vs-measure-total-sums]] — `atomic` — why percentage calculated columns sum incorrectly in totals
- [[power-query-vs-dax-calculated-columns]] — `atomic` — do in Power Query what you can; use DAX when you need RELATED()
- [[dax-calculated-column-use-cases]] — `atomic` — categorisations, relationship keys, row-level properties, RELATED()
- [[dax-measure-use-cases]] — `atomic` — aggregations, YoY growth, ratios, % of total, KPIs

## Metadata

| Field | Value |
|-------|-------|
| Source file | Master Power BI Working with Fields and Measures.md |
| Ingestion date | 2026-08-01 |
| Word count | ~3,500 |
| Level | Beginner |
| Category | DAX |
