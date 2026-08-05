---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["datetime", "m-function"]
---


# DateTime.IsInNextNHours

Indicates whether the given datetime value dateTime occurs during the next number of hours, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current hour. dateTime: A datetime, or datetimezone value to be evaluated. hours: The number of hours. Example Determine if the hour after the current system time is in the next two hours. Usage Power Query M DateTime.IsInNextNHours(DateTime.FixedLocalNow() + #duration(0, 2, 0, 0), 2) Output true Last updated on 03/24/2026 --- PAGE 579 ---

## Signature

```m
DateTime.IsInNextNHours(dateTime as any, hours as number) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| hours | number | |

## Returns

nullable logical

