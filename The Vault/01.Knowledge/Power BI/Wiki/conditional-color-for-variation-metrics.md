---
created: 2026-08-02
updated: 2026-08-05
source: Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data.md
note_type: pattern
tags: [powerbi, conditional-formatting, color-logic, dax, variation-metrics]
---

# Conditional Color for Variation Metrics

A DAX color measure that returns green or red based on whether a variation or "vs target" metric is positive or negative, applied to chart bars/columns via conditional formatting.

## Purpose

When showing comparison metrics (Sales vs. Target, Variation %), color-coding bars green (positive) or red (negative) lets users instantly spot good or bad performance without reading the axis values.

## Structure

```dax
Bar Color =
VAR _sel = SELECTEDVALUE('Metric'[Order])
VAR _value =
    SWITCH(
        _sel,
        1, [_Sales Variation Selected Period],
        2, [_Sales vs. Target Selected Period],
        5, [_Profit Variation Selected Period],
        7, [_Costs Variation Selected Period],
        BLANK()
    )
RETURN
    IF(
        NOT ISBLANK(_value),
        IF(_value > 0, [_Color Dark Green], [_Color Dark Red]),
        [_Color Main]
    )
```

## How It Works

1. `SELECTEDVALUE('Metric'[Order])` — detects which metric the user has selected by its sort order in the field parameter.
2. `SWITCH` — maps the selected metric order to its corresponding measure.
3. `ISBLANK` — returns the default color when the selected metric is not a variation metric (avoids blank/null color errors).
4. `IF(_value > 0, ...)` — returns green for positive values, red for negative or zero.
5. The measure is applied via **Conditional formatting → Field value** on the visual's data colors.

## Key Rules

- Each variation metric must have a unique sort order integer in the field parameter.
- The color measures (e.g. `_Color Dark Green`, `_Color Main`) should be defined in the model as fixed color constants.
- Non-variation metrics fall through to the `BLANK()` → `[_Color Main]` path.

## Related

- [[field-parameters-for-metric-dimension-selection]]
- [[visual-explorer-pattern]]
