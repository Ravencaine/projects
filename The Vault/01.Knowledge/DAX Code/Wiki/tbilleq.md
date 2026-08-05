---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# TBILLEQ

Applies to: Calculated column Calculated table Measure Visual calculation Returns the bond-equivalent yield for a Treasury bill.

## Syntax

```dax
TBILLEQ(<settlement>, <maturity>, <discount>)
```

## Remarks

Dates are stored as sequential serial numbers so they can be used in calculations. In DAX, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899. TBILLEQ is calculated as: