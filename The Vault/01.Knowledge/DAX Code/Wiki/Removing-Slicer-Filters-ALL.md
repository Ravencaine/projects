---
created: 2026-08-05
updated: 2026-08-05
source: ALL and REMOVEFILTERS in Power BI (Boniface Muchendu)
note_type: pattern
tags: [dax, all, removefilters, calculate, slicer, grand-total, pattern]
---

# Removing Slicer Filters with ALL

Using `CALCULATE(..., ALL(...))` to return a grand-total measure that ignores all active slicer filters — enabling "percentage of total" ratios, "compare to total" KPIs, and unfiltered totals alongside filtered breakdowns.

## The Pattern

```dax
Total Sales = SUM(Sales[Amount])

Total Sales (Grand Total) =
CALCULATE(
    [Total Sales],
    ALL(DimProduct),
    ALL(DimSalesTerritory)
)
```

`Total Sales (Grand Total)` returns the same value regardless of which Country or Color slicer is active — it always shows the grand total across all products and territories.

## Why Use ALL in CALCULATE

By default, Power BI measures respect all slicer and filter context. Wrapping a measure in CALCULATE with ALL removes selected filters on specific tables or columns, forcing the measure to operate on the full unfiltered dataset.

## Multiple Tables

To ignore filters on multiple tables simultaneously, pass each as a separate argument to ALL:

```dax
Total Sales ALL =
CALCULATE(
    [Total Sales],
    ALL(DimProduct),           -- ignore Color slicer
    ALL(DimSalesTerritory),   -- ignore Country slicer
    ALL(DimDate)              -- ignore Date slicer
)
```

## Percentage of Total Pattern

ALL enables the "percentage of total" calculation:

```dax
% of Total Sales =
DIVIDE(
    [Total Sales],              -- filtered total
    CALCULATE([Total Sales], ALL(DimProduct))  -- grand total
)
```

- Numerator: respects the Color slicer (shows sales for selected color)
- Denominator: ignores Color slicer (shows sales for all colors)
- Result: selected color's share of total sales

## REMOVEFILTERS Equivalent

```dax
Total Sales REMOVEFILTERS =
CALCULATE(
    [Total Sales],
    REMOVEFILTERS(DimProduct),
    REMOVEFILTERS(DimSalesTerritory)
)
```

Same result — REMOVEFILTERS is the more readable modern form when only removing filters.

## Common Use Cases

| Use case | Description |
|---------|-------------|
| Grand total alongside filtered breakdown | Show both filtered and unfiltered totals on the same visual |
| % of total | Selected segment / All segments |
| Share of market | Selected region / All regions |
| Comparison KPIs | Current selection vs overall average |

## Related

- [[ALL-Function-DAX]]
- [[REMOVEFILTERS-Function-DAX]]
- [[ALL-vs-REMOVEFILTERS]]
