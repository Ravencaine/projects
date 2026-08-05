---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.IntegerDivide

Returns the integer portion of the result from dividing a number, number1, by another number, number2. If number1 or number2 are null, Number.IntegerDivide returns null. number1: The dividend. number2: The divisor.

## Signature

```m
Number.IntegerDivide(
number1 as nullable number,
number2 as nullable number,
optional precision as nullable number
) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number1 | nullable number | |
| number2 | nullable number | |
| optional precision | nullable number | |

## Returns

nullable number

### Example 1

Divide 6 by 4.

```m
Number.IntegerDivide(6, 4)
```

// Output
```
1
```

### Example 2

Divide 8.3 by 3.

```m
Number.IntegerDivide(8.3, 3)
```

// Output
```
2
```

