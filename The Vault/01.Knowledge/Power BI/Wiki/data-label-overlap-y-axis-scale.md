---
created: 2026-08-02
updated: 2026-08-05
source: Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels
note_type: atomic
tags: [powerbi, chart, data-label, bug, workaround]
---

# Data Label Overlap Due to Y-Axis Scale

When a chart's data label includes detail sub-values, the label can overlap the chart bar/column even with "Outside end" positioning selected.

## Root Cause

The Y-axis scale ends at or near the maximum data value, leaving no room for the taller label to render fully above the bar.

## Fix

Set the Y-axis Maximum to a value higher than the actual maximum, calculated as:

```
MaxValue + 35% × MaxValue
```

This creates headroom for the label without changing what the user sees in the data.

## Implementation

Create a measure named `Maximum Value` and assign it to the Y-axis Maximum via the `fx` option.

## Source

Isabelle Bittar — "Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels", 2024-01-21
