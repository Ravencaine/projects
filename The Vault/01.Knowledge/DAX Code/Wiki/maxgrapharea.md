---
created: 2026-08-11
source: How I Built a Modern Oblique Area Chart in Power BI Using Only Native Visuals
note_type: function
tags: [dax, measure, chart-axis]
---

# MaxGraphArea

Returns the upper Y-axis boundary for a line chart, calculated as the global maximum vital value plus a 5% buffer.

## Signature

```dax
MaxGraphArea =
VAR _MaxVital =
    CALCULATE (
        MAXX ( ALL ( 'Vital Stats'[Date] ), [Max Vital] )
    )
RETURN
    _MaxVital + 0.05 * _MaxVital
```

## Purpose

Sets the Y-axis maximum for a line chart so that the chart canvas extends slightly beyond the data range. The 5% buffer creates visual breathing room and enables the error-bar fill technique to mask the area above the maximum data line.

## Context

Used with MinGraphArea to control the chart's Y-axis range. Combined with white-filled error bars, these measures enable the oblique area chart effect — white fills hide everything outside the desired range, leaving only the slanted area between Min and Max visible. See [[how-i-built-a-modern-oblique-area-chart-native-visuals]].
