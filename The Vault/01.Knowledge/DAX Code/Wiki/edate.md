---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# EDATE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the date that is the indicated number of months before or after the start date.

## Syntax

```dax
EDATE(<start_date>, <months>)
```

## Remarks

In contrast to Microsoft Excel, which stores dates as sequential serial numbers, DAX works with dates in a datetime format. Dates stored in other formats are converted implicitly. If start_date is not a valid date, EDATE returns an error. Make sure that the column reference or date that you supply as the first argument is a date. If months is not an integer, it is truncated.