---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.AddWeeks

Returns the date, datetime, or datetimezone result from adding numberOfWeeks weeks to the datetime value dateTime. dateTime: The date, datetime, or datetimezone value to which weeks are being added. numberOfWeeks: The number of weeks to add. Example Add 2 weeks to the date, datetime, or datetimezone value representing the date 5/14/2011. Usage Power Query M Date.AddWeeks(#date(2011, 5, 14), 2) Output #date(2011, 5, 28) Related content #date #datetime #datetimezone Last updated on 03/24/2026 --- PAGE 493 ---

## Signature

```m
Date.AddWeeks(dateTime as any, numberOfWeeks as number) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| numberOfWeeks | number | |

## Returns

any

