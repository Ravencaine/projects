---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["record", "m-function"]
---


# Record.FieldValues

Returns a list of the field values in record record.

## Signature

```m
Record.FieldValues(record as record) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| record | record | |

## Returns

list

### Example 1

Find the field values in the record.

```m
Record.FieldValues([CustomerID = 1, Name = "Bob", Phone = "123-4567"])
```

// Output
```
{1, "Bob", "123-4567"}
```

