---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["value", "m-function"]
---


# Value.Type

Returns the type of the given value. value: The value whose type is returned.

## Signature

```m
Value.Type(value as any) as type
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |

## Returns

type

### Example 1

Return the type of the specified number.

```m
Value.Type(243.448)
```

// Output
```
type number
```

### Example 2

Return the type of the specified date.

```m
Value.Type(#datetime(2010, 12, 31))
```

// Output
```
type date
```

### Example 3

Return the type of the specified record.

```m
Value.Type([a = 1, b = 2])
```

// Output
```
type record
```

## Related

[[type_functions]]

