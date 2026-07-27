---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["record", "m-function"]
---


# Record.FieldNames

Returns the names of the fields in the record record as text.

## Signature

```m
Record.FieldNames(record as record) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| record | record | |

## Returns

list

### Example 1

Find the names of the fields in the record.

```m
Record.FieldNames([OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price =
100.0])
```

// Output
```
{"OrderID", "CustomerID", "Item", "Price"}
```

