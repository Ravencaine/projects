---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["record", "m-function"]
---


# Record.RemoveFields

Returns a record that removes all the fields specified in list fields from the input record. If the field specified does not exist, an error is raised.

## Signature

```m
Record.RemoveFields(
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

Remove the field "Price" from the record.

```m
Record.RemoveFields([CustomerID = 1, Item = "Fishing rod", Price = 18.00], "Price")
```

// Output
```
[CustomerID = 1, Item = "Fishing rod"]
```

### Example 2

Remove the fields "Price" and "Item" from the record.

```m
Record.RemoveFields([CustomerID = 1, Item = "Fishing rod", Price = 18.00], {"Price",
"Item"})
```

// Output
```
[CustomerID = 1]
Last updated on 01/22/2026
```

