---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# DATEVALUE

Applies to: Calculated column Calculated table Measure Visual calculation Converts a date in text format to a date in datetime format.

## Syntax

```dax
DATEVALUE(date_text)
```

## Remarks

When converting, DATEVALUE uses the locale and date/time settings of the model to determine a date value. If the model date/time settings represent dates in the format of Month/Day/Year, then the string, "1/8/2009", is converted to a datetime value equivalent to January 8th of 2009. However, if the model date/time settings represent dates in the format of Day/Month/Year, the same string is converted as a datetime value equivalent to August 1st of 2009. If conversion using the locale and date/time settings of the model fails, DATEVALUE will attempt to use other date formats. In this case, some 