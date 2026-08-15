---
created: 2026-08-13
source: 5 Mistakes in Power BI Data Modeling (And How to Fix Them)
note_type: pattern
tags: [dax, power-bi, data-modeling, calculated-column, measure, beginner, performance]
---

# Data Modeling Mistake: Overusing Calculated Columns

<!-- Calculated columns materialise values at model refresh time, increasing memory and size. Measures compute at query time and are almost always the right choice for business logic. -->

## The Mistake

Using **calculated columns** for business metrics instead of **measures**.

```
❌ Calculated Column:
    Profit = Sales[Revenue] - Sales[Cost]

    → Computed once per row at refresh
    → Stored in the model (increases size)
    → Static — does not respond to slicer context
```

This is the #1 model bloat mistake for beginners.

## What Calculated Columns Actually Do

| | Calculated Column | Measure |
|--|---|---|
| Computed | At refresh time (once) | At query time (per visual) |
| Stored | Yes — in the model | No — computed on the fly |
| Responds to slicers | No — fixed value per row | Yes — evaluates in filter context |
| Memory impact | Increases model size | Zero |
| Use when | Need to filter/sort/group on the result | Need to aggregate or calculate ratios |

## The Fix Pattern

### Replace column logic with measures

```dax
// ❌ Column (wrong):
Profit = Sales[Revenue] - Sales[Cost]

// ✓ Measure (correct):
Profit =
SUM(Sales[Revenue]) - SUM(Sales[Cost])
```

### When columns ARE correct

Calculated columns are appropriate when:
- The result is used as a **slicer, filter, or row grouping** (DAX cannot filter on a measure)
- The value is a **categorical flag** (e.g., CustomerSegment = "Enterprise")
- You need to **sort a column** by a different value

```dax
// ✅ Valid column use — used to group/filter
IsEnterprise = IF(Customers[Revenue] > 1000000, "Enterprise", "SMB")

// ✅ Valid column use — sorting ProductName by TotalRevenue
// Set sort-by column on ProductName = Product[TotalRevenueSort]
TotalRevenueSort = SUM(Sales[Amount])
```

## Performance Impact

```
Model with 10 calculated columns × 10M rows = 100M stored values
Same model with 10 measures = 0 extra stored values
```

Calculated columns also block query parallelism in DirectQuery mode.

## Decision Tree

```
Does the calculation need to respond to slicers/filters?
  → YES → Use a MEASURE
  → NO  → Does it need to be used in a slicer, filter, or GROUP BY?
        → YES → Use a CALCULATED COLUMN
        → NO  → You probably don't need either
```

## Related

- [[measures-vs-calculated-columns]] — DAX Code: full comparison
- [[calculated-column-performance-impact]] — DAX Code: memory and query performance
- [[calculated-column-vs-measure-decision-tree]] — DAX Code: decision flowchart
- [[data-model-5-common-problems-fixes]] — Power BI: Problem 1 (numbers 10x too high — M:M vs column confusion)
