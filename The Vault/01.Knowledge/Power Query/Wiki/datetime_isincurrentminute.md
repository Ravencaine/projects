---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [datetime, m-function]
---


# DateTime.IsInCurrentMinute

Indicates whether the given datetime value dateTime occurs during the current minute, as determined by the current date and time on the system. dateTime: A datetime, or datetimezone value to be evaluated.

## Signature

```m
DateTime.IsInCurrentMinute(dateTime as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable logical

### Example 1

Determine if the current system time is in the current minute.

```m
DateTime.IsInCurrentMinute(DateTime.FixedLocalNow())
```

// Output
```
true
```

