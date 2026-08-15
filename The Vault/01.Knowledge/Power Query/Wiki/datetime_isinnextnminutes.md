---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [datetime, m-function]
---


# DateTime.IsInNextNMinutes

Indicates whether the given datetime value dateTime occurs during the next number of minutes, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current minute. dateTime: A datetime, or datetimezone value to be evaluated. minutes: The number of minutes.

## Signature

```m
DateTime.IsInNextNMinutes(dateTime as any, minutes as number) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| minutes | number | |

## Returns

nullable logical

### Example 1

Determine if the minute after the current system time is in the next two minutes.

```m
DateTime.IsInNextNMinutes(DateTime.FixedLocalNow() + #duration(0, 0, 2, 0), 2)
```

// Output
```
true
```

