---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.IsInNextQuarter

Indicates whether the given datetime value dateTime occurs during the next quarter, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current quarter. dateTime: A date, datetime, or datetimezone value to be evaluated. Example Determine if the quarter after the current system time is in the next quarter. Usage Power Query M Date.IsInNextQuarter(Date.AddQuarters(DateTime.FixedLocalNow(), 1)) Output true Last updated on 03/24/2026 --- PAGE 529 ---

## Signature

```m
Date.IsInNextQuarter(dateTime as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable logical

