---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["expression", "m-function"]
---


# Expression.Constant

Returns the M source code representation of a constant value.

## Signature

```m
Expression.Constant(value as any) as text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |

## Returns

text

### Example 1

Get the M source code representation of a number value.

```m
Expression.Constant(123)
```

// Output
```
"123"
```

### Example 2

Get the M source code representation of a date value.

```m
Expression.Constant(#date(2035, 01, 02))
```

// Output
```
"#date(2035, 1, 2)"
```

### Example 3

Get the M source code representation of a text value.

```m
Expression.Constant("abc")
```

// Output
```
"""abc"""
```

