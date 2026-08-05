---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, dax]
---

# COMBINA

Applies to: Calculated column Calculated table Measure Visual Returns the number of combinations (with repetitions) for a given number of items.

## Syntax

```dax
COMBINA(number, number_chosen)
```

## Remarks

If the value of either argument is outside of its constraints, COMBINA returns the #NUM! error value. If either argument is a non-numeric value, COMBINA returns the #VALUE! error value. N M The following equation is used, where is Number and is Number_chosen: N + M − 1 ( ) N − 1