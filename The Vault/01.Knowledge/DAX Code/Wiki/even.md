---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# EVEN

Applies to: Calculated column Calculated table Measure Visual calculation Returns number rounded up to the nearest even integer. You can use this function for

## Syntax

```dax
EVEN(number)
```

## Remarks

If number is nonnumeric, EVEN returns the #VALUE! error value. Regardless of the sign of number, a value is rounded up when adjusted away from zero. If number is an even integer, no rounding occurs. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.