---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.DayOfWeek

Returns a number (from 0 to 6) indicating the day of the week of the provided dateTime. dateTime: A date, datetime, or datetimezone value. firstDayOfWeek: A Day value indicating which day should be considered the first day of the week. Allowed values are Day.Sunday, Day.Monday, Day.Tuesday, Day.Wednesday, Day.Thursday, Day.Friday, or Day.Saturday. If unspecified, a culture-dependent default is used.

## Signature

```m
Date.DayOfWeek(dateTime as any, optional firstDayOfWeek as nullable number) as
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

Get the day of the week represented by Monday, February 21st, 2011, treating Sunday as the first day of the week.

```m
Date.DayOfWeek(#date(2011, 02, 21), Day.Sunday)
```

// Output
```
1
```

### Example 2

Get the day of the week represented by Monday, February 21st, 2011, treating Monday as the first day of the week.

```m
Date.DayOfWeek(#date(2011, 02, 21), Day.Monday)
```

// Output
```
0
```

## Related

[[culture_and_text_formatting]]

