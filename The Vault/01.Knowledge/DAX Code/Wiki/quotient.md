---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# QUOTIENT

Applies to: Calculated column Calculated table Measure Visual calculation Performs division and returns only the integer portion of the division result. Use this

## Syntax

```dax
QUOTIENT(<numerator>, <denominator>)
```

## Remarks

If either argument is non-numeric, QUOTIENT returns the #VALUE! error value. You can use a column reference instead of a literal value for either argument. However, if the column that you reference contains a 0 (zero), an error is returned for the entire column of values.