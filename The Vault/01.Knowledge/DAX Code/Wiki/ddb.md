---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# DDB

Applies to: Calculated column Calculated table Measure Visual calculation Returns the depreciation of an asset for a specified period using the double-declining balance method or some other method you specify.

## Syntax

```dax
DDB(<cost>, <salvage>, <life>, <period>[, <factor>])
```

## Remarks

The double-declining balance method computes depreciation at an accelerated rate. Depreciation is highest in the first period and decreases in successive periods. DDB uses the following formula to calculate depreciation for a period: factor Min((cost−totaldepreciationfrompriorperiods)×( ),(cost−salvage−totaldepreciationfrompriorperiods)) life Change factor if you do not want to use the double-declining balance method. Use the VDB function if you want to switch to the straight-line depreciation method when depreciation is greater than the declining balance calculation. period is rounded to the 