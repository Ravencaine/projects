---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [record, m-function]
---


# Record.ToTable

Returns a table containing the columns Name and Value with a row for each field in record.

## Signature

```m
Record.ToTable(record as record) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| record | record | |

## Returns

table

### Example 1

Return the table from the record.

```m
Record.ToTable([OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0])
```

// Output
```
Table.FromRecords({
[Name = "OrderID", Value = 1],
[Name = "CustomerID", Value = 1],
[Name = "Item", Value = "Fishing rod"],
[Name = "Price", Value = 100]
})
```

