---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["type", "m-function"]
---


# Type.RecordFields

Returns a record describing the fields of a record type. Each field of the returned record type has a corresponding name and a value, in the form of a record [ Type = type, Optional = logical ].

## Signature

```m
Type.RecordFields(type as type) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| type | type | |

## Returns

record

### Example 1

Find the name and value of the record [ A = number, optional B = any].

```m
Type.RecordFields(type [A = number, optional B = any])
```

// Output
```
[
A = [Type = type number, Optional = false],
B = [Type = type any, Optional = true]
]
```

## Related

[[type_functions]]

