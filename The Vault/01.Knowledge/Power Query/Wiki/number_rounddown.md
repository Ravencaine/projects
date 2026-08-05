---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.RoundDown

Returns the result of rounding number down to the previous highest integer. If number is null, this function returns null. If digits is provided, number is rounded to the specified number of decimal digits.

## Signature

```m
Number.RoundDown(number as nullable number, optional digits as nullable number) as
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

Round down 1.234 to integer.

```m
Number.RoundDown(1.234)
```

// Output
```
1
```

### Example 2

Round down 1.999 to integer.

```m
Number.RoundDown(1.999)
```

// Output
```
1
```

### Example 3

Round down 1.999 to two decimal places.

```m
Number.RoundDown(1.999, 2)
```

// Output
```
1.99
```

