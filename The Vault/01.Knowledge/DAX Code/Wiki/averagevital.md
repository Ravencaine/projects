---
created: 2026-08-11
source: How I Built a Modern Oblique Area Chart in Power BI Using Only Native Visuals
note_type: function
tags: [dax, measure, healthcare]
---

# AverageVital

Returns the average value for a selected vital sign from the Vital Stats table.

## Signature

```dax
AverageVital =
CALCULATE (
    SUM ( 'Vital Stats'[Value] ),
    FILTER ( 'Vital Stats', 'Vital Stats'[Measure Type] = "Average" )
)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| 'Vital Stats'[Value] | Numeric column containing vital readings |
| 'Vital Stats'[Measure Type] | Column identifying the measure type (Average/Max/Min row) |

## Purpose

Used in an oblique area chart as the main data series. The measure filters to only the "Average" row within the Vital Stats table, which stores one row per vital type with separate Average/Max/Min columns.

## Context

Part of a three-measure set (AverageVital, MaxVital, MinVital) used to create a modern healthcare area chart using only native visuals. See [[how-i-built-a-modern-oblique-area-chart-native-visuals]].
