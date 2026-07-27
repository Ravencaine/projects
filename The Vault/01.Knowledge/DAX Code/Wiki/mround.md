---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# MROUND

Applies to: Calculated column Calculated table Measure Visual calculation Returns a number rounded to the desired multiple.

## Syntax

```dax
MROUND(<number>, <multiple>)
```

## Remarks

MROUND rounds up, away from zero, if the remainder of dividing number by the specified multiple is greater than or equal to half the value of multiple.