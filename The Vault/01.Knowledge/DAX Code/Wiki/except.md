---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, function, table, except, set-difference]
note_type: function

---

# EXCEPT — Set Difference

Returns rows from the left table that do not exist in the right table.

## Signature

```dax
EXCEPT( <LeftTable>, <RightTable> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| LeftTable | Table | Base table. |
| RightTable | Table | Table of rows to exclude. |

## Returns

Rows from the left table not present in the right table.

## Examples

```dax
New Customers :=
EXCEPT(
    CALCULATETABLE( VALUES( 'Customers'[CustomerID] ), 'Sales'[Year] = 2024 ),
    CALCULATETABLE( VALUES( 'Customers'[CustomerID] ), 'Sales'[Year] = 2023 )
)
```

## Notes

- Duplicates in the left table are retained
- Column names must match
- Order matters: EXCEPT(Left, Right) is not the same as EXCEPT(Right, Left)

## Related

- [[UNION]]
- [[intersect]]
