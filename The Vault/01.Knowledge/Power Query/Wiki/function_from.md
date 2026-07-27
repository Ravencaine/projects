---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["function", "m-function"]
---


# Function.From

Takes a unary function function and creates a new function with the type functionType that constructs a list out of its arguments and passes it to function.

## Signature

```m
Function.From(functionType as type, function as function) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| functionType | type | |
| function | function | |

## Returns

function

### Example 1

Converts List.Sum into a two-argument function whose arguments are added together.

```m
Function.From(type function (a as number, b as number) as number, List.Sum)(2, 1)
```

// Output
```
3
```

### Example 2

Converts a function taking a list into a two-argument function.

```m
Function.From(type function (a as text, b as text) as text, (list) => list{0} &
list{1})("2", "1")
```

// Output
```
"21"
```

