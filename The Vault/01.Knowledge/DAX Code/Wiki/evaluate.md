---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "function", "query", "evaluate", "dax-studio"]
note_type: function

---

# EVALUATE — DAX Query Execution

Returns a table from a DAX query. Used in DAX Studio, SSMS, and direct queries.

## Signature

```dax
EVALUATE <TableExpression>
```

## Examples

```dax
EVALUATE
SUMMARIZECOLUMNS(
    'Product'[Category],
    "Sales", SUM( 'Sales'[Amount] )
)
ORDER BY [Sales] DESC
```

## Notes

- `EVALUATE` is the DAX equivalent of `SELECT` in SQL
- Combine with `ORDER BY`, `START AT`, `TOPN`
- Used in DAX Studio for testing queries before embedding in Power BI

## Related

- [[dax-performance-optimization-techniques]]
- [[performance-analyzer-debugging]]
