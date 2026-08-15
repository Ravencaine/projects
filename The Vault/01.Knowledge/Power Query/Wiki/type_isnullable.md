---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [type, m-function]
---


# Type.IsNullable

Returns true if a type is a nullable type; otherwise, false.

## Signature

```m
Type.IsNullable(type as type) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| type | type | |

## Returns

logical

### Example 1

Determine if number is nullable.

```m
Type.IsNullable(type number)
```

// Output
```
false
```

### Example 2

Determine if type nullable number is nullable.

```m
Type.IsNullable(type nullable number)
```

// Output
```
true
```

## Related

[[type_functions]]

