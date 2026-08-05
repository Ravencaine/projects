---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# FIXED

Applies to: Calculated column Calculated table Measure Visual calculation Rounds a number to the specified number of decimals and returns the result as text. You

## Syntax

```dax
FIXED(<number>, <decimals>, <no_commas>)
```

## Remarks

If the value used for the decimals parameter is negative, number is rounded to the left of the decimal point. If you omit decimals, it is assumed to be 2. If no_commas is 0 or is omitted, then the returned text includes commas as usual.