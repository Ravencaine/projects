---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# RRI

Applies to: Calculated column Calculated table Measure Visual calculation Returns an equivalent interest rate for the growth of an investment.

## Syntax

```dax
RRI(<nper>, <pv>, <fv>)
```

## Remarks

nper pv RRI returns the interest rate given (the number of periods), (present fv value), and (future value), calculated by using the following equation: fv ( 1 ) nper ( ) − 1 pv An error is returned if: nper ≤ 0.