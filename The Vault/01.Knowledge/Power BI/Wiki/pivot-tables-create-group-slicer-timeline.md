---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: workflow
tags: [pivot-table, excel, slicer, timeline]
---

# Pivot Tables: Create, Group by Month, Slicer, and Timeline

A step-by-step workflow for building Excel Pivot Tables with grouping, slicers, and timeline filters — covering the full analysis workflow from raw data to sliced summary.

## Prerequisites

- Excel 2013 or later with data in a table (Ctrl+T to create a table)
- Data should have date fields, categorical fields, and numeric measures

## Steps

1. **Create the Pivot Table**
   - Select any cell in the data range
   - Go to Insert → PivotTable → OK (accept default: new worksheet)
   - Drag fields to Rows, Columns, Values, and Filters boxes in the PivotTable Fields pane

2. **Group by Month (Date Column)**
   - Right-click any cell in the date column
   - Select Group → choose Months from the Grouping window → OK
   - The date field groups into months automatically

3. **Group by Day of Week**
   - Insert a new column next to the date column
   - Enter formula `=TEXT(A3,"dddd")` in the first cell — Excel Tables auto-copy down
   - Add this column to the Pivot Table as a row field alongside the model/category

4. **Add Subtotals and Grand Totals**
   - Go to PivotTable Tools → Design → Subtotals
   - Options: Do not show / Show at bottom / Show at top
   - Grand Totals: Off / On for rows and columns / On for rows only / On for columns only

5. **Add a Slicer (Categorical Filter)**
   - Go to PivotTable Tools → Analyze → Insert Slicer
   - Select the fields to slice (e.g., salesperson, product)
   - Click a value in the slicer to filter; use the slicer header dropdown for additional options

6. **Add a Timeline (Date Filter)**
   - Go to PivotTable Tools → Analyze → Insert Timeline
   - Select the date field
   - Use the dropdown at the top of the Timeline to switch between Years / Quarters / Months / Days
   - Slicers and Timelines can work together simultaneously

7. **Create a Pivot Chart**
   - With the Pivot Table visible, go to PivotTable Tools → Analyze → PivotChart
   - Select chart type (stacked column is common) → OK
   - The chart is linked to the Pivot Table and updates with slicer/timeline filters

## Variations

- **Multi-level breakdown:** Drag two fields to Rows (e.g., sell date then salesperson) for hierarchical row structure
- **Value filtering:** Click the arrow next to a field in the Rows box → Value Filters → configure threshold conditions
- **Azure Marketplace data:** Import external data directly into a Pivot Table via Data → From Other Sources → Azure Marketplace

## Related

- [[pivot-charts-from-pivot-tables]] — converting Pivot Tables to Pivot Charts
- [[excel-analysis-toolpak-descriptive-statistics-histogram]] — statistical analysis on Pivot Table data
