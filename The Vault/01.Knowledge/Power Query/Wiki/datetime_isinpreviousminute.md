---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [datetime, m-function]
---


# DateTime.IsInPreviousMinute

Indicates whether the given datetime value dateTime occurs during the previous minute, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current minute. dateTime: A datetime, or datetimezone value to be evaluated.

## Signature

```m
DateTime.IsInPreviousMinute(dateTime as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable logical

### Example 1

Determine if the minute before the current system time is in the previous minute.

```m
DateTime.IsInPreviousMinute(DateTime.FixedLocalNow() - #duration(0, 0, 1, 0))
```

// Output
```
true
```

