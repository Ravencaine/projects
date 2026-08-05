---
created: 2026-08-02
source: Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels
note_type: function
tags: [dax, measure, chart, axis, max]
---

# Maximum Value (Y-Axis Headroom)

Calculates the maximum value in a measure and adds 35% padding — used to set the Y-axis maximum and prevent data label overlap.

```dax
Maximum Value =
VAR _MaxProcessDuration =
    MAXX(
        ALL('Process Steps'),
        [Process Duration]
    )
VAR _AxisValue = _MaxProcessDuration + 0.35 * _MaxProcessDuration
RETURN _AxisValue
```

## Why 35%

Empirical choice — enough to accommodate detail sub-values without visually changing the chart's scale.

## Usage

Assigned to the Y-axis Maximum via the `fx` option on a bar/column chart.

## Pattern

`MAXX(ALL(...), <measure>)` — iterates over the full unfiltered table to find the global maximum, ignoring any slicer or filter context.

## Source

Isabelle Bittar — "Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels", 2024-01-21
