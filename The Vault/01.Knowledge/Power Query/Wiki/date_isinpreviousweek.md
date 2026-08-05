---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.IsInPreviousWeek

Indicates whether the given datetime value dateTime occurs during the previous week, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current week. dateTime: A date, datetime, or datetimezone value to be evaluated.

## Signature

```m
Date.IsInPreviousWeek(dateTime as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable logical

### Example 1

Determine if the week before the current system time is in the previous week.

```m
Date.IsInPreviousWeek(Date.AddDays(DateTime.FixedLocalNow(), -7))
```

// Output
```
true
```

