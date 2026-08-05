---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: function
tags: [dax, function, filter-context, calculate]
---

# CALCULATE() — Apply Filter Context to DAX Aggregations

`CALCULATE()` evaluates an expression under a modified filter context. It is the most important and most used DAX function for conditional aggregation.

## Signature

```dax
CALCULATE( <expression>, <filter1>, <filter2>, ... )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `<expression>` | scalar | The aggregation or expression to evaluate — typically a measure like `SUM(...)`, `[MeasureName]`, etc. |
| `<filter1>, <filter2>...` | boolean or table | One or more filter conditions. Multiple filters are combined with AND logic. |

## Returns

A scalar value — the result of the expression under the applied filter conditions.

## Examples

```dax
-- Total sales through the Store channel only
StoreSales := CALCULATE(
    SUM(dbo_FactSales[TotalSales]),
    dbo_DimChannel[ChannelName] = "Store"
)

-- Store sales for 2009 (filter on year extracted from DateKey text)
StoreSales2009 := CALCULATE(
    [StoreSales],
    LEFT(dbo_DimDate[Datekey], 4) = "2009"
)

-- Store sales for 2008
StoreSales2008 := CALCULATE(
    [StoreSales],
    LEFT(dbo_DimDate[Datekey], 4) = "2008"
)

-- Year-over-year growth: reference other calculated fields by wrapping in square brackets
SalesChange := ([StoreSales2009] - [StoreSales2008]) / [StoreSales2008]
```

## Notes

- `CALCULATE()` can take a previously-defined calculated field as its first argument — this is the chaining pattern
- Multiple filter arguments act as AND conditions: `CALCULATE(SUM(...), [Col1] = "A", [Col2] > 100)`
- The filter can be a table expression (e.g., `FILTER(Table, Condition)`) for more complex logic
- `CALCULATE()` creates a new filter context; any existing filters from the Pivot Table are replaced for the specified columns
- Without `CALCULATE()`, aggregation functions ignore the row context and aggregate the entire column

## Related

- [[dax-year-over-year]] — the complete YoY calculation pattern using CALCULATE chaining
- [[dax-sumx-function]] — for row-by-row expressions before aggregation
- [[calculated-column-vs-calculated-field]] — where CALCULATE is used (measures, not columns)
