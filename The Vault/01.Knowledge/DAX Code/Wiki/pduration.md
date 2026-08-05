---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# PDURATION

Applies to: Calculated column Calculated table Measure Visual calculation Returns the number of periods required by an investment to reach a specified value.

## Syntax

```dax
PDURATION(<rate>, <pv>, <fv>)
```

## Remarks

PDURATION uses the following equation: log(fv) − log(pv) PDURATION = log(1 + rate) An error is returned if: rate ≤ 0. pv ≤ 0. fv ≤ 0.