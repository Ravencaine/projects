---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [time, m-function]
---


# Time.Second

Returns the second component of the provided time, datetime, or datetimezone value, dateTime.

## Signature

```m
Time.Second(dateTime as any) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable number

### Example 1

Find the second value from a datetime value.

```m
Time.Second(#datetime(2011, 12, 31, 9, 15, 36.5))
```

// Output
```
36.5
```

