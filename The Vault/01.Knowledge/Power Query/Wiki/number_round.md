---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.Round

Returns the result of rounding number to the nearest number. If number is null, Number.Round returns null. By default, number is rounded to the nearest integer, and ties are broken by rounding to the nearest even number (using RoundingMode.ToEven, also known as "banker's rounding"). However, these defaults can be overridden via the following optional parameters. digits: Causes number to be rounded to the specified number of decimal digits. roundingMode: Overrides the default tie-breaking behavior when number is at the midpoint between two potential rounded values (refer to RoundingMode.Type for possible values).

## Signature

```m
Number.Round(
number as nullable number,
optional digits as nullable number,
optional roundingMode as nullable number
) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number | nullable number | |
| optional digits | nullable number | |
| optional roundingMode | nullable number | |

## Returns

nullable number

### Example 1

Round 1.234 to the nearest integer.

```m
Number.Round(1.234)
```

// Output
```
1
```

### Example 2

```m
Number.Round(1.56)
```

// Output
```
2
```

### Example 3

Round 1.2345 to two decimal places.

```m
Number.Round(1.2345, 2)
```

// Output
```
1.23
```

### Example 4

Round 1.2345 to three decimal places (Rounding up).

```m
Number.Round(1.2345, 3, RoundingMode.Up)
```

// Output
```
1.235
```

### Example 5

Round 1.2345 to three decimal places (Rounding down).

```m
Number.Round(1.2345, 3, RoundingMode.Down)
```

// Output
```
1.234
```

