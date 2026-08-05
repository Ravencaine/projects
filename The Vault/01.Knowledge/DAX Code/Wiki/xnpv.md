---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# XNPV

Applies to: Calculated column Calculated table Measure Visual calculation Returns the present value for a schedule of cash flows that is not necessarily periodic.

## Syntax

```dax
XNPV(<table>, <values>, <dates>, <rate>)
```

## Remarks

The value is calculated as the following summation: N P j ∑ (1 + rate) dj−d1 j=1 365 Where: P jth j is the payment