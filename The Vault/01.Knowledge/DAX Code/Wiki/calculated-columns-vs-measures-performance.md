---
created: 2026-07-30
updated: 2026-08-02
source: I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance.md
note_type: pattern
tags: [dax, calculated-columns, measures, performance, memory, pattern]
---

# Calculated Columns vs Measures — Performance Tradeoffs

Using calculated columns for values that could be measures causes slow data refresh and high memory consumption. The tradeoff: calculated columns = fast query / slow refresh / high memory; measures = slightly slower query / fast refresh / low memory.

## Purpose

Clarify when to use a calculated column versus a measure, focusing on the performance and memory implications of each approach. This is the second most common performance pattern found in production DAX (28% of slow measures).

## The Tradeoff Matrix

| Dimension | Calculated Column | Measure |
|-----------|-------------------|---------|
| Evaluation | At data refresh (once) | At query time (every time) |
| Memory | Stores full column of values | No storage |
| Query speed | Fast (pre-computed) | Slower per query |
| Refresh time | Slow (recomputes entire column) | N/A (nothing to refresh) |
| Row context | Yes (row by row at refresh) | No (filter context) |

## The Problem Pattern

Storing business logic as calculated columns in large tables:

```dax
-- In a 8.2M-row Sales table:
GrossProfit       -- calculated column (stored)
GrossProfitMargin -- calculated column (stored)
Year              -- calculated column (derived from Date)
Quarter           -- calculated column (derived from Date)
YearMonth         -- calculated column (derived from Date)
PriorYearAmount   -- calculated column (stored)
YoYGrowth         -- calculated column (stored)
```

12 calculated columns → 890 MB extra memory, 22 minutes of refresh time.

## When Calculated Columns ARE Correct

1. **Used for filtering or grouping**: values used in slicers, rows, or columns on visuals:
```dax
-- Good: used for slicing
ProductCategory = RELATED(Products[Category])
```

2. **Small dimension tables**: tables with hundreds or thousands of rows (the storage cost is negligible):
```dax
-- Fine: Products table has 200 rows
FullPrice = Products[ListPrice] * Products[UnitsPerCase]
```

3. **Used as a bridge column**: for data that genuinely changes slowly and needs to be stable between refreshes.

## When Measures Are Correct

Any calculation that aggregates, compares, or operates across multiple rows:

```dax
-- Good: measure — computed at query time
Gross Profit =
SUMX(Sales, Sales[Revenue] - Sales[Cost])

-- Good: measure — percentage of total
% of Total =
DIVIDE(
    SUM(Sales[Revenue]),
    CALCULATE(SUM(Sales[Revenue]), REMOVEFILTERS())
)
```

## The Decision Rule

Ask: **"Will this value ever be used as a filter, slicer, or axis label?"**

- YES → calculated column (or a column in the source)
- NO (it's a number I aggregate) → measure

## Related

- [[measures-vs-calculated-columns]] — conceptual differences
- [[calculated-column-vs-calculated-field]] — DAX-specific terminology
