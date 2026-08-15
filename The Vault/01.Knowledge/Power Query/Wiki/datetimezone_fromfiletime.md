---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [datetimezone, m-function]
---


# DateTimeZone.FromFileTime

Creates a datetimezone value from the fileTime value and converts it to the local time zone. The filetime is a Windows file time value that represents the number of 100-nanosecond intervals that have elapsed since 12:00 midnight, January 1, 1601 A.D. (C.E.) Coordinated Universal Time (UTC). Example Convert 129876402529842245 into a datetimezone value. Usage Power Query M DateTimeZone.FromFileTime(129876402529842245) Output #datetimezone(2012, 7, 24, 14, 50, 52.9842245, -7, 0) Last updated on 03/24/2026 --- PAGE 603 ---

## Signature

```m
DateTimeZone.FromFileTime(fileTime as nullable number) as nullable datetimezone
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| fileTime | nullable number | |

## Returns

nullable datetimezone

