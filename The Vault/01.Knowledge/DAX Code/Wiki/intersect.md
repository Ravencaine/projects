---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, function, table, intersect, set]
note_type: function

---

# INTERSECT — Row Overlap

Returns the rows that appear in both tables.

## Signature

```dax
INTERSECT( <LeftTable>, <RightTable> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| LeftTable | Table | First table. |
| RightTable | Table | Table to intersect with. |

## Returns

Rows that exist in both tables.

## Examples

```dax
Common Customers :=
INTERSECT(
    CALCULATETABLE( VALUES( 'Customers'[CustomerID] ), 'Sales'[Year] = 2024 ),
    CALCULATETABLE( VALUES( 'Customers'[CustomerID] ), 'Sales'[Year] = 2023 )
)
```

## Notes

- Matches by column values, not row position
- Column names must match across tables

## Related

- [[UNION]]
- [[except]]
