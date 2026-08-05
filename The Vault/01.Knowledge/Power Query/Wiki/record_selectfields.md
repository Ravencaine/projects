---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["record", "m-function"]
---


# Record.SelectFields

Returns a record which includes only the fields specified in list fields from the input record.

## Signature

```m
Record.SelectFields(
record as record,
fields as any,
optional missingField as nullable number
) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| record | record | |
| fields | any | |
| optional missingField | nullable number | |

## Returns

record

### Example 1

Select the fields "Item" and "Price" in the record.

```m
Record.SelectFields(
[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],
{"Item", "Price"}
)
```

// Output
```
[Item = "Fishing rod", Price = 100]
```

