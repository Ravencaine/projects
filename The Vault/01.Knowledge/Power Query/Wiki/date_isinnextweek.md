---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.IsInNextWeek

Indicates whether the given datetime value dateTime occurs during the next week, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current week. dateTime: A date, datetime, or datetimezone value to be evaluated.

## Signature

```m
Date.IsInNextWeek(dateTime as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable logical

### Example 1

Determine if the week after the current system time is in the next week.

```m
Date.IsInNextWeek(Date.AddDays(DateTime.FixedLocalNow(), 7))
```

// Output
```
true
```

