---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# SECOND

Applies to: Calculated column Calculated table Measure Visual calculation Returns the seconds of a time value, as a number from 0 to 59.

## Syntax

```dax
SECOND(<time>)
```

## Remarks

In contrast to Microsoft Excel, which stores dates and times as serial numbers, DAX uses a datetime format when working with dates and times. If the source data is not in this format, DAX implicitly converts the data. You can use formatting to display the dates and times as a serial number of you need to. The date/time value that you supply as an argument to the SECOND function can be entered as a text string within quotation marks (for