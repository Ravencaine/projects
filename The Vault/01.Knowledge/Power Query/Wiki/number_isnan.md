---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.IsNaN

Indicates if the value is NaN (Not a number). Returns true if number is equivalent to Number.NaN, false otherwise.

## Signature

```m
Number.IsNaN(number as number) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number | number | |

## Returns

logical

### Example 1

Check if 0 divided by 0 is NaN.

```m
Number.IsNaN(0/0)
```

// Output
```
true
```

### Example 2

Check if 1 divided by 0 is NaN.

```m
Number.IsNaN(1/0)
```

// Output
```
false
Last updated on 04/02/2026
```

