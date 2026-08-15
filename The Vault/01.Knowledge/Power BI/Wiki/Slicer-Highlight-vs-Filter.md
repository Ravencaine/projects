---
created: 2026-08-08
updated: 2026-08-08
source: "5 Power BI Slicer Tricks To Build Professional Dashboards"
source_url: https://www.youtube.com/watch?v=sdyxtL1250E
note_type: pattern
tags: [power-bi, slicers, disconnected-table, conditional-formatting, highlight]
related:
  - "[[Disconnected-Table-Slicer-Pattern]]"
  - "[[Slicer-Highlight-Measure-IN-VALUES-Snippet]]"
---

# Slicer Highlight vs Filter

Use a disconnected table to make a slicer **highlight** matching rows instead of **filtering** them out. Requires a disconnected table, a DAX measure with `SELECTEDVALUE` + `IN VALUES`, and conditional formatting.

## Purpose

Standard slicers filter data — rows not matching the slicer selection disappear. This pattern highlights matching rows in a distinct color while keeping non-matching rows visible. Useful for comparison views, partial highlights in tables, or emphasis in bar/column charts.

## Components

1. **Disconnected table:** unconnected to the data model, populated with values from the target column
2. **DAX measure:** checks whether each row's value is selected in the disconnected table slicer
3. **Conditional formatting:** applies background/text color based on the measure output
4. **Slicer:** built on the disconnected table column (not the related dimension table)

## Structure

### Step 1 — Create Disconnected Table

Power Query (M code):
```m
= Table.Distinct(
    Table.SelectColumns(
        SourceTable,
        {"Product"}
    )
)
```
Removes blanks, creates a single-column table with unique values.

### Step 2 — DAX Measure for Highlight Detection

```dax
Highlight =
VAR Check =
    COUNTROWS(
        FILTER(
            'Products',           -- connected dimension table
            'Products'[Product]
                IN VALUES('Products_Disconnected'[Product])  -- slicer values
        )
    )
RETURN
    IF(Check >= 1, 1, 0)
```

### Step 3 — Conditional Formatting

1. Add the `Highlight` measure to the visual
2. Format the target field (e.g., Total Sales, Product Name) → Cell Elements → Background Color → Field value → select `Highlight`
3. Apply to each column in the visual for full-row highlighting

## Example

- Table: Product Name | Total Sales
- Slicer: disconnected Product column
- Select "Bike Wash Dissolver" in slicer → row highlights in orange; non-matching rows remain visible but unhighlighted
- Select multiple products → all matching rows highlight simultaneously

## Variations

- **Text color:** Use the same measure with Font Color instead of Background Color
- **Bar/column charts:** Apply conditional formatting to the bar/column fill based on the Highlight measure
- **Multiple columns:** Apply the same measure to multiple fields for consistent row-level highlighting

See also [[Conditional-Formatting-in-Power-BI]] for the conditional formatting mechanics.

## Related

- [[Disconnected-Table-Slicer-Pattern]] — general pattern for disconnected tables
- [[Slicer-Highlight-Measure-IN-VALUES-Snippet]] — DAX boilerplate for the measure
