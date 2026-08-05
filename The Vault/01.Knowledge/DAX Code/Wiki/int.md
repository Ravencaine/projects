---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# INT

Applies to: Calculated column Calculated table Measure Visual calculation Rounds a number down to the nearest integer.

## Syntax

```dax
INT(<number>)
```

## Remarks

TRUNC and INT are similar in that both return integers. TRUNC removes the fractional part of the number. INT rounds numbers down to the nearest integer based on the value of the fractional part of the number. INT and TRUNC are different only when using negative numbers: TRUNC(-4.3) returns -4, but INT(-4.3) returns -5 because -5 is the lower number.