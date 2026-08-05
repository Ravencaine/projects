---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "function", "table", "union", "combine"]
note_type: function

---

# UNION — Combine Tables

Stacks two or more tables vertically, keeping all rows.

## Signature

```dax
UNION( <Table1>, <Table2>, ... )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Table1, Table2, ... | Table | Tables to combine. Must have the same number of columns. |

## Returns

A table containing all rows from each input table.

## Examples

```dax
Combined :=
UNION(
    FILTER( 'Sales', 'Sales'[Region] = "North" ),
    FILTER( 'Sales', 'Sales'[Region] = "South" )
)
```

## Notes

- Columns are matched by position, not name
- Duplicate rows are retained
- Use DISTINCT(UNION(...)) to remove duplicates
- All input tables must have the same column count

## Related

- [[intersect]]
- [[except]]
- [[SUMMARIZECOLUMNS]]
