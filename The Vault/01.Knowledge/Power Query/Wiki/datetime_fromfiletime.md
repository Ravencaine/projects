---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["datetime", "m-function"]
---


# DateTime.FromFileTime

Creates a datetime value from the fileTime value and converts it to the local time zone. The filetime is a Windows file time value that represents the number of 100-nanosecond intervals that have elapsed since 12:00 midnight, January 1, 1601 A.D. (C.E.) Coordinated Universal Time (UTC).

## Signature

```m
DateTime.FromFileTime(fileTime as nullable number) as nullable datetime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| fileTime | nullable number | |

## Returns

nullable datetime

### Example 1

Convert 129876402529842245 into a datetime value.

```m
DateTime.FromFileTime(129876402529842245)
```

// Output
```
#datetime(2012, 7, 24, 14, 50, 52.9842245)
```

