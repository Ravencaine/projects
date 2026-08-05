---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# POISSON.DIST

Applies to: Calculated column Calculated table Measure Visual calculation Returns the Poisson distribution. A common application of the Poisson distribution is

## Syntax

```dax
POISSON.DIST(x,mean,cumulative)
```

## Remarks

If x is not an integer, it is rounded. If x or mean is nonnumeric, POISSON.DIST returns the #VALUE! error value.