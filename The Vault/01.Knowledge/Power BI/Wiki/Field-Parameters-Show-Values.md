---
created: 2026-08-08
updated: 2026-08-08
source: "5 Power BI Slicer Tricks To Build Professional Dashboards"
source_url: https://www.youtube.com/watch?v=sdyxtL1250E
note_type: pattern
tags: [power-bi, slicers, field-parameters]
---

# Field Parameters: Show Values of Selected Field

Use Field Parameters to add a secondary slicer that displays the **values** of the selected column (not just the column names).

## Purpose

A standard Field Parameter slicer lets users switch between columns (e.g., Region vs Channel). This pattern adds a second slicer that dynamically shows the values of whichever column the first slicer selected — enabling value-level filtering on top of field-level switching.

## Components

1. **Field Parameter:** created via Modeling tab → New Parameter → Fields
2. **Primary slicer:** switches between column names (standard Field Parameter behaviour)
3. **Secondary slicer:** set to "Show values of the selected field" to display column values
4. **Visual:** receives the selected column from the primary slicer

## Structure

### Step 1 — Create Field Parameter

```
Modeling tab → New Parameter → Fields
Name: KPI (or any name)
Columns: Channel, Region
→ Add slicer to page
→ Click Create
```

### Step 2 — Configure Primary Slicer

- Add the Field Parameter column to the visual → slicer toggles between Channel and Region

### Step 3 — Configure Secondary Slicer (Show Values)

```
Ctrl + click the primary slicer to duplicate it
Select the duplicated slicer
In the slicer settings:
  → Columns → Show values of the selected field
```

Now the secondary slicer displays the actual values (e.g., East, West, North) of whichever column the primary slicer selected.

## Example

1. Primary slicer: Channel / Region (column-level toggle)
2. Secondary slicer: East / West / North (value-level filter for selected column)
3. User selects "Region" in primary slicer → secondary slicer updates to show region values
4. Further filter: user selects "East" in secondary slicer → visual filters to East

## Variations

- **Multiple columns:** Works with any number of columns in the Field Parameter
- **Numeric ranges:** Combine with a What-If parameter for numeric value ranges
- **Cross-filter chain:** Chain multiple Show Values slicers for drill-down filtering

## Related

- [[Field-Parameters-KPI-Hierarchy]] — extending Field Parameters with hierarchy/tag columns
