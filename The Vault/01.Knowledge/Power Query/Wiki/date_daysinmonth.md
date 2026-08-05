---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.DaysInMonth

Returns the number of days in the month in the date, datetime, or datetimezone value dateTime. dateTime: A date, datetime, or datetimezone value for which the number of days in the month is returned.

## Signature

```m
Date.DaysInMonth(dateTime as any) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable number

### Example 1

Number of days in the month December as represented by #date(2011, 12, 01).

```m
Date.DaysInMonth(#date(2011, 12, 01))
```

// Output
```
31
```

