---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [value, m-function]
---


# Value.RemoveMetadata

Strips the input of metadata.

## Signature

```m
Value.RemoveMetadata(value as any, optional metaValue as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| optional metaValue | any | |

## Returns

any

### Example 1

Remove all metadata from a text value.

```m
Value.Metadata(
Value.RemoveMetadata("abc" meta [a = 1, b = 2])
)
```

// Output
```
[]
```

### Example 2

Remove only one field of metadata from a text value.

```m
Value.Metadata(
Value.RemoveMetadata("abc" meta [a = 1, b = 2], {"a"})
)
```

// Output
```
[b = 2]
```

