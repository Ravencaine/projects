---
created: 2026-08-02
updated: 2026-08-05
source: Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data.md
note_type: source
tags: [powerbi, visualization, tutorial, bookmarks, field-parameters]
---

# Source: Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data

> Author: Isabelle Bittar
> Published: 2025-11-01
> URL: https://medium.com/microsoft-power-bi/build-a-visual-explorer-in-power-bi-let-users-choose-what-and-how-they-see-data-d19d35c765e8

## Introduction

When people start using reports — like really using them — they end up with more questions, not fewer. That is a good thing: dashboards are doing their job, sparking curiosity and deeper analysis. But it also means users ask for "just one more visual" or "a slightly different view."

A Visual Explorer solves this. Instead of creating dozens of near-identical pages, give users the freedom to customise their view — choosing what metric to analyze and how to visualise it (bar, line, table, etc.). It is a mini reporting sandbox inside Power BI.

These exploration sections are especially valuable on client projects with heavy report usage. The more users can explore on their own, the fewer ad hoc requests the author receives.

## Step 1: Create Field Parameters for Metrics and Dimensions

Create two field parameters:

- **Metric** — Sales, Profit, Target, Variations, Costs, etc.
- **Dimension** — Region, Category, Customer Segment, Product Type, Sales Channel

Each parameter allows users to switch between different fields without modifying visuals directly.

**Metric parameter:**

```c
Metric = {
    ("Sales", NAMEOF('_Measures'[Sales Selected Period]), 0),
    ("Sales Variation %", NAMEOF('_Measures'[Sales Variation Selected Period]), 1),
    ("Sales vs. Target", NAMEOF('_Measures'[Sales vs. Target Selected Period]), 2),
    ("Target", NAMEOF('_Measures'[Target Selected Period]), 3),
    ("Profit", NAMEOF('_Measures'[Profit Selected Period]), 4),
    ("Profit Variation %", NAMEOF('_Measures'[Profit Variation Selected Period]), 5),
    ("Costs", NAMEOF('_Measures'[Costs Selected Period]), 6),
    ("Costs Variation %", NAMEOF('_Measures'[Costs Variation Selected Period]), 7)
}
```

**Dimension parameter:**

```c
Dimension = {
    ("Region", NAMEOF('Sales'[Region]), 0),
    ("Category", NAMEOF('Sales'[Category]), 1),
    ("Customer Segment", NAMEOF('Sales'[Customer Segment]), 2),
    ("Product Type", NAMEOF('Sales'[Product Type]), 3),
    ("Sales Channel", NAMEOF('Sales'[Sales Channel]), 4)
}
```

Add slicers for each parameter so users can interactively choose their metric and dimension.

## Step 2: Create Bookmarks to Switch Between Visual Types

Build one version of each visual to include (bar, column, line, table, matrix). Position them in the same spot so they overlap perfectly. Assign the Metric and Dimension field parameters to their respective axis on each visual.

Create one bookmark per visual type. In the bookmark options, **ensure "Data" is unchecked** so slicer selections stay intact when switching visuals.

Integrate a bookmark navigator to enable users to toggle between chart options.

**Tip:** The included PBIX file contains a "View Selection" group of objects — images and bookmark holder setup — that can be copied into any report. The visual icons used are screenshots of default Power BI visual icons, but custom icons matching the dashboard UI can be substituted.

**Bonus — Matrix with Column Selector:** A second field parameter ("Dimension 2") assigned to matrix columns lets users decide what appears across the columns. This enables analyzing a chosen metric by row category and column dimension simultaneously.

## Step 3: Create a Dynamic Chart Title

A DAX measure updates the chart title based on the user's current selections:

```c
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

When users select multiple metrics or dimensions, the title adjusts dynamically, helping them stay oriented as they explore.

## Step 4: Add Color Logic for "vs" or "Variation" Metrics

When showing comparisons (Sales vs. Target, Variation %), color-coding bars/columns green/red helps users instantly spot good or bad performance:

```c
Bar Color =
VAR _sel = SELECTEDVALUE('Metric'[Order])
VAR _value =
    SWITCH(
        _sel,
        1, [_Sales Variation Selected Period],
        2, [_Sales vs. Target Selected Period],
        5, [_Profit Variation Selected Period],
        7, [_Costs Variation Selected Period],
        BLANK()
    )
RETURN
    IF(
        NOT ISBLANK(_value),
        IF(_value > 0, [_Color Dark Green], [_Color Dark Red]),
        [_Color Main]
    )
```

Apply this measure via conditional formatting on the visual's data colors.

## Step 5: (Optional) Add Time Context

Integrate a time selection toggle — Last Year, Last Quarter, Last Month — linked to the UDF or Selected Period measures, so users can see how performance evolves over time.

## Step 6: Finishing Touches

- Add subtle emojis for clarity and personality.
- Include a tooltip: "🖱️ Hover to expand, export, or other options."
- Use soft backgrounds and consistent button states to make interactions feel natural.

## Additional Features

- Color-coding for performance metrics (green/red).
- Dynamic date filters for exploring different periods.
- Metric-level descriptions via hover tooltip.
- Pre-defined "views" as bookmarks for quick access to common combinations.

## PBIX Download

Available at: [[Dynamic Visual Explorer.pbix]]
