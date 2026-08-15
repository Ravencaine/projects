---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.IsInYearToDate

Indicates whether the given datetime value dateTime occurs during the current year and is on or before the current day, as determined by the current date and time on the system. dateTime: A date, datetime, or datetimezone value to be evaluated.

## Signature

```m
Date.IsInYearToDate(dateTime as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable logical

### Example 1

Determine if the current system time is in the year to date.

```m
Date.IsInYearToDate(DateTime.FixedLocalNow())
```

// Output
```
true
```

