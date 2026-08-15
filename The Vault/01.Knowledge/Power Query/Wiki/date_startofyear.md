---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.StartOfYear

Returns the start of the year that contains dateTime. dateTime must be a date, datetime, or datetimezone value.

## Signature

```m
Date.StartOfYear(dateTime as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

any

### Example 1

Find the start of the year for October 10th, 2011, 8:10:32AM.

```m
Date.StartOfYear(#datetime(2011, 10, 10, 8, 10, 32))
```

// Output
```
#datetime(2011, 1, 1, 0, 0, 0)
```

