---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: pattern
tags: [pivot-chart, excel, visualization]
---

# Pivot Charts from Pivot Tables

Converting a Pivot Table into a chart so that sliced and filtered data is displayed visually. The chart inherits the Pivot Table's row/column structure and responds to slicer and timeline filters.

## Purpose

Pivot Charts provide visual representation of the same data that drives the Pivot Table — without needing to rebuild the data model. Useful for presentations, dashboards, and spotting trends that are hard to see in a grid.

## Components

- An existing Pivot Table with fields assigned to Rows, Columns, Values
- Excel PivotTable Tools → Analyze ribbon

## Structure

1. Click anywhere inside the Pivot Table
2. PivotTable Tools → Analyze → PivotChart
3. Select chart type from Insert Chart dialog:
   - **Clustered Column:** side-by-side bars per category
   - **Stacked Column:** bars stacked, showing total + composition
   - **Line:** time-series trends
   - **Pie:** composition of a whole (use sparingly — hard to read)
4. Click OK — the chart is placed on the same or a new sheet

## Example

- Pivot Table showing sales by day of week and product model → Stacked Column Chart → each bar shows total sales for that day, segments show product breakdown
- Click a slicer value (e.g., specific salesperson) → the chart updates to show only that salesperson's data

## Variations

- **Copy and chart separately:** Right-click table → Copy → paste in blank area → create chart from the copy. This decouples the chart from the Pivot Table if a static snapshot is needed.
- **Pop-out chart:** Click the pop-out icon in the upper-right corner of the chart to enlarge it to full screen

## Notes

- Every chart type has a Pivot Chart equivalent (except 3D charts — not available)
- Right-click the chart → Select Data to manually adjust the series and axis labels

## Related

- [[pivot-tables-create-group-slicer-timeline]] — the upstream workflow
- [[scatter-chart-with-r-squared-trendline]] — a non-pivot chart pattern for correlation analysis
