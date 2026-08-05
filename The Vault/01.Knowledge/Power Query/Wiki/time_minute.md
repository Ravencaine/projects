---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["time", "m-function"]
---


# Time.Minute

Returns the minute component of the provided time, datetime, or datetimezone value, dateTime.

## Signature

```m
Time.Minute(dateTime as any) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable number

### Example 1

Find the minute in #datetime(2011, 12, 31, 9, 15, 36).

```m
Time.Minute(#datetime(2011, 12, 31, 9, 15, 36))
```

// Output
```
15
```

