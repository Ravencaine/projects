---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# CURRENCY

Applies to: Calculated column Calculated table Measure Visual calculation Evaluates the argument and returns the result as currency data type.

## Syntax

```dax
CURRENCY(<value>)
```

## Return Value

the 4th decimal digit. Rounding up occurs if the 5th significant decimal is equal or larger than 5. For

## Remarks

The CURRENCY function rounds up the 5th significant decimal, in value, to return the 4th decimal digit. Rounding up occurs if the 5th significant decimal is equal or larger than 5. For