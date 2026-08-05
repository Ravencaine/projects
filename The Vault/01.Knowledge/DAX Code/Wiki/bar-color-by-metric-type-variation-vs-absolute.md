---
created: 2026-08-02
updated: 2026-08-05
source: Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data
note_type: pattern
tags: [dax, power-bi, conditional-formatting, color, field-parameters, switch]
---

# Bar Color by Metric Type (Variation vs. Absolute)

Color bars/columns green or red depending on whether the current metric is a variation or an absolute value — and whether the direction is positive or negative.

## Pattern

```c
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

## Logic

```
Metric Order in parameter
        ↓
Map to the specific variation measure (via SWITCH)
        ↓
If > 0 → green (positive change)
If < 0 → red (negative change)
If blank or non-variation metric → [_Color Main]
```

## Design Notes

- Only variation/comparison metrics get the red/green treatment
- Absolute metrics (Sales, Profit, Costs, Target) use the main brand color
- Color measures stored as dedicated measures (`[_Color Dark Green]`, `[_Color Dark Red]`) for reuse

## Applying

Use as **Column/Bar → Format → Data colors → fx → Field value** → `Bar Color` measure.

## Related

- [[color-palette-measures-static-hex-strings]] — color measure pattern
- [[conditional-formatting-via-dax]] — DAX-based conditional formatting
- [[label-font-color-variance-based]] — font color by variance direction
