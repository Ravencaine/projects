---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.IsInNextNQuarters

Indicates whether the given datetime value dateTime occurs during the next number of quarters, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current quarter. dateTime: A date, datetime, or datetimezone value to be evaluated. quarters: The number of quarters. Example Determine if the quarter after the current system time is in the next two quarters. Usage Power Query M Date.IsInNextNQuarters(Date.AddQuarters(DateTime.FixedLocalNow(), 1), 2) Output true Last updated on 03/24/2026 --- PAGE 526 ---

## Signature

```m
Date.IsInNextNQuarters(dateTime as any, quarters as number) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| quarters | number | |

## Returns

nullable logical

