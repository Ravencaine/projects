---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["table", "m-function"]
---


# Table.AddColumn

Adds a column named newColumnName to the table table. The values for the column are computed using the specified selection function columnGenerator with each row taken as an input.

## Signature

```m
Table.AddColumn(
table as table,
newColumnName as text,
columnGenerator as function,
optional columnType as nullable type
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| newColumnName | text | |
| columnGenerator | function | |
| optional columnType | nullable type | |

## Returns

table

### Example 1

Add a number column named "TotalPrice" to the table, with each value being the sum of the [Price] and [Shipping] columns.

```m
Table.AddColumn(
Table.FromRecords({
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0,
Shipping = 10.00],
[OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0, Shipping
= 15.00],
[OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0, Shipping
= 10.00]
}),
"TotalPrice",
each [Price] + [Shipping],
type number
)
```

// Output
```
Power Query M
Table.FromRecords({
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100, Shipping =
10, TotalPrice = 110],
[OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5, Shipping = 15,
TotalPrice = 20],
[OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25, Shipping = 10,
TotalPrice = 35]
})
```

## Related

[[type_functions]]

