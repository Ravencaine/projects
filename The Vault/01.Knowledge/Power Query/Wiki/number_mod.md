---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.Mod

Returns the remainder resulting from the integer division of number by divisor. If number or divisor are null, this function returns null. number: The dividend. divisor: The divisor. precision: (Optional) The precision of the integer division. This parameter can be either Precision.Double for Double precision or Precision.Decimal for Decimal precision. The default value is Precision.Double.

## Signature

```m
Number.Mod(
number as nullable number,
divisor as nullable number,
optional precision as nullable number
) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number | nullable number | |
| divisor | nullable number | |
| optional precision | nullable number | |

## Returns

nullable number

### Example 1

Find the remainder when you divide 5 by 3.

```m
Number.Mod(5, 3)
```

// Output
```
2
```

### Example 2

```m
let
Dividend = 10.5,
Divisor = 0.2,
#"Use Double Precision" = Number.Mod(Dividend, Divisor, Precision.Double),
#"Use Decimal Precision" = Number.Mod(Dividend, Divisor, Precision.Decimal),
// Convert to text to inspect precision
#"Double To Text" = Number.ToText(#"Use Double Precision", "G"),
#"Decimal To Text" = Number.ToText(#"Use Decimal Precision", "G"),
#"Display Result" = [
DoublePrecision = #"Double To Text",
DecimalPrecision = #"Decimal To Text"
]
in
#"Display Result"
```

// Output
```
[
DoublePrecision = "0.0999999999999994",
DecimalPrecision = "0.1"
]
```

