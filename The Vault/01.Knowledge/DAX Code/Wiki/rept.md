---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# REPT

Applies to: Calculated column Calculated table Measure Visual calculation Repeats text a given number of times. Use REPT to fill a cell with a number of instances

## Syntax

```dax
REPT(<text>, <num_times>)
```

## Remarks

If number_times is 0 (zero), REPT returns a blank. If number_times is not an integer, it is truncated. The result of the REPT function cannot be longer than 32,767 characters, or REPT returns an error.