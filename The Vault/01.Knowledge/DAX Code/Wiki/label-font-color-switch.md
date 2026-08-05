---
created: 2026-08-02
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: pattern
tags: [dax, pattern, color, switch, conditional-formatting]
---

# Label Font Color (SWITCH(TRUE()) on Variance)

A SWITCH-TRUE measure returning a hex color name based on the sign of a variance metric. Used to apply conditional font color to chart data labels.

## Purpose

After applying conditional background colors to chart label series, the font color should also be adjusted so the label text remains legible — dark green on light green, dark red on light red. This measure provides that dynamic font color logic.

## Components

1. Color constant measures (`_Color Dark Green`, `_Color Dark Red`, `_Color Text Secondary`)
2. `SWITCH(TRUE(), ...)` — evaluates variance conditions in order
3. Color names returned as strings (Power BI resolves these via per-series conditional formatting or direct binding)

## Structure

```dax
_Color Dark Green = "#31D286"
_Color Dark Red   = "#F05660"
_Color Text Secondary = "#79797C"

Label Font Color =
    SWITCH(
        TRUE(),
        [Turnover Rate Variance] > 0, [_Color Dark Red],
        [Turnover Rate Variance] < 0, [_Color Dark Green],
        [_Color Text Secondary]
    )
```

## Notes

- For turnover: positive = bad (red), negative = good (green) — inverted from typical sales/variance patterns
- For metrics where increase is positive (e.g. revenue), swap the color assignments
- The color names are defined as separate measures and stored under `_Constants/Colors` in the PBIX measure tree
- Bound to the chart's **Data labels → Font color** property via the "fx" conditional formatting option pointing to this measure

## Related

- [[dummy-measures-for-label-background]]
- [[Variance-Arrow-Label]]
- [[Column-Color]]
