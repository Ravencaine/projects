---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.IsInCurrentDay

Indicates whether the given datetime value dateTime occurs during the current day, as determined by the current date and time on the system. dateTime: A date, datetime, or datetimezone value to be evaluated. Example Determine if the current system time is in the current day. Usage Power Query M Date.IsInCurrentDay(DateTime.FixedLocalNow()) Output true --- PAGE 517 ---

## Signature

```m
Date.IsInCurrentDay(dateTime as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable logical

