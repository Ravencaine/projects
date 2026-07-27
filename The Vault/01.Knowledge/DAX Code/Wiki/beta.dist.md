---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# BETA.DIST

Applies to: Calculated column Calculated table Measure Visual calculation Returns the beta distribution. The beta distribution is commonly used to study variation

## Syntax

```dax
BETA.DIST(x,alpha,beta,cumulative,[A],[B])
```

## Remarks

If any argument is nonnumeric, BETA.DIST returns the #VALUE! error value. If any argument is not an integer, it is rounded.