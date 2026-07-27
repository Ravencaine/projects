---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# YEAR

Applies to: Calculated column Calculated table Measure Visual calculation Returns the year of a date as a four digit integer in the range 1900-9999.

## Syntax

```dax
YEAR(<date>)
```

## Remarks

In contrast to Microsoft Excel, which stores dates as serial numbers, DAX uses a datetime data type to work with dates and times. Dates should be entered by using the DATE function, or as results of other formulas or functions. You can also enter dates in accepted text representations of a date, such as March 3, 2007, or Mar-3-2003. Values returned by the YEAR, MONTH, and DAY functions will be Gregorian values regardless of the display format for the supplied date value. For