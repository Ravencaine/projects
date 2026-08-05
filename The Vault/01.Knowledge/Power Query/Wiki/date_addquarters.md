---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.AddQuarters

Returns the date, datetime, or datetimezone result from adding numberOfQuarters quarters to the datetime value dateTime. dateTime: The date, datetime, or datetimezone value to which quarters are being added. numberOfQuarters: The number of quarters to add. Example Add 1 quarter to the date, datetime, or datetimezone value representing the date 5/14/2011. Usage Power Query M Date.AddQuarters(#date(2011, 5, 14), 1) Output #date(2011, 8, 14) Related content #date #datetime #datetimezone Last updated on 03/24/2026 --- PAGE 492 ---

## Signature

```m
Date.AddQuarters(dateTime as any, numberOfQuarters as number) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| numberOfQuarters | number | |

## Returns

any

