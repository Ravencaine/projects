---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.IsInPreviousNQuarters

Indicates whether the given datetime value dateTime occurs during the previous number of quarters, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current quarter. dateTime: A date, datetime, or datetimezone value to be evaluated. quarters: The number of quarters.

## Signature

```m
Date.IsInPreviousNQuarters(dateTime as any, quarters as number) as nullable
logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| quarters | number | |

## Returns

nullable logical

### Example 1

Determine if the quarter before the current system time is in the previous two quarters.

```m
Date.IsInPreviousNQuarters(Date.AddQuarters(DateTime.FixedLocalNow(), -1), 2)
```

// Output
```
true
```

