---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["value", "m-function"]
---


# Value.As

Returns the value if it's compatible with the specified type. This is equivalent to the "as" operator in M, with the exception that it can accept identifier type references such as Number.Type.

## Signature

```m
Value.As(value as any, type as type) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| type | type | |

## Returns

any

### Example 1

Cast a number to a number.

```m
Value.As(123, Number.Type)
```

// Output
```
123
```

### Example 2

Attempt to cast a text value to a number.

```m
Value.As("abc", type number)
```

// Output
```
[Expression.Error] We cannot convert the value "abc" to type Number.
```

