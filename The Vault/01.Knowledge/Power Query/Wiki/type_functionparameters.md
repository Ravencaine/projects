---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [type, m-function]
---


# Type.FunctionParameters

Returns a record with field values set to the name of the parameters of type, and their values set to their corresponding types.

## Signature

```m
Type.FunctionParameters(type as type) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| type | type | |

## Returns

record

### Example 1

Find the types of the parameters to the function (x as number, y as text).

```m
Type.FunctionParameters(type function (x as number, y as text) as any)
```

// Output
```
[x = type number, y = type text]
```

