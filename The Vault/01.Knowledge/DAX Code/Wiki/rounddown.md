---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, dax]
---

# ROUNDDOWN

Applies to: Calculated column Calculated table Measure Visual Rounds a number down, toward zero.

## Syntax

```dax
ROUNDDOWN(<number>, <num_digits>)
```

## Remarks

If num_digits is greater than 0 (zero), then the value in number is rounded down to the specified number of decimal places. If num_digits is 0, then the value in number is rounded down to the nearest integer. If num_digits is less than 0, then the value in number is rounded down to the left of the decimal point.