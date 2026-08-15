---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.IsLeapYear

Indicates whether the given datetime value dateTime falls in is a leap year. dateTime: A date, datetime, or datetimezone value to be evaluated.

## Signature

```m
Date.IsLeapYear(dateTime as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable logical

### Example 1

Determine if the year 2012, as represented by #date(2012, 01, 01) is a leap year.

```m
Date.IsLeapYear(#date(2012, 01, 01))
```

// Output
```
true
```

