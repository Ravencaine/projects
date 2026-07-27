---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.Cos

Returns the cosine of the specified angle. number: An angle, measured in radians.

## Signature

```m
Number.Cos(number as nullable number) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number | nullable number | |

## Returns

nullable number

### Example 1

Find the cosine of the angle 0.

```m
Number.Cos(0)
```

// Output
```
1
```

### Example 2

Find the cosine of π radians.

```m
Number.Cos(Number.PI)
```

// Output
```
-1
```

