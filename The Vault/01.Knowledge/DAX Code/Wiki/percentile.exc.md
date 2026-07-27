---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# PERCENTILE.EXC

Applies to: Calculated column Calculated table Measure Visual calculation Returns the k-th percentile of values in a range, where k is in the range 0..1, exclusive.

## Syntax

```dax
PERCENTILE.EXC(<column>, <k>)
```

## Remarks

If column is empty, BLANK() is returned. If k is zero or blank, percentile rank of 1/(n+1) returns the smallest value. If zero, it is out of range and an error is returned. If k is nonnumeric or outside the range 0 to 1, an error is returned.