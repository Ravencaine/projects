---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["record", "m-function"]
---


# Record.FromList

Returns a record given a list of field values and a set of fields. The fields can be specified either by a list of text values, or a record type. An error is thrown if the fields are not unique.

## Signature

```m
Record.FromList(list as list, fields as any) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| fields | any | |

## Returns

record

### Example 1

Build a record from a list of field values and a list of field names.

```m
Record.FromList({1, "Bob", "123-4567"}, {"CustomerID", "Name", "Phone"})
```

// Output
```
[CustomerID = 1, Name = "Bob", Phone = "123-4567"]
```

### Example 2

Build a record from a list of field values and a record type.

```m
Record.FromList({1, "Bob", "123-4567"}, type [CustomerID = number, Name = text,
Phone = number])
```

// Output
```
[CustomerID = 1, Name = "Bob", Phone = "123-4567"]
```

