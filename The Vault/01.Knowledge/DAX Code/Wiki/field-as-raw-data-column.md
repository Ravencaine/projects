---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Working with Fields and Measures.md"
note_type: atomic
tags: [dax, power-bi, fields, columns, beginner]
---

# Field as Raw Data Column

Fields are the columns that come directly from your data source — the raw material Power BI uses to build everything else. Understanding what a field is and isn't is the foundation for knowing when you need more.

## What a Field Is

A field is a column imported from your data source. It appears in the Fields pane with a table icon and carries a Sigma (Σ) symbol if Power BI recognises it as numeric (and therefore capable of being aggregated).

| Property | Detail |
|----------|--------|
| Source | Directly from data source — no calculation applied |
| Storage | Compressed in the model alongside all other imported data |
| Values | Every value from the source column is stored and visible in Data view |
| Auto-aggregation | Numeric fields get Σ symbol — Power BI can automatically sum, average, count, etc. |

## What the Sigma (Σ) Symbol Means

The Σ symbol next to a numeric field means Power BI **can automatically aggregate this column**: sum it, average it, count rows, find the minimum or maximum. When you drag a numeric field into a visual without writing any DAX, Power BI creates an implicit measure using one of these aggregation types.

## The Two Paths from Field to Calculation

| Path | Creates | Evaluated |
|------|---------|-----------|
| Drag field into visual without DAX | Implicit measure | At query time, per visual |
| Write a DAX formula in the model | Explicit measure or calculated column | Measure: query time; Column: refresh time |

The Sigma symbol is not a recommendation to use implicit aggregation. The [[implicit-measure-trap]] explains why explicit measures are always preferable.

## When a Field Is Enough

- You only need the raw value, filtered or sliced by other dimensions
- No calculation is needed beyond the basic aggregation Power BI provides by default
- You are exploring data before writing any formulas

## Related

- [[calculated-column-row-context]] — what happens when a field needs computation row-by-row
- [[measure-filter-context]] — what happens when a field needs aggregation in a visual
- [[implicit-measure-trap]] — why auto-aggregation is a starting point, not a destination
