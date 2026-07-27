---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, dax]
---

# IF.EAGER

Applies to: Calculated column Calculated table Measure Visual calculation Checks a condition, and returns one value when TRUE, otherwise it returns a second

## Syntax

```dax
IF.EAGER(<logical_test>, <value_if_true>[, <value_if_false>])
```

## Remarks

The IF.EAGER function can return a variant data type if value_if_true and value_if_false are of different data types, but the function attempts to return a single data type if both value_if_true and value_if_false are of numeric data types. In the latter case, the IF.EAGER function will implicitly convert data types to accommodate both values.