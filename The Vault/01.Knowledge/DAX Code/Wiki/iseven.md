---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# ISEVEN

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE if number is even, or FALSE if number is odd.

## Syntax

```dax
ISEVEN(number)
```

## Remarks

If number is nonnumeric, ISEVEN returns the #VALUE! error value. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.