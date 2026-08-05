---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.Exp

Returns the result of raising e to the power of number (exponential function). number: A number for which the exponential function is to be calculated. If number is null, Number.Exp returns null.

## Signature

```m
Number.Exp(number as nullable number) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number | nullable number | |

## Returns

nullable number

### Example 1

Raise e to the power of 3.

```m
Number.Exp(3)
```

// Output
```
20.085536923187668
```

