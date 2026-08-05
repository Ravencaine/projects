---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.AddYears

Returns the date, datetime, or datetimezone result of adding numberOfYears to a datetime value dateTime. dateTime: The date, datetime, or datetimezone value to which years are added. numberOfYears: The number of years to add.

## Signature

```m
Date.AddYears(dateTime as any, numberOfYears as number) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| numberOfYears | number | |

## Returns

any

### Example 1

Add 4 years to the date, datetime, or datetimezone value representing the date 5/14/2011.

```m
Date.AddYears(#date(2011, 5, 14), 4)
```

// Output
```
#date(2015, 5, 14)
```

### Example 2

Add 10 years to the date, datetime, or datetimezone value representing the date and time of 5/14/2011 08:15:22 AM.

```m
Date.AddYears(#datetime(2011, 5, 14, 8, 15, 22), 10)
```

// Output
```
#datetime(2021, 5, 14, 8, 15, 22)
```

