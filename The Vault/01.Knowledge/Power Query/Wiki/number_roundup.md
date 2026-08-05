---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.RoundUp

Returns the result of rounding number up to the next highest integer. If number is null, this function returns null. If digits is provided, number is rounded to the specified number of decimal digits.

## Signature

```m
Number.RoundUp(number as nullable number, optional digits as nullable number) as
nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number | nullable number | |
| optional digits | nullable number | |

## Returns

nullable number

### Example 1

Round up 1.234 to integer.

```m
Number.RoundUp(1.234)
```

// Output
```
2
```

### Example 2

Round up 1.999 to integer.

```m
Number.RoundUp(1.999)
```

// Output
```
2
```

### Example 3

Round up 1.234 to two decimal places.

```m
Number.RoundUp(1.234, 2)
```

// Output
```
1.24
```

