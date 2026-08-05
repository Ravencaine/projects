---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["record", "m-function"]
---


# Record.AddField

Adds a field to a record record, given the name of the field fieldName and the value value.

## Signature

```m
Record.AddField(
record as record,
fieldName as text,
value as any,
optional delayed as nullable logical
) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| record | record | |
| fieldName | text | |
| value | any | |
| optional delayed | nullable logical | |

## Returns

record

### Example 1

Add the field Address to the record.

```m
Record.AddField([CustomerID = 1, Name = "Bob", Phone = "123-4567"], "Address",
"123 Main St.")
```

// Output
```
[CustomerID = 1, Name = "Bob", Phone = "123-4567", Address = "123 Main St."]
```

