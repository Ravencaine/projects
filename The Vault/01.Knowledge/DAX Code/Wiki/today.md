---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# TODAY

Applies to: Calculated column Calculated table Measure Visual calculation Returns the current date.

## Syntax

```dax
TODAY()
```

## Remarks

The TODAY function is useful when you need to have the current date displayed in a report, regardless of when you open it. It is also useful for calculating intervals. If the TODAY function does not update the date when you expect it to, you might need to change the settings that control when the report or semantic model is refreshed. The NOW function is similar but returns the exact time, whereas TODAY returns the time value 12:00:00 AM (midnight) for all dates.