---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.AddDays

Returns the date, datetime, or datetimezone result from adding numberOfDays days to the datetime value dateTime. dateTime: The date, datetime, or datetimezone value to which days are being added. numberOfDays: The number of days to add. Example Add 5 days to the date, datetime, or datetimezone value representing the date 5/14/2011. Usage Power Query M Date.AddDays(#date(2011, 5, 14), 5) Output #date(2011, 5, 19) Related content #date #datetime #datetimezone Last updated on 03/24/2026 --- PAGE 489 ---

## Signature

```m
Date.AddDays(dateTime as any, numberOfDays as number) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| numberOfDays | number | |

## Returns

any

