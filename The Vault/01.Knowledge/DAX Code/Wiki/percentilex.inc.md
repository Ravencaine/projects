---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# PERCENTILEX.INC

Applies to: Calculated column Calculated table Measure Visual calculation Returns the percentile number of an expression evaluated for each row in a table.

## Syntax

```dax
PERCENTILEX.INC(<table>, <expression>;, k)
```

## Remarks

If k is zero or blank, percentile rank of 1/(n - 1) returns the smallest value. If zero, it is out of range and an error is returned. If k is nonnumeric or outside the range 0 to 1, an error is returned. If k is not a multiple of 1/(n - 1), PERCENTILEX.EXC will interpolate to determine the value at the k-th percentile.