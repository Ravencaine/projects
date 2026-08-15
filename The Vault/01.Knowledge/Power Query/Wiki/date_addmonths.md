---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.AddMonths

Returns the date, datetime, or datetimezone result from adding numberOfMonths months to the datetime value dateTime. dateTime: The date, datetime, or datetimezone value to which months are being added. numberOfMonths: The number of months to add.

## Signature

```m
Date.AddMonths(dateTime as any, numberOfMonths as number) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| numberOfMonths | number | |

## Returns

any

### Example 1

Add 5 months to the date, datetime, or datetimezone value representing the date 5/14/2011.

```m
Date.AddMonths(#date(2011, 5, 14), 5)
```

// Output
```
#date(2011, 10, 14)
```

### Example 2

Add 18 months to the date, datetime, or datetimezone value representing the date and time of 5/14/2011 08:15:22 AM.

```m
Date.AddMonths(#datetime(2011, 5, 14, 8, 15, 22), 18)
```

// Output
```
#datetime(2012, 11, 14, 8, 15, 22)
```

