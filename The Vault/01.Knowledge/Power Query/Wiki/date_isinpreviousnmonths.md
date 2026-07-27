---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.IsInPreviousNMonths

Indicates whether the given datetime value dateTime occurs during the previous number of months, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current month. dateTime: A date, datetime, or datetimezone value to be evaluated. months: The number of months.

## Signature

```m
Date.IsInPreviousNMonths(dateTime as any, months as number) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| months | number | |

## Returns

nullable logical

### Example 1

Determine if the month before the current system time is in the previous two months.

```m
Date.IsInPreviousNMonths(Date.AddMonths(DateTime.FixedLocalNow(), -1), 2)
```

// Output
```
true
```

