---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: function
tags: [dax, function, aggregate, average, min, max]
---

# AVERAGE(), MIN(), MAX() — DAX Aggregate Measures

These three DAX aggregation functions operate on entire columns (or column expressions) and return a single scalar value. They are the most commonly used functions when building calculated fields in the PowerPivot calculation area.

## Signature

```dax
AVERAGE( <column> )
MIN( <column> )
MAX( <column> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `<column>` | column reference | The column to aggregate. Must be a numeric or date column. |

## Returns

| Function | Returns |
|----------|---------|
| `AVERAGE` | Arithmetic mean of all non-blank values in the column |
| `MIN` | The smallest value in the column |
| `MAX` | The largest value in the column |

## Examples

```dax
-- Using AutoSum to create these is faster: click a cell in the calculation area,
-- double-click AutoSum → creates SUM; click arrow next to AutoSum → pick AVERAGE/MIN/MAX

-- Manually enter in the calculation area:
Average of Total Profits := AVERAGE(dbo_FactSales[TotalProfit])
Average of Profit/Sales := AVERAGE([Profit/Sales])

-- Average of Profit/Sales as a KPI base metric
Average of Profit/Sales := AVERAGE([Profit/Sales])

-- KPI: right-click → Create KPI → set target value (e.g., 0.53 for 53%)
```

## Notes

- These functions ignore blank rows — they only aggregate non-empty values
- In the calculation area, clicking AutoSum and selecting a function creates the measure with a default identifier label (e.g., "Sum of Total Profits")
- The identifier acts as both a display label and a variable name — reference it in other formulas as `[Sum of Total Profits]`
- Use `AVERAGEA()` if you want to treat text zeros as 0 (AVERAGE ignores text entirely)

## Related

- [[dax-sumx-function]] — SUMX for row-by-row expressions before aggregation
- [[calculated-column-vs-calculated-field]] — where to place these in PowerPivot
- [[dax-kpi-create-key-performance-indicator]] — AVERAGE as the base metric for KPI creation
