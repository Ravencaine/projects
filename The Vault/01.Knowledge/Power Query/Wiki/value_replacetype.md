---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["value", "m-function"]
---


# Value.ReplaceType

Replaces the value's type with the provided type.

## Signature

```m
Value.ReplaceType(value as any, type as type) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| type | type | |

## Returns

any

### Example 1

Replace the default type of a record with a more specific type.

```m
Type.RecordFields(
Value.Type(
Value.ReplaceType(
[Column1 = 123],
type [Column1 = number]
)
)
)[Column1][Type]
```

// Output
```
type number
```

