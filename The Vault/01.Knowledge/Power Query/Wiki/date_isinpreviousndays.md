---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.IsInPreviousNDays

Indicates whether the given datetime value dateTime occurs during the previous number of days, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current day. dateTime: A date, datetime, or datetimezone value to be evaluated. days: The number of days. Example Determine if the day before the current system time is in the previous two days. Usage Power Query M Date.IsInPreviousNDays(Date.AddDays(DateTime.FixedLocalNow(), -1), 2) Output true Last updated on 03/24/2026 --- PAGE 534 ---

## Signature

```m
Date.IsInPreviousNDays(dateTime as any, days as number) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| days | number | |

## Returns

nullable logical

