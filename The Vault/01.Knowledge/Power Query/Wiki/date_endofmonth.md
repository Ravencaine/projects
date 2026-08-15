---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.EndOfMonth

Returns the end of the month that contains dateTime. dateTime: A date, datetime, or datetimezone value from which the end of the month is calculated.

## Signature

```m
Date.EndOfMonth(dateTime as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

any

### Example 1

Get the end of the month for 5/14/2011.

```m
Date.EndOfMonth(#date(2011, 5, 14))
```

// Output
```
#date(2011, 5, 31)
```

### Example 2

Get the end of the month for 5/17/2011 05:00:00 PM -7:00.

```m
Date.EndOfMonth(#datetimezone(2011, 5, 17, 5, 0, 0, -7, 0))
```

// Output
```
#datetimezone(2011, 5, 31, 23, 59, 59.9999999, -7, 0)
```

