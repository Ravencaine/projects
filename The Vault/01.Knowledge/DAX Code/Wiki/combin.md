---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, dax]
---

# COMBIN

Applies to: Calculated column Calculated table Measure Visual Returns the number of combinations for a given number of items. Use COMBIN to determine the total possible number of groups for a given number of items.

## Syntax

```dax
COMBIN(number, number_chosen)
```

## Return Value

the #NUM! error value. A combination is any set or subset of items, regardless of their internal order. Combinations are distinct from permutations, for which the internal order is

## Remarks

Numeric arguments are truncated to integers. If either argument is nonnumeric, COMBIN returns the #VALUE! error value. If number < 0, number_chosen < 0, or number < number_chosen, COMBIN returns the #NUM! error value. A combination is any set or subset of items, regardless of their internal order. Combinations are distinct from permutations, for which the internal order is