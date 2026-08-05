---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.IsInNextNDays

Indicates whether the given datetime value dateTime occurs during the next number of days, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current day. dateTime: A date, datetime, or datetimezone value to be evaluated. days: The number of days.

## Signature

```m
Date.IsInNextNDays(dateTime as any, days as number) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| days | number | |

## Returns

nullable logical

### Example 1

Determine if the day after the current system time is in the next two days.

```m
Date.IsInNextNDays(Date.AddDays(DateTime.FixedLocalNow(), 1), 2)
```

// Output
```
true
```

