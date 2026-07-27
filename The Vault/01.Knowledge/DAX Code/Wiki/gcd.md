---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# GCD

Applies to: Calculated column Calculated table Measure Visual calculation Returns the greatest common divisor of two or more integers. The greatest common divisor is the largest integer that divides both number1 and number2 without a remainder.

## Syntax

```dax
GCD(number1, number2)
```

## Remarks

If any argument is nonnumeric, GCD returns the #VALUE! error value. If any argument is less than zero, GCD returns the #NUM! error value. One divides any value evenly. A prime number has only itself and one as even divisors. If a parameter to GCD is >=2^53, GCD returns the #NUM! error value. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.