---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# LCM

Applies to: Calculated column Calculated table Measure Visual calculation Returns the least common multiple of integers. The least common multiple is the smallest positive integer that is a multiple of all integer arguments number1, number2, and so on. Use

## Syntax

```dax
LCM(number1, number2)
```

## Remarks

If any argument is nonnumeric, LCM returns the #VALUE! error value. If any argument is less than zero, LCM returns the #NUM! error value. If LCM(a,b) >=2^53, LCM returns the #NUM! error value. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.