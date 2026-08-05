---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.StartOfDay

Returns the start of the day represented by dateTime. dateTime must be a date, datetime, or datetimezone value.

## Signature

```m
Date.StartOfDay(dateTime as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

any

### Example 1

Find the start of the day for October 10th, 2011, 8:00AM.

```m
Date.StartOfDay(#datetime(2011, 10, 10, 8, 0, 0))
```

// Output
```
#datetime(2011, 10, 10, 0, 0, 0)
```

