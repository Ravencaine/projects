---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# MOD

Applies to: Calculated column Calculated table Measure Visual calculation Returns the remainder after a number is divided by a divisor. The result always has the

## Syntax

```dax
MOD(<number>, <divisor>)
```

## Remarks

If the divisor is 0 (zero), MOD returns an error. You cannot divide by 0. The MOD function can be expressed in terms of the INT function: MOD(n, d) = n - d*INT(n/d)