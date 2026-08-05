---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# CHISQ.INV

Applies to: Calculated column Calculated table Measure Visual calculation Returns the inverse of the left-tailed probability of the chi-squared distribution.

## Syntax

```dax
CHISQ.INV(probability,deg_freedom)
```

## Remarks

If argument is nonnumeric, CHISQ.INV returns the #VALUE! error value. If probability < 0 or probability > 1, CHISQ.INV returns the #NUM! error value. If deg_freedom is not an integer, it is rounded.