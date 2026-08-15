---
created: 2026-08-09
updated: 2026-08-09
source: "Filtering measures through slicers.md"
note_type: atomic
tags: [dax, measure, filter, granularity, measure-cannot-be-filtered, atomic]
---

# Measure Cannot Be Filtered Granularity Required Atomic

**Type:** Atomic · **KB:** DAX Code · **Source:** [[source-filtering-measures-through-slicers]]

A measure cannot be filtered directly. "Filter Sales Amount greater than 100,000" is logically incomplete — a filter must act on a column (entity), not on a measure. You must always define the **granularity**: the table/column over which the measure is evaluated.

## The incomplete question

| Question | Why incomplete |
|----------|---------------|
| "Filter Sales Amount > 100k" | No entity specified — filter on what? |
| "Filter products with sales > 100k" | Complete — granularity is Product |
| "Filter customers with sales > 100k" | Complete — granularity is Customer |

## The semantic rule

> A filter always requires a column. A measure produces a scalar value per context. You cannot filter a scalar — you filter the rows that produce it.

## What actually happens

When you write `FILTER(Product, [Sales Amount] > 100000)`:
- `Product` = the granularity (column/table)
- `[Sales Amount]` = the measure evaluated per Product row
- The filter evaluates the measure at each Product's granularity, then keeps only those exceeding 100k

## Why beginners ask this

Power BI's visual filter pane allows placing a measure in the filter well. This creates the illusion that measures can be filtered. In reality, the visual provides the granularity automatically (e.g., matrix groups by Brand).

## Related

- [[measure-as-filter-in-visual-filter-pane]] — why visual filter pane creates the illusion
- [[filterproductsbasedonmeasure-local-function]] — implementing the pattern correctly
