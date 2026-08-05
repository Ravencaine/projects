---
created: 2026-08-02
updated: 2026-08-05
source: Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data
note_type: pattern
tags: [dax, power-bi, dynamic-title, field-parameters, selectcolumns, allselected, concatenatex]
---

# Dynamic Chart Title from Metric + Dimension Selections

A `Chart Title` measure that reads `ALLSELECTED` from the Metric and Dimension field parameters and composes a readable title like `"📊 Sales by Region"`.

## Pattern

```c
Chart Title =
VAR _MetricTbl =
    SELECTCOLUMNS(
        ALLSELECTED('Metric'),
        "Metric", 'Metric'[Metric],
        "Sort",   'Metric'[Metric Order]
    )
VAR _DimTbl =
    SELECTCOLUMNS(
        ALLSELECTED('Dimension'),
        "Dimension", 'Dimension'[Dimension],
        "Sort",      'Dimension'[Dimension Order]
    )
VAR _MetricCount = COUNTROWS(_MetricTbl)
VAR _DimCount    = COUNTROWS(_DimTbl)

VAR _MetricText =
    SWITCH(TRUE(),
        _MetricCount = 0, "Metric",
        _MetricCount = 1, MAXX(_MetricTbl, [Metric]),
        _MetricCount = 2, CONCATENATEX(_MetricTbl, [Metric], " and ", [Sort], ASC),
        CONCATENATEX(_MetricTbl, [Metric], ", ", [Sort], ASC)
    )

VAR _DimText =
    SWITCH(TRUE(),
        _DimCount = 0, "Dimension",
        _DimCount = 1, MAXX(_DimTbl, [Dimension]),
        _DimCount = 2, CONCATENATEX(_DimTbl, [Dimension], " and ", [Sort], ASC),
        CONCATENATEX(_DimTbl, [Dimension], ", ", [Sort], ASC)
    )

RETURN IF(
    _MetricCount > 2,
    "📊 View by " & _DimText,
    "📊 " & _MetricText & " by " & _DimText
)
```

## Logic

| Metric count | Title format |
|-------------|--------------|
| 0 | `"📊 Metric"` |
| 1 | `"📊 [Metric] by [Dimension]"` |
| 2 | `"📊 [M1] and [M2] by [Dimension]"` |
| > 2 | `"📊 View by [Dimension]"` |

## Components Used

- `ALLSELECTED` — reads current parameter slicer state
- `SELECTCOLUMNS` — flattens parameter table to name + sort
- `CONCATENATEX` — joins multi-selection with "and" / ","
- `MAXX` — pulls single value from single-selection

## Related

- [[dynamic-text-titles-in-power-bi]] — general dynamic title pattern
- [[field-parameters-for-metric-dimension-selection]] — parameter setup
