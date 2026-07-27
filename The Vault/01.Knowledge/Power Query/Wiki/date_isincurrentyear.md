---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.IsInCurrentYear

Indicates whether the given datetime value dateTime occurs during the current year, as determined by the current date and time on the system. dateTime: A date, datetime, or datetimezone value to be evaluated.

## Signature

```m
Date.IsInCurrentYear(dateTime as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable logical

### Example 1

Determine if the current system time is in the current year.

```m
Date.IsInCurrentYear(DateTime.FixedLocalNow())
```

// Output
```
true
```

