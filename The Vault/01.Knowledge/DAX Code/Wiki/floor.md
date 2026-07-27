---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# FLOOR

Applies to: Calculated column Calculated table Measure Visual calculation Rounds a number down, toward zero, to the nearest multiple of significance.

## Syntax

```dax
FLOOR(<number>, <significance>)
```

## Remarks

If either argument is nonnumeric, FLOOR returns #VALUE! error value. If number and significance have different signs, FLOOR returns the #NUM! error value. Regardless of the sign of the number, a value is rounded down when adjusted away from zero. If the number is an exact multiple of significance, no rounding occurs.