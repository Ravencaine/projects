---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "function", "statistics", "median", "iterator"]
note_type: function

---

# MEDIANX — Iterator-based Median

Returns the median of values from a table expression. Iterator function.

## Signature

```dax
MEDIANX( <Table>, <Expression> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Table | Table | Table or filtered table to iterate. |
| Expression | Number | Numeric expression evaluated per row. |

## Returns

The median (middle value when sorted) of the expression results.

## Examples

```dax
Median Price := MEDIANX( 'Products', 'Products'[Price] )
Median Sales by Category := MEDIANX( FILTER( 'Sales', 'Sales'[Category] = "Electronics" ), 'Sales'[Amount] )
```

## Notes

- Automatically ignores BLANK values
- For filtered context, wrap the table in `FILTER()`
- Returns BLANK if the result set is empty
- Use `MEDIAN()` for simple column aggregation

## Related

- [[better-median-workaround-in-dax]]
- [[stdevx.p]]
