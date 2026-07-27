---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# ODD

Applies to: Calculated column Calculated table Measure Visual calculation Returns number rounded up to the nearest odd integer.

## Syntax

```dax
ODD(number)
```

## Remarks

If number is nonnumeric, ODD returns the #VALUE! error value. Regardless of the sign of number, a value is rounded up when adjusted away from zero. If number is an odd integer, no rounding occurs. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.