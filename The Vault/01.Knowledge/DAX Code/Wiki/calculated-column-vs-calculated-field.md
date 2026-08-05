---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: atomic
tags: [dax, calculated-column, calculated-field, measure]
---

# Calculated Column vs. Calculated Field (Measure) in DAX

DAX expressions live in one of two locations in a PowerPivot table, each with different evaluation context and use cases.

## Definition

- **Calculated column:** A new column added to an existing PowerPivot table. The formula evaluates for every row individually (row context). The result is stored in the table — one value per row.
- **Calculated field (measure):** A formula placed in the calculation area at the bottom of the PowerPivot window. The formula evaluates in the current filter context — it aggregates across all rows that pass the current filter. No value is stored; it recalculates on every Pivot Table interaction.

Dunlop (Ch7): "Calculated columns can be added to an existing PowerPivot table. When a column contains a formula, the value is calculated for each row. ... Calculated fields or measures are placed in the calculation area at the bottom of the PowerPivot window."

## Key Points

- Calculated columns add a new physical column to the table — useful for intermediate values that need to be sliced/filtered (e.g., `Profit/Sales` per row)
- Calculated fields are not stored in the table — they exist only in the measure context of a Pivot Table or Power View report
- Calculated fields often use aggregation functions (SUM, AVERAGE) that reference entire columns
- Same-name conflict: Dunlop's caution — avoid giving a calculated field and a calculated column the same name
- Calculated fields can reference other calculated fields (chaining): `StoreSales2009` references `[StoreSales]`

## Examples

```dax
-- Calculated column: Profit/Sales per row
Profit/Sales := [TotalProfit] / [TotalSales]
-- Right-click column → Rename Column → "Profit/Sales"
-- Format as Percentage

-- Calculated field: average of the Profit/Sales column
Average of Profit/Sales := AVERAGE([Profit/Sales])

-- Calculated field referencing another calculated field
SalesChange := ([StoreSales2009] - [StoreSales2008]) / [StoreSales2008]
```

## Related

- [[dax-is-column-oriented]] — the foundational column-reference model
- [[dax-calculate-function]] — the most common measure function
- [[dax-kpi-create-key-performance-indicator]] — KPIs require a calculated field as the base metric
