---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.IsInNextYear

Indicates whether the given datetime value dateTime occurs during the next year, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current year. dateTime: A date, datetime, or datetimezone value to be evaluated.

## Signature

```m
Date.IsInNextYear(dateTime as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable logical

### Example 1

Determine if the year after the current system time is in the next year.

```m
Date.IsInNextYear(Date.AddYears(DateTime.FixedLocalNow(), 1))
```

// Output
```
true
```

