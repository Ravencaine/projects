---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# NOW

Applies to: Calculated column Calculated table Measure Visual calculation Returns the current date and time in datetime format.

## Syntax

```dax
NOW()
```

## Remarks

The result of the NOW function changes only when the column that contains the formula is refreshed. It is not updated continuously. In the Power BI Service, the result of the NOW function is always in the UTC timezone. The TODAY function returns the same date but is not precise with regard to time; the time returned is always 12:00:00 AM and only the date is updated.