---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["type", "m-function"]
---


# Type.Is

Determines if a value of type1 is always compatible with type2. Parameter type2 should be a primitive (or nullable primitive) type value. Otherwise, this function's behavior is undefined and shouldn't be relied on.

## Signature

```m
Type.Is(type1 as type, type2 as type) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| type1 | type | |
| type2 | type | |

## Returns

logical

### Example 1

Determine if a value of type number can always also be treated as type any.

```m
Type.Is(type number, type any)
```

// Output
```
true
```

### Example 2

Determine if a value of type any can always also be treated as type number.

```m
Type.Is(type any, type number)
```

// Output
```
false
```

## Related

[[type_functions]]

