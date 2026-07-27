---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# PERMUT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the number of permutations for a given number of objects that can be selected

## Syntax

```dax
PERMUT(number, number_chosen)
```

## Remarks

Both arguments are truncated to integers. If number or number_chosen is nonnumeric, PERMUT returns the #VALUE! error value.