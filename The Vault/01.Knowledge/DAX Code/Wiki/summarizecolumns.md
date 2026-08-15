---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, function, table, summarize, aggregation]
note_type: function

---

# SUMMARIZECOLUMNS — Aggregation Table

Creates a summary table with grouped rows and optional aggregations.

## Signature

```dax
SUMMARIZECOLUMNS( <Column1>, [<Column2>...], [<FilterTable>], [<Name>, <Expression>...] )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Column | Column | Columns to group by. |
| FilterTable | Table | Filter to apply. Optional. |
| Name | Text | Column name for aggregation result. |
| Expression | Any | Aggregation expression. |

## Examples

```dax
Summary :=
SUMMARIZECOLUMNS(
    'Product'[Category],
    'Date'[Year],
    "Total Sales", SUM( 'Sales'[Amount] ),
    "Avg Price", AVERAGE( 'Sales'[Price] )
)
```

## Notes

- More efficient than SUMMARIZE for many use cases
- Automatically removes blank combinations
- Does not require ROLLUP for subtotals

## Related

- [[GROUPBY]]
- [[SELECTCOLUMNS]]
