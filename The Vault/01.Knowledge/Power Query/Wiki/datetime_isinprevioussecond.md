---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["datetime", "m-function"]
---


# DateTime.IsInPreviousSecond

Indicates whether the given datetime value dateTime occurs during the previous second, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current second. dateTime: A datetime, or datetimezone value to be evaluated. Example Determine if the second before the current system time is in the previous second. Usage Power Query M DateTime.IsInPreviousSecond(DateTime.FixedLocalNow() - #duration(0, 0, 0, 1)) Output true Last updated on 03/24/2026 --- PAGE 588 ---

## Signature

```m
DateTime.IsInPreviousSecond(dateTime as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable logical

