---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.EndOfQuarter

Returns the end of the quarter that contains dateTime. Time zone information is preserved. dateTime: A date, datetime, or datetimezone value from which the end of the quarter is calculated.

## Signature

```m
Date.EndOfQuarter(dateTime as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

any

### Example 1

Find the end of the quarter for October 10th, 2011, 8:00AM.

```m
Date.EndOfQuarter(#datetime(2011, 10, 10, 8, 0, 0))
```

// Output
```
#datetime(2011, 12, 31, 23, 59, 59.9999999)
```

