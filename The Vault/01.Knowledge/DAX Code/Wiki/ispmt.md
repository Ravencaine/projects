---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# ISPMT

Applies to: Calculated column Calculated table Measure Visual calculation Calculates the interest paid (or received) for the specified period of a loan (or

## Syntax

```dax
ISPMT(<rate>, <per>, <nper>, <pv>)
```

## Remarks

Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at an annual interest rate of 12 percent, use 0.12/12 for rate and 4*12 for nper. If you make annual payments on the same loan, use 0.12 for rate and 4 for nper.