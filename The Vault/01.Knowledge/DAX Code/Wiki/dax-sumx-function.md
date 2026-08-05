---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: function
tags: [dax, function, iterator, row-context]
---

# SUMX() — Row-By-Row Iteration with Expression

`SUMX()` iterates through each row of a table, evaluates an expression for that row, and returns the sum of those per-row results.

## Signature

```dax
SUMX( <table>, <expression> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `<table>` | table or table expression | The table to iterate over — can be a physical table or `FILTER()` result |
| `<expression>` | scalar | The expression evaluated for each row — can reference any column in that row |

## Returns

A scalar number — the sum of the expression evaluated across all rows.

## Examples

```dax
-- Sum of UnitPrice × SalesQuantity for each row
testsumx := SUMX(
    dbo_FactSales,
    dbo_FactSales[UnitPrice] * dbo_FactSales[SalesQuantity]
)

-- Equivalent to: SUM(dbo_FactSales[UnitPrice] * dbo_FactSales[SalesQuantity])
-- ...but SUM cannot handle column × column multiplication without SUMX
```

## Notes

- `SUMX` is an **iterator**: it creates a row context for each row of the table and evaluates the expression in that context
- `SUMX(table, [Col1] * [Col2])` is equivalent to adding a calculated column `Col1 * Col2` then `SUM([NewCol])` — but SUMX does it in one step
- Use `SUMX` when the expression requires multiplying or combining columns that aren't already in a single column
- The table argument can be a filtered table: `SUMX(FILTER(dbo_FactSales, [SalesQuantity] > 0), [UnitPrice] * [SalesQuantity])`
- `SUMX` respects existing filter context — it first applies any Pivot Table filters, then iterates over the filtered rows

## Related

- [[dax-calculate-function]] — CALCULATE modifies filter context before SUMX iterates
- [[dax-is-column-oriented]] — understanding column references in row context
- [[dax-aggregate-functions-average-min-max]] — non-iterating aggregate functions
