---
created: 2026-08-06
updated: 2026-08-06
source: Building a Clean KPI Card in Power BI With DAX and HTML.md
note_type: atomic
tags: [dax, kpi, conditional-formatting, if, divi]
---

# KPI Card: Arrow and Color from Growth

Return an arrow symbol and hex color code based on whether a growth value is positive or negative.

## Definition

`IF(Growth >= 0, "▲", "▼")` for the arrow — use with `IF(Growth >= 0, "#22c55e", "#ef4444")` for the color. The color maps green (`#22c55e`) for growth and red (`#ef4444`) for decline.

## Key Points

- Arrow and color are driven by the **same condition:** always in sync
- Use hardcoded hex values for HTML Content output; use Power BI conditional formatting natively for native KPI visuals
- Can be extended to handle zero: `IF(Growth > 0, ..., IF(Growth < 0, ..., ...))`

## Examples

```dax
VAR Growth = [Growth %]
VAR Arrow  = IF(Growth >= 0, "▲", "▼")
VAR Color  = IF(Growth >= 0, "#22c55e", "#ef4444")
RETURN
    "{Arrow} {FORMAT(Growth, '0.0%')}"
```

## Related

- [[divide-function-vs-divide-operator]] — used to compute growth
- [[kpi-card-html-content-measure-presentation-logic]] — combines this with presentation variables
