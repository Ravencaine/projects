---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# EOMONTH

Applies to: Calculated column Calculated table Measure Visual calculation Returns the date in datetime format of the last day of the month, before or after a

## Syntax

```dax
EOMONTH(<start_date>, <months>)
```

## Remarks

In contrast to Microsoft Excel, which stores dates as sequential serial numbers, DAX works with dates in a datetime format. The EOMONTH function can accept dates in other formats, with the following restrictions: If start_date is not a valid date, EOMONTH returns an error.