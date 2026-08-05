---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Working with Fields and Measures.md"
note_type: atomic
tags: [dax, calculated-column, performance, model-size, beginner]
---

# Calculated Column Performance Impact

Calculated columns add data to the model. Measures do not. This distinction drives the most common performance mistake beginners make: overusing calculated columns for calculations that should be measures.

## Storage Impact

Every calculated column is stored in compressed format in the model. The storage cost is real — each column adds to the final .pbix file size.

| Source data | Model with calculated columns |
|------------|------------------------------|
| 50 MB raw data | 50–60 MB (few columns, well-chosen) |
| 50 MB raw data | 400–800 MB (too many calculated columns) |
| 50 MB raw data | 50 MB (all calculations as measures) |

A 50 MB source producing an 800 MB .pbix is almost always a calculated column bloat problem.

## Refresh Time Impact

Calculated columns are evaluated at every data refresh. Complex DAX in a calculated column adds directly to refresh time — every refresh recomputes the entire column from scratch. Measures have zero impact on refresh time (they don't store data).

## Query Speed

Once computed and stored, calculated columns are fast for filtering and slicing — the data is already materialised. Measures compute at query time, which costs CPU but typically less than the memory cost of storing the column.

## When Calculated Columns Are Worth It

Not all calculated columns are a problem. The cost is justified when:
- The result is needed in a slicer, filter, or Matrix rows/columns
- The result is a relationship key (e.g., `DateKey = FORMAT(Date, "YYYYMMDD")`)
- The result is used for cross-table lookups via `RELATED()`
- The result is a categorical property of each row that would be expensive to compute at query time repeatedly

## When to Convert to a Measure

If a calculated column is only used inside visuals as a numeric value (not as a filter), convert it to a measure:

```dax
// ❌ Calculated column — stored for every row
TotalRevenue = Sales[Quantity] * Sales[UnitPrice]

// ✅ Measure — computed on demand, zero storage cost
Total Revenue = SUMX(Sales, Sales[Quantity] * Sales[UnitPrice])
```

## The Priority Rule

> **Do as much as possible in Power Query (M language).** M transformations happen before compression — they cost less storage than DAX calculated columns for equivalent operations. Reserve DAX calculated columns for operations that require the model layer (relationships, RELATED(), context transitions).

## Related

- [[calculated-column-vs-measure-decision-tree]] — when a column is the right choice
- [[power-query-vs-dax-calculated-columns]] — the Power Query alternative
- [[calculated-column-vs-measure-total-sums]] — the percentage mistake that bloats models
