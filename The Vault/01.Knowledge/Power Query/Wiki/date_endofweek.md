---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.EndOfWeek

Returns the end of the week that contains dateTime. This function takes an optional Day, firstDayOfWeek, to set as the first day of the week for this relative calculation. The default value is Day.Sunday. dateTime: A date, datetime, or datetimezone value from which the last day of the week is calculated firstDayOfWeek: (Optional) A Day.Type value representing the first day of the week. Possible values are Day.Sunday, Day.Monday, Day.Tuesday, Day.Wednesday, Day.Thursday, Day.Friday and Day.Saturday. The default value is Day.Sunday.

## Signature

```m
Date.EndOfWeek(dateTime as any, optional firstDayOfWeek as nullable number) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| optional firstDayOfWeek | nullable number | |

## Returns

any

### Example 1

Get the end of the week for 5/14/2011.

```m
Date.EndOfWeek(#date(2011, 5, 14))
```

// Output
```
#date(2011, 5, 14)
```

### Example 2

Get the end of the week for 5/17/2011 05:00:00 PM -7:00, with Sunday as the first day of the week.

```m
Power Query M
Date.EndOfWeek(#datetimezone(2011, 5, 17, 5, 0, 0, -7, 0), Day.Sunday)
```

// Output
```
#datetimezone(2011, 5, 21, 23, 59, 59.9999999, -7, 0)
Last updated on 04/03/2026
```

