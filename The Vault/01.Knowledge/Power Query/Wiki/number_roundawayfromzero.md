---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.RoundAwayFromZero

Returns the result of rounding number based on the sign of the number. This function will round positive numbers up and negative numbers down. If digits is specified, number is rounded to the digits number of decimal digits.

## Signature

```m
Number.RoundAwayFromZero(number as nullable number, optional digits as nullable
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

Round the number -1.2 away from zero.

```m
Number.RoundAwayFromZero(-1.2)
```

// Output
```
-2
```

### Example 2

Round the number 1.2 away from zero.

```m
Number.RoundAwayFromZero(1.2)
```

// Output
```
2
```

### Example 3

Round the number -1.234 to two decimal places away from zero.

```m
Number.RoundAwayFromZero(-1.234, 2)
```

// Output
```
-1.24
```

