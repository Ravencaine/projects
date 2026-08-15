---
created: 2026-08-06
updated: 2026-08-06
source: Building a Clean KPI Card in Power BI With DAX and HTML.md
note_type: atomic
tags: [dax, kpi, if, text, summary]
---

# KPI Card: Growth Summary Text

Turn a growth percentage into a plain-language sentence describing the trend direction.

## Definition

`IF(Growth > 0, "Sales are increasing compared to last month", "Sales declined compared to last month")` — returns a human-readable string from a numeric growth measure.

## Key Points

- Uses a simple `IF` on the raw growth value — zero-growth falls into the declining branch
- The text is static and non-interactive; for multi-metric KPIs, generalize with a parameter or measure name substitution
- Useful inside HTML Content measures where the KPI card needs a textual interpretation alongside the number

## Examples

```dax
VAR Growth  = [Growth %]
VAR Summary =
    IF(
        Growth > 0,
        "Sales are increasing compared to last month",
        "Sales declined compared to last month"
    )
RETURN
    Summary
```

## Related

- [[kpi-card-arrow-color-from-growth]] — pairs with this for arrow + color
- [[kpi-card-html-content-measure-presentation-logic]] — both used as presentation variables in the HTML measure
