---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.IsInNextNYears

Indicates whether the given datetime value dateTime occurs during the next number of years, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current year. dateTime: A date, datetime, or datetimezone value to be evaluated. years: The number of years.

## Signature

```m
Date.IsInNextNYears(dateTime as any, years as number) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| years | number | |

## Returns

nullable logical

### Example 1

Determine if the year after the current system time is in the next two years.

```m
Date.IsInNextNYears(Date.AddYears(DateTime.FixedLocalNow(), 1), 2)
```

// Output
```
true
```

