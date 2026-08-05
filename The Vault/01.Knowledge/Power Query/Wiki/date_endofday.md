---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.EndOfDay

Returns the end of the day represented by dateTime. Time zone information is preserved. dateTime: A date, datetime, or datetimezone value from from which the end of the day is calculated.

## Signature

```m
Date.EndOfDay(dateTime as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

any

### Example 1

Get the end of the day for 5/14/2011 05:00:00 PM.

```m
Date.EndOfDay(#datetime(2011, 5, 14, 17, 0, 0))
```

// Output
```
#datetime(2011, 5, 14, 23, 59, 59.9999999)
```

### Example 2

Get the end of the day for 5/17/2011 05:00:00 PM -7:00.

```m
Date.EndOfDay(#datetimezone(2011, 5, 17, 5, 0, 0, -7, 0))
```

// Output
```
#datetimezone(2011, 5, 17, 23, 59, 59.9999999, -7, 0)
Last updated on 03/24/2026
```

