---
created: 2026-07-26
updated: 2026-08-02
source: "Beyond VLOOKUP: Unleashing Excel's True Data Power for Business Analysis"
source_url: https://medium.com/@harsh1995hg/beyond-vlookup-unleashing-excels-true-data-power-for-business-analysis-33e9c54a66c4
note_type: function
tags: [excel, pivot-tables, aggregation, reporting]
---

# Pivot Tables

An interactive table that aggregates, counts, averages, or sums data across categories instantly — no formulas required.

## Signature

```
Insert → Pivot Table
```

Select a data range or an existing table/query, then choose where to place the output (new sheet or existing sheet).

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Data range | Table/Range | The source data to analyse |
| Destination | Sheet location | Where the pivot table is placed |
| Fields | Drag-and-drop | Rows, Columns, Values, Filters |

## Returns

A dynamic cross-tabulation of the source data. The output updates automatically when fields are added, removed, or reconfigured.

## Examples

**Sales by region:**
1. Drag "Region" to Rows.
2. Drag "Sales Amount" to Values — it auto-sums.
3. Result: one row per region with total sales.

**Month-over-month change:**
1. Drag "Month" to Columns.
2. Drag "Revenue" to Values (set to Sum).
3. Add a calculated field: `=[Current Month] - [Prior Month]`.

**Dynamic filtering:**
1. Drag "Product Category" to Filters.
2. The field appears as a dropdown above the table — select a category to slice all values at once.

## Notes

- Pivot Tables require data in a **flat, tabular structure**: one row per record, one column per attribute. Messy source data should be cleaned in Power Query first.
- Refreshing the underlying data does not automatically refresh the pivot table — right-click the table and select "Refresh," or use "Refresh All" from the Data tab.
- Calculated fields operate on the *aggregated* values, not the raw rows. For row-level calculations, add a calculated column to the source data instead.

## Related

- [[power-query-etl-workflow]] — clean the source data before pivoting
- [[conditional-formatting]] — apply visual formatting to pivot table values
- [[excel-as-bi-tool]] — pivot tables as a BI reporting capability
