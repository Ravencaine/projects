---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [datetime, m-function]
---


# DateTime.IsInNextNSeconds

Indicates whether the given datetime value dateTime occurs during the next number of seconds, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current second. dateTime: A datetime, or datetimezone value to be evaluated. seconds: The number of seconds.

## Signature

```m
DateTime.IsInNextNSeconds(dateTime as any, seconds as number) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| seconds | number | |

## Returns

nullable logical

### Example 1

Determine if the second after the current system time is in the next two seconds.

```m
DateTime.IsInNextNSeconds(DateTime.FixedLocalNow() + #duration(0, 0, 0, 2), 2)
```

// Output
```
true
```

