---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [record, m-function]
---


# Record.HasFields

Indicates whether the record record has the fields specified in fields, by returning a logical value (true or false). Multiple field values can be specified using a list.

## Signature

```m
Record.HasFields(record as record, fields as any) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| record | record | |
| fields | any | |

## Returns

logical

### Example 1

Check if the record has the field "CustomerID".

```m
Record.HasFields([CustomerID = 1, Name = "Bob", Phone = "123-4567"], "CustomerID")
```

// Output
```
true
```

### Example 2

Check if the record has the field "CustomerID" and "Address".

```m
Record.HasFields([CustomerID = 1, Name = "Bob", Phone = "123-4567"],
{"CustomerID", "Address"})
```

// Output
```
false
```

