---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, function, table, groupby, aggregation]
note_type: function

---

# GROUPBY — Manual Grouping in Iterators

Groups rows and computes aggregations within iterator functions.

## Signature

```dax
GROUPBY( <Table>, [<GroupBy_Column1>], [<Name1>, <Expression1>], ... )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Table | Table | Table to group. |
| GroupBy_Column | Column | Column to group by. |
| Name | Text | Output column name. |
| Expression | Any | Expression evaluated per group. |

## Examples

```dax
Category Summary :=
GROUPBY(
    'Sales',
    'Sales'[Category],
    "Total", SUMX( CURRENTGROUP(), 'Sales'[Amount] )
)
```

## Notes

- Requires SUMX(CURRENTGROUP(), ...) for aggregations inside GROUPBY
- CURRENTGROUP() refers to the current group within the iterator
- Use SUMMARIZECOLUMNS() instead for simpler syntax

## Related

- [[SUMMARIZECOLUMNS]]
- [[SELECTCOLUMNS]]
