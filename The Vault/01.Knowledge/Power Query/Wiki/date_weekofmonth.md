---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.WeekOfMonth

Returns a number from 1 to 6 indicating which week of the month the date dateTime falls in. dateTime: A datetime value for which the week-of-the-month is determined.

## Signature

```m
Date.WeekOfMonth(dateTime as any, optional firstDayOfWeek as nullable number) as
nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| optional firstDayOfWeek | nullable number | |

## Returns

nullable number

### Example 1

Determine which week of March the 15th falls on in 2011.

```m
Date.WeekOfMonth(#date(2011, 03, 15))
```

// Output
```
3
```

