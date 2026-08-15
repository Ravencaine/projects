---
created: 2026-08-06
updated: 2026-08-06
source: Building a Clean KPI Card in Power BI With DAX and HTML.md
note_type: atomic
tags: [dax, kpi, filter-context, measure-design]
---

# KPI Card: Context-Preserving Measure Design

Design KPI measures that react naturally to slicer and chart selections — without `ALL()` overriding filter context.

## Definition

KPI card measures use only `SUM`, `CALCULATE`, and time-intelligence functions (not `ALL`, `REMOVEFILTERS`, or `KEEPFILTERS`) so that the KPI responds to the report's active filters.

## Key Points

- `SUM(Sales[Amount])` alone is context-preserving — it respects row and filter context
- `CALCULATE` can shift time context (e.g., `DATEADD`) without breaking cross-visual interactivity
- **Avoid** `ALL()` in KPI measure definitions — it strips user-applied filters from the card, breaking sync with slicers and chart selections
- Measures must be self-contained so the KPI card and adjacent visuals stay in sync with no extra logic

## Examples

```dax
// Context-preserving — reacts to slicers
Total Sales = SUM(Sales[Amount])

// Time-shifted but still context-preserving
Previous Sales =
CALCULATE(
    [Total Sales],
    DATEADD(Sales[Date], -1, MONTH)
)

// NOT this — ALL strips filter context:
// Bad KPI Total = CALCULATE(SUM(Sales[Amount]), ALL(Sales))
```

## Related

- [[calculate]] — `CALCULATE` without `ALL` modifier
- [[dax-context]] — filter context and row context
- [[kpi-card-growth-percent-divide]] — uses this pattern
