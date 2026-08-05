---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# DOLLARFR

Applies to: Calculated column Calculated table Measure Visual calculation Converts a dollar price expressed as a decimal number into a dollar price expressed as

## Syntax

```dax
DOLLARFR(<decimal_dollar>, <fraction>)
```

## Remarks

fraction is rounded to the nearest integer. An error is returned if: fraction < 1. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.