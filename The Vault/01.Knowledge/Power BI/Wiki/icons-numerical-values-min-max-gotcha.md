---
created: 2026-08-09
updated: 2026-08-09
source: "Elevate Your Power BI Tables with Custom Icons 🥳 1.md"
note_type: gotcha
tags: [power-bi, custom-icons, conditional-formatting, min-max, gotcha]
---

# Icons Numerical Values Min Max Constraint Gotcha

**Type:** Gotcha · **KB:** Power BI · **Source:** [[source-custom-icons-power-bi-tables]]

Cell element icon conditional formatting requires a minimum and maximum value to be set when using icons on numerical fields. If your data values fall outside the defined range, the icons won't display — even for valid data points.

## The problem

Conditional formatting icons on numerical columns requires a min/max range:

```
Minimum: 0
Maximum: 1000
```

If a data value exceeds the maximum (e.g., 1500) or falls below the minimum, no icon appears for that row.

## Why this is a problem

For trend indicators (up/down arrows based on price variation), the actual values are not known in advance. A static min/max range will fail for values outside the range.

## Workaround: intermediate text measure

1. Create a DAX measure that classifies the value as text:

```dax
Trend Icon =
VAR Change = [Price] - [PriorPrice]
RETURN
    IF(Change > 0, "positive",
        IF(Change < 0, "negative", "neutral"))
```

2. Apply custom icons to this text measure instead of directly to the numerical column
3. Create icon rules: "positive" → up arrow, "negative" → down arrow, "neutral" → equal icon

Text-based icon rules don't require min/max values — they use exact match or contains rules.

## Rule of thumb

> For icon-based indicators on numerical data, always use a text-based intermediate measure rather than applying icons directly to the numeric field.

## Related

- [[custom-icons-json-theme-cell-element-pattern]] — pattern
- [[embed-custom-icons-theme-workflow]] — workflow
