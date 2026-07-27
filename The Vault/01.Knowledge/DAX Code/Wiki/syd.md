---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# SYD

Applies to: Calculated column Calculated table Measure Visual calculation Returns the sum-of-years' digits depreciation of an asset for a specified period.

## Syntax

```dax
SYD(<cost>, <salvage>, <life>, <per>)
```

## Remarks

SYD is calculated as follows: (cost − salvage) × (life − per + 1) × 2 SYD = (life) × (life + 1)