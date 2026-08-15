---
created: 2026-08-09
updated: 2026-08-09
source: "⚡How I Built a Modern Oblique Area Chart in Power BI (Using Only Native Visuals)"
note_type: reference
tags: [power-bi, y-axis, dynamic, min, max, measure, range, line-chart, axis, all]
---

# Dynamic Y-Axis Min/Max via Measures

The Power BI line chart's Y-axis accepts measures as its minimum and maximum values. This enables a fully dynamic axis range that recalculates based on the current data context — driven by DAX measures using ALL over the date column.

## How to Configure

1. Add the min/max measure to the **Y-axis Fields** well alongside the data series
2. Select the Y-axis → **Min** → select the min measure
3. Select the Y-axis → **Max** → select the max measure

## Dynamic Measures Used

```dax
Max Graph Area =  -- used as Y-axis max
VAR _MaxVital = CALCULATE(MAXX(ALL('Vital Stats'[Date]), [Max Vital]))
RETURN _MaxVital + 0.05 * _MaxVital

Min Graph Area =  -- used as Y-axis min
VAR _MinVital = CALCULATE(MINX(ALL('Vital Stats'[Date]), [Min Vital]))
RETURN _MinVital - 0.05 * _MinVital
```

## Why Use Measures Instead of Fixed Numbers

| Approach | Behaviour |
|----------|----------|
| Fixed numbers | Static; breaks when data changes or date selection changes |
| Measures (ALL over date) | Dynamic; recalculates based on full data range regardless of slicer/filter |

## Key Pattern

`ALL('Table'[Date])` inside the measure removes the date filter so the MAXX/MINX sees the entire dataset. This is essential for a consistent Y-axis range even when the user filters to a subset of dates.

## Related

- [[Source-Oblique-Area-Chart-Native-Visuals-Isabelle-Bittar]] — source
- [[MAXX-MINX-ALL-Date-Dynamic-Range]] — DAX: the underlying measure pattern
- [[Dynamic-Graph-Area-Buffer]] — the buffer pattern that feeds the Y-axis measures
- [[Error-Bars-White-Fill-Zones]] — how the dynamic range enables the white fill zone technique
