---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# TRUNC

Applies to: Calculated column Calculated table Measure Visual calculation Truncates a number to an integer by removing the decimal, or fractional, part of the

## Syntax

```dax
TRUNC(<number>,<num_digits>)
```

## Remarks

TRUNC and INT are similar in that both return integers. TRUNC removes the fractional part of the number. INT rounds numbers down to the nearest integer based on the value of the fractional part of the number. INT and TRUNC are different only when using negative numbers: TRUNC(-4.3) returns -4, but INT(-4.3) returns -5 because -5 is the smaller number.