---
created: 2026-08-02
source: Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels
note_type: function
tags: [dax, measure, color, constants]
---

# Color Process Duration Variation (Hex Constants)

Returns the appropriate hex color string for the variation sign — green for decrease (positive outcome), red for increase (negative outcome).

```dax
Color Dark Green = "#3B952D"
Color Dark Red  = "#D8404A"

Color Process Duration Variation =
    IF(
        [Process Duration Variation] > 0,
        [Color Dark Red],
        [Color Dark Green]
    )
```

## Pattern

Named color constants as separate measures — keeps the color palette centralized and easy to update.

## Usage

Assigned to the `fx` (dynamic font color) option of a chart data label detail sub-value to color-code the variance text.

## Source

Isabelle Bittar — "Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels", 2024-01-21
