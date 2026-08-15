---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [record, m-function]
---


# Record.FieldOrDefault

Returns the value of the specified field field in the record record. If the field is not found, the optional defaultValue is returned.

## Signature

```m
Record.FieldOrDefault(
record as nullable record,
field as text,
optional defaultValue as any
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| record | nullable record | |
| field | text | |
| optional defaultValue | any | |

## Returns

any

### Example 1

Find the value of field "Phone" in the record, or return null if it doesn't exist.

```m
Record.FieldOrDefault([CustomerID = 1, Name = "Bob"], "Phone")
```

// Output
```
null
```

### Example 2

Find the value of field "Phone" in the record, or return the default if it doesn't exist.

```m
Record.FieldOrDefault([CustomerID = 1, Name = "Bob"], "Phone", "123-4567")
```

// Output
```
"123-4567"
```

