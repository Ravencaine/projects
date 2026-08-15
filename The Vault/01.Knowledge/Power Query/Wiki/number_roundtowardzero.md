---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [number, m-function]
---


# Number.RoundTowardZero

Returns the result of rounding number based on the sign of the number. This function will round positive numbers down and negative numbers up. If digits is specified, number is rounded to the digits number of decimal digits.

## Signature

```m
Number.RoundTowardZero(number as nullable number, optional digits as nullable
number) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number | nullable number | |
| optional digits | nullable number | |

## Returns

nullable number

### Example 1

Round the number -1.2 toward zero.

```m
Number.RoundTowardZero(-1.2)
```

// Output
```
-1
```

### Example 2

Round the number 1.2 toward zero.

```m
Number.RoundTowardZero(1.2)
```

// Output
```
1
```

### Example 3

Round the number -1.234 to two decimal places toward zero.

```m
Number.RoundTowardZero(-1.234, 2)
```

// Output
```
-1.23
```

