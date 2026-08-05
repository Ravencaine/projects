---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# SLN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the straight-line depreciation of an asset for one period.

## Syntax

```dax
SLN(<cost>, <salvage>, <life>)
```

## Remarks

An error is returned if: life = 0. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.