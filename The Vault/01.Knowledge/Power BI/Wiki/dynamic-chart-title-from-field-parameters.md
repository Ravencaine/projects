---
created: 2026-08-02
updated: 2026-08-05
source: Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data.md
note_type: pattern
tags: [powerbi, dax, dynamic-title, field-parameters, selectcolumns, concatenatex]
---

# Dynamic Chart Title from Field Parameters

A DAX measure that reads the user's current `ALLSELECTED` selections from `Metric` and `Dimension` field parameters and assembles a human-readable chart title.

## Purpose

When users change the metric or dimension via slicers, the chart title updates automatically to reflect the current selection — keeping users oriented without needing a fixed static title.

## Structure

```dax
Chart Title =
VAR _MetricTbl =
    SELECTCOLUMNS (
        ALLSELECTED ( 'Metric' ),
        "Metric", 'Metric'[Metric],
        "Sort",   'Metric'[Metric Order]
    )
VAR _DimTbl =
    SELECTCOLUMNS (
        ALLSELECTED ( 'Dimension' ),
        "Dimension", 'Dimension'[Dimension],
        "Sort",      'Dimension'[Dimension Order]
    )

VAR _MetricCount = COUNTROWS ( _MetricTbl )
VAR _DimCount    = COUNTROWS ( _DimTbl )

VAR _MetricTextWhenShown =
    SWITCH (
        TRUE(),
        _MetricCount = 0, "Metric",
        _MetricCount = 1, MAXX ( _MetricTbl, [Metric] ),
        _MetricCount = 2, CONCATENATEX ( _MetricTbl, [Metric], " and ", [Sort], ASC ),
        /* _MetricCount > 2 */ CONCATENATEX ( _MetricTbl, [Metric], ", ", [Sort], ASC )
    )

VAR _DimText =
    SWITCH (
        TRUE(),
        _DimCount = 0, "Dimension",
        _DimCount = 1, MAXX ( _DimTbl, [Dimension] ),
        _DimCount = 2, CONCATENATEX ( _DimTbl, [Dimension], " and ", [Sort], ASC ),
        /* else */        CONCATENATEX ( _DimTbl, [Dimension], ", ", [Sort], ASC )
    )

RETURN
    IF (
        _MetricCount > 2,
            "📊 View by " & _DimText,
            "📊 " & _MetricTextWhenShown & " by " & _DimText
    )
```

## How It Works

1. `ALLSELECTED('Metric')` / `ALLSELECTED('Dimension')` — captures the user's current slicer selections.
2. `SELECTCOLUMNS` — extracts just the label and sort order into local variables.
3. `COUNTROWS` — determines how many items are selected (single, two, or many).
4. `SWITCH` + `TRUE()` pattern — handles the three cases: zero, one, two, or many selections.
5. `CONCATENATEX` — joins two labels with "and" for two selections, or commas for more.
6. `IF` — hides the metric name from the title when more than two metrics are selected (prevents a cluttered title).

## Key Rules

- The field parameter tables must include an `Order` column (integer) used for sorting in `CONCATENATEX`.
- The title measure is applied to the visual's Title property via the Field option in the visual's format pane.

## Related

- [[field-parameters-for-metric-dimension-selection]]
- [[visual-explorer-pattern]]
