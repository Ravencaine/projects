---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, dax]
---

# ROUNDUP

Applies to: Calculated column Calculated table Measure Visual Rounds a number up, away from 0 (zero).

## Syntax

```dax
ROUNDUP(<number>, <num_digits>)
```

## Remarks

If num_digits is greater than 0 (zero), then the number is rounded up to the specified number of decimal places. If num_digits is 0, then number is rounded up to the nearest integer. If num_digits is less than 0, then number is rounded up to the left of the decimal point. ROUNDUP behaves like ROUND, except that it always rounds a number up.