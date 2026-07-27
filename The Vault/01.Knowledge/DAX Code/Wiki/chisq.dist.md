---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# CHISQ.DIST

Applies to: Calculated column Calculated table Measure Visual calculation Returns the chi-squared distribution.

## Syntax

```dax
CHISQ.DIST(<x>, <deg_freedom>, <cumulative>)
```

## Remarks

If x or deg_freedom is nonnumeric, an error is returned. If deg_freedom is not an integer, it is rounded.