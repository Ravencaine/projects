---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# BETA.INV

Applies to: Calculated column Calculated table Measure Visual Returns the inverse of the beta cumulative probability density function (BETA.DIST). If probability = BETA.DIST(x,...TRUE), then BETA.INV(probability,...) = x. The beta

## Syntax

```dax
BETA.INV(probability,...)
```

## Remarks

If any argument is nonnumeric, BETA.INV returns the #VALUE! error value.