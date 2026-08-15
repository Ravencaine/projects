---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.IsInNextNWeeks

Indicates whether the given datetime value dateTime occurs during the next number of weeks, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current week. dateTime: A date, datetime, or datetimezone value to be evaluated. weeks: The number of weeks. Example Determine if the week after the current system time is in the next two weeks. Usage Power Query M Date.IsInNextNWeeks(Date.AddDays(DateTime.FixedLocalNow(), 7), 2) Output true Last updated on 03/24/2026 --- PAGE 527 ---

## Signature

```m
Date.IsInNextNWeeks(dateTime as any, weeks as number) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| weeks | number | |

## Returns

nullable logical

