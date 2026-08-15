---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.IsInPreviousDay

Indicates whether the given datetime value dateTime occurs during the previous day, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current day. dateTime: A date, datetime, or datetimezone value to be evaluated.

## Signature

```m
Date.IsInPreviousDay(dateTime as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable logical

### Example 1

Determine if the day before the current system time is in the previous day.

```m
Date.IsInPreviousDay(Date.AddDays(DateTime.FixedLocalNow(), -1))
```

// Output
```
true
```

