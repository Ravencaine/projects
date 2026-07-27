---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# DAY

Applies to: Calculated column Calculated table Measure Visual calculation Returns the day of the month, a number from 1 to 31.

## Syntax

```dax
DAY(<date>)
```

## Remarks

The DAY function takes as an argument the date of the day you are trying to find. Dates can be provided to the function by using another date function, by using an expression that returns a date, or by typing a date in a datetime format. You can also type a date in one of the accepted string formats for dates. Values returned by the YEAR, MONTH and DAY functions will be Gregorian values regardless of the display format for the supplied date value. For