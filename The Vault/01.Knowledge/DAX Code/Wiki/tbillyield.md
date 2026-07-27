---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# TBILLYIELD

Applies to: Calculated column Calculated table Measure Visual calculation Returns the yield for a Treasury bill.

## Syntax

```dax
TBILLYIELD(<settlement>, <maturity>, <pr>)
```

## Remarks

Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899. TBILLYIELD is calculated as follows: