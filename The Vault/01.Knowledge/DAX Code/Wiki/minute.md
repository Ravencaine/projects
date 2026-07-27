---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# MINUTE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the minute as a number from 0 to 59, given a date and time value.

## Syntax

```dax
MINUTE(<datetime>)
```

## Remarks

In contrast to Microsoft Excel, which stores dates and times in a serial numeric format, DAX uses a datetime data type for dates and times. You can provide the datetime value to the MINUTE function by referencing a column that stores dates and times, by using a date/time function, or by using an expression that returns a date and time. When the datetime argument is a text representation of the date and time, the function uses the locale and date/time settings of the client computer to understand the text value in order to perform the conversion. Most locales use the colon (:) as the time separ