---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["datetime", "m-function"]
---


# DateTime.IsInNextHour

Indicates whether the given datetime value dateTime occurs during the next hour, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current hour. dateTime: A datetime, or datetimezone value to be evaluated.

## Signature

```m
DateTime.IsInNextHour(dateTime as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable logical

### Example 1

Determine if the hour after the current system time is in the next hour.

```m
DateTime.IsInNextHour(DateTime.FixedLocalNow() + #duration(0, 1, 0, 0))
```

// Output
```
true
```

