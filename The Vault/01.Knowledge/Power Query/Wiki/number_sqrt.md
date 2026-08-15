---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [number, m-function]
---


# Number.Sqrt

Returns the square root of number. If number is null, Number.Sqrt returns null. If it is a negative value, Number.NaN is returned (Not a number).

## Signature

```m
Number.Sqrt(number as nullable number) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number | nullable number | |

## Returns

nullable number

### Example 1

Find the square root of 625.

```m
Number.Sqrt(625)
```

// Output
```
25
```

### Example 2

Find the square root of 85.

```m
Number.Sqrt(85)
```

// Output
```
9.2195444572928871
```

