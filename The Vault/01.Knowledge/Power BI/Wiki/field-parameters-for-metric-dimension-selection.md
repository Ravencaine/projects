---
created: 2026-08-02
updated: 2026-08-05
source: Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data.md
note_type: pattern
tags: [powerbi, field-parameters, dynamic-measures, user-defined-functions]
---

# Field Parameters for Metric and Dimension Selection

Two field parameters — one for the metric to display, one for the dimension to slice by — enable users to dynamically change what a visual shows without modifying the report.

## Purpose

Field parameters (Power BI November 2023+) allow a single visual to swap its underlying measure or column at runtime based on user selection. Pairing a `Metric` parameter with a `Dimension` parameter lets users explore any metric by any category without needing multiple visuals or pages.

## Components

- `Metric` field parameter — references pre-built DAX measures (must exist in the model)
- `Dimension` field parameter — references columns from dimension tables
- Each tuple: `(Label, NAMEOF(Reference), SortOrder)`
- Slicers bound to each parameter for interactive selection

## Structure

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

## Key Rules

- The referenced measures must already exist in the model — field parameters cannot create new measures, only select existing ones.
- Measures driven by a UDF (User Defined Function) pattern — with a `Selected Period` argument — work well here, allowing the metric to also respond to a time period slicer.
- The sort order integer controls the order of options in the slicer, independent of alphabetical order.

## Related

- [[visual-explorer-pattern]]
- [[dynamic-chart-title-from-field-parameters]]
