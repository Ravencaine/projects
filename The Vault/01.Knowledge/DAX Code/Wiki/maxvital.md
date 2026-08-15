---
created: 2026-08-11
source: How I Built a Modern Oblique Area Chart in Power BI Using Only Native Visuals
note_type: function
tags: [dax, measure, healthcare]
---

# MaxVital

Returns the maximum value for a selected vital sign from the Vital Stats table.

## Signature

```dax
MaxVital =
CALCULATE (
    SUM ( 'Vital Stats'[Value] ),
    FILTER ( 'Vital Stats', 'Vital Stats'[Measure Type] = "Max" )
)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| 'Vital Stats'[Value] | Numeric column containing vital readings |
| 'Vital Stats'[Measure Type] | Column identifying the measure type (Average/Max/Min row) |

## Purpose

Used in an oblique area chart as the upper boundary series. The measure filters to only the "Max" row within the Vital Stats table.

## Context

Part of a three-measure set (AverageVital, MaxVital, MinVital). MaxVital drives both the chart line and the upper error bar bound in the oblique area chart technique. See [[how-i-built-a-modern-oblique-area-chart-native-visuals]].
