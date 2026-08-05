---
created: 2026-08-02
source: Dynamic Bin Analysis Using Percentile Bucketing in Power BI (PBIX Included!) 🎢.md
note_type: pattern
tags: [powerbi, dax, percentilex, allselected, percentile-buckets]
---

# Dynamic Percentile Threshold Measures

Five DAX measures that compute percentile boundaries (p0, p20, p40, p60, p80, p100) for a numeric column, recalculated dynamically per the user's current filter context.

## Purpose

These measures form the foundation of percentile bucketing. Each computes the dollar value at a given percentile of the filtered dataset. Because they use `ALLSELECTED`, they respond to page-level slicers while ignoring the visual's own axis (cross-filtering is preserved).

## Structure

```dax
[Total Expense Amount] = SUM ( Expenses[Amount] )

p0 Amount =
    PERCENTILEX.INC (
        ALLSELECTED ( Invoices ),
        [Total Expense Amount],
        0.0
    )

p20 Amount =
    PERCENTILEX.INC (
        ALLSELECTED ( Invoices ),
        [Total Expense Amount],
        0.20
    )

p40 Amount =
    PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 0.40 )

p60 Amount =
    PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 0.60 )

p80 Amount =
    PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 0.80 )

p100 Amount =
    PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 1.0 )
```

## Key Design Decisions

- `ALLSELECTED(Invoices)` preserves cross-filtering from slicers (department, category, period) while ignoring the axis of the bar chart itself.
- `PERCENTILEX.INC` over `PERCENTILEX.EXC`: inclusive ensures bins span the full range including min and max, avoiding clipped extremes when users apply narrow filters.
- These are standalone base measures — not wrapped in FILTER — so they evaluate in a row context independent of the visual's granularity.

## Variations

- **p10 increments:** Use 0.1, 0.2, ..., 1.0 for deciles instead of quintiles.
- **Multiple columns:** Create separate percentile measures per metric (Amount, Quantity, Days) if bucketing different variables.

## Related

- [[percentile-bucketing-concept]]
- [[quintile-bucket-min-max-amount]]
- [[bucket-count-total-via-filter-allselected]]
