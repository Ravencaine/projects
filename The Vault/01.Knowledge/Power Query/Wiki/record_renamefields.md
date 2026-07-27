---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["record", "m-function"]
---


# Record.RenameFields

Returns a record after renaming fields in the input record to the new field names specified in list renames. For multiple renames, a nested list can be used ({ {old1, new1}, {old2, new2} }).

## Signature

```m
Record.RenameFields(
record as record,
renames as list,
optional missingField as nullable number
) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| record | record | |
| renames | list | |
| optional missingField | nullable number | |

## Returns

record

### Example 1

Rename the field "UnitPrice" to "Price" from the record.

```m
Record.RenameFields(
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", UnitPrice = 100.0],
{"UnitPrice", "Price"}
)
```

// Output
```
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0]
```

### Example 2

Rename the fields "UnitPrice" to "Price" and "OrderNum" to "OrderID" from the record.

```m
Record.RenameFields(
[OrderNum = 1, CustomerID = 1, Item = "Fishing rod", UnitPrice = 100.0],
{
{"UnitPrice", "Price"},
{"OrderNum", "OrderID"}
}
)
```

// Output
```
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0]
```

