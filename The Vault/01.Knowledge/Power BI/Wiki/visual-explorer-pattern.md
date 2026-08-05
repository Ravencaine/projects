---
created: 2026-08-02
updated: 2026-08-05
source: Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data.md
note_type: pattern
tags: [powerbi, visualization, user-experience, bookmarks, field-parameters]
---

# Visual Explorer Pattern

A report section that lets users choose what metric and dimension to analyze, and how to visualize it — without creating multiple static pages.

## Purpose

Empowers end users to explore data on their own terms. Instead of building dozens of near-identical report pages, give users a single "plug-in" section where they select metric, dimension, and chart type interactively. Reduces ad hoc requests to the report author.

## Components

- Two field parameters: `Metric` and `Dimension`
- Multiple overlapping visuals (bar, column, line, table, matrix) positioned in the same location
- One bookmark per visual type
- A bookmark navigator button group for switching between visuals
- Optional: dynamic chart title, conditional color logic, time context toggle, second dimension parameter for matrix columns

## Structure

### 1. Field Parameters

```
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

```
Dimension = {
    ("Region", NAMEOF('Sales'[Region]), 0),
    ("Category", NAMEOF('Sales'[Category]), 1),
    ("Customer Segment", NAMEOF('Sales'[Customer Segment]), 2),
    ("Product Type", NAMEOF('Sales'[Product Type]), 3),
    ("Sales Channel", NAMEOF('Sales'[Sales Channel]), 4)
}
```

### 2. Overlapping Visuals

Place bar, column, line, table, and matrix visuals in the same position on the canvas. Assign `Metric` to the Y-axis/value field and `Dimension` to the X-axis/rows field on each.

### 3. Bookmarks

Create one bookmark per visual type. In each bookmark, ensure **Data is unchecked** so slicer selections (field parameter choices) persist when switching visuals.

### 4. Bookmark Navigator

Add a bookmark navigator button group to the report canvas. Link each button to its corresponding bookmark. The navigator becomes the UI for switching chart types.

### 5. Dynamic Chart Title (optional)

Use a DAX measure that reads `ALLSELECTED('Metric')` and `ALLSELECTED('Dimension')` to build a dynamic title reflecting current selections.

### 6. Conditional Color (optional)

For variation or "vs target" metrics, color bars/columns green (positive) or red (negative) using a color measure applied via conditional formatting.

### 7. Time Context Toggle (optional)

A separate field parameter or slicer for time period (Last Year, Last Quarter, Last Month) connected to the UDF/Selected Period measures driving the metric values.

### 8. Matrix Column Selector (optional)

A second field parameter (`Dimension 2`) assigned to matrix columns — lets users set both row and column dimensions independently.

## Variations

- **Minimal:** One metric + one dimension + bar chart only — just field parameters and a single bookmark.
- **Standard:** Metric + Dimension + bar/column/line/table visuals with bookmark navigator.
- **Full-featured:** Adds dynamic title, conditional colors, time toggle, and matrix column selector.

## Related

- [[field-parameters-for-metric-dimension-selection]]
- [[bookmark-navigator-visual-switching]]
- [[dynamic-chart-title-from-field-parameters]]
- [[conditional-color-for-variation-metrics]]
- [[time-context-toggle-for-visual-explorer]]
