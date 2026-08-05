---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Working with Fields and Measures.md"
note_type: atomic
tags: [dax, calculated-column, total-sums, percentages, measure, beginner, common-mistake]
---

# Calculated Column vs Measure: Total Sum Error

The most counterintuitive DAX mistake beginners make: storing a percentage in a calculated column produces mathematically incorrect totals when the column is summed in a visual.

## The Mistake

```dax
// ❌ In a calculated column
Margin % = (Sales[Revenue] - Sales[Cost]) / Sales[Revenue]
```

When placed in a table visual, the total row shows 104.67% instead of the correct 32%.

## Why It Happens

Power BI sums all the individual row percentages:
```
Row 1: 35.00%
Row 2: 28.00%
Row 3: 41.67%
Total (wrong): 104.67%  ← sums the individual percentages
```

But the correct total should be:
```
Total Revenue:  $1,000,000
Total Cost:       $680,000
Total Margin:       $320,000
Correct Margin %:  32.00%  ← percentage of the total, not sum of percentages
```

## The Formula in the Column vs the Formula in a Measure

The calculated column computes: `(Revenue - Cost) / Revenue` for each row independently. This is the row-level margin — what percentage each individual transaction contributed to its own revenue.

The correct total margin is: `(Total Revenue - Total Cost) / Total Revenue` — a percentage computed from the aggregated totals, not from the sum of row-level percentages.

## The Fix: Use a Measure

```dax
// ✅ As a measure — evaluates correctly at every aggregation level
Margin % =
DIVIDE(
    SUM(Sales[Revenue]) - SUM(Sales[Cost]),
    SUM(Sales[Revenue]),
    0
)
```

The measure evaluates `SUM(Revenue)` and `SUM(Cost)` at whatever aggregation level the visual is showing (row, category, total) — then computes the percentage. At the grand total row, it uses grand total revenue and cost. At a category row, it uses category totals.

## The Rule

> **Any calculation that involves division, ratio, or percentage belongs in a measure, not a calculated column.** The only exception is when you specifically need the row-level percentage for slicing or filtering purposes — in which case you are using the column as a category, not as a number to sum.

## Related

- [[calculated-column-row-context]] — why the column evaluates row-by-row
- [[measure-filter-context]] — why the measure evaluates at the filtered aggregate level
- [[calculated-column-vs-measure-decision-tree]] — the decision that prevents this mistake
