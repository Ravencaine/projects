---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# EXPON.DIST

Applies to: Calculated column Calculated table Measure Visual calculation Returns the exponential distribution. Use EXPON.DIST to model the time between

## Syntax

```dax
EXPON.DIST(x,lambda,cumulative)
```

## Remarks

If x or lambda is nonnumeric, EXPON.DIST returns the #VALUE! error value. If x or lambda is not an integer, it is rounded.