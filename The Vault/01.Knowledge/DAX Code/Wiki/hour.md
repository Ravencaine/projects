---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# HOUR

Applies to: Calculated column Calculated table Measure Visual calculation Returns the hour as a number from 0 (12:00 A.M.) to 23 (11:00 P.M.).

## Syntax

```dax
HOUR(<datetime>)
```

## Remarks

The HOUR function takes as argument the time that contains the hour you want to find. You can supply the time by using a date/time function, an expression that returns a datetime, or by typing the value directly in one of the accepted time formats. Times can also be entered as any accepted text representation of a time. When the datetime argument is a text representation of the date and time, the function uses the locale and date/time settings of the client computer to understand the text value in order to perform the conversion. Most locales use the colon (:) as the time separator and any inp