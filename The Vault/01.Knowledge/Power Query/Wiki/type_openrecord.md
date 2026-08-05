---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["type", "m-function"]
---


# Type.OpenRecord

Returns an opened version of the given record type (or the same type, if it is already opened).

## Signature

```m
Type.OpenRecord(type as type) as type
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| type | type | |

## Returns

type

### Example 1

Create an opened version of type [ A = number].

```m
Type.OpenRecord(type [A = number])
```

// Output
```
type [A = number, ...]
```

## Related

[[type_functions]]

