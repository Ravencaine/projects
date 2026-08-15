---
created: 2026-08-06
updated: 2026-08-06
source: Building a Clean KPI Card in Power BI With DAX and HTML.md
note_type: atomic
tags: [dax, kpi, growth, divide, time-intelligence]
---

# KPI Card: Growth % via DIVIDE

Calculate period-over-period growth as a ratio using `DIVIDE`, avoiding division-by-zero errors.

## Definition

`DIVIDE([Total Sales] - [Previous Sales], [Previous Sales])` — computes growth as `(current − previous) / previous`. `DIVIDE` returns `BLANK()` instead of an error when the denominator is zero.

## Key Points

- `DIVIDE` is safer than the `/` operator — handles zero denominator gracefully
- Result is a **ratio** (e.g., `0.15` for 15%), not a percentage string — format with `FORMAT(..., "0.0%")` for display
- Previous period measure uses `CALCULATE` + `DATEADD` to shift the date context back one month

## Examples

```dax
Growth % =
DIVIDE(
    [Total Sales] - [Previous Sales],
    [Previous Sales]
)

Previous Sales =
CALCULATE(
    [Total Sales],
    DATEADD(Sales[Date], -1, MONTH)
)
```

## Related

- [[divide-function-vs-divide-operator]] — `DIVIDE` vs `/`
- [[kpi-card-arrow-color-from-growth]] — consumes this measure to drive arrow/color
- [[kpi-card-context-preserving-measures]] — why these measures intentionally avoid `ALL()`
