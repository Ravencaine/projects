---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: pattern
tags: [power-view, power-bi, report, visualization]
---

# Power View Reports: Table, Matrix, Bar Chart, and Map

Power View (Excel 2013, predecessor to Power BI) provides an interactive report canvas where tables, matrices, and charts are built by selecting fields — no formula or coding required.

## Purpose

Power View enables rapid, drag-and-drop report creation from data already loaded into PowerPivot. It automatically infers table relationships and supports multi-table reporting. It was the direct ancestor of Power BI's report view.

## Components

- PowerPivot data model with loaded tables and defined relationships
- Excel Insert → Power View Reports ribbon

## Structure

1. **Open Power View sheet:** Insert → Power View Reports
2. **Create a Table:** Click fields in the Power View Fields pane — they appear as columns in a table
3. **Add a relationship field:** Drag a field from a related table to the Values area — Power View prompts to create the relationship if one doesn't exist
4. **Set aggregation:** Click the arrow next to a numeric field → select Sum, Count, Average, or Do Not Summarize
5. **Switch to Matrix view:** Design → Table → Matrix
6. **Add a Bar Chart:** Design → Bar Chart → Stacked / Clustered
7. **Add a Map:** Click a geographic field (City, Country, State) — Power View auto-detects and inserts a map; drag numeric fields to Size or Color
8. **Add Filters:** Drag fields to the Filters pane — drag to the axis to filter by threshold (greater than, less than)
9. **Pop-out:** Click the pop-out icon in the upper-right corner for full-screen view

## Example

1. Select Company and City from the Customers table → Table appears
2. Drag Price Total from Order Price Totals table → prompts for relationship creation on Order ID
3. Set Price Total to "Do Not Summarize" → shows individual order values per company
4. Add a matrix view → rows = company, columns = city, values = order total
5. Add Map: select Country and State fields → Bing map auto-renders; drag Sales to Size

## Variations

- **Multi-table charts:** Charts automatically inherit the relationship chain — selecting from three related tables builds a chart that spans all three
- **Filtering out zero values:** Drag the measure to Filters pane → set threshold to ≥ 1 to hide rows with no orders

## Related

- [[pivot-charts-from-pivot-tables]] — the Excel-native alternative
- [[hdinsight-power-query-pivot-table-power-map-pipeline]] — the Azure → Power Query → Power Map end-to-end pipeline
