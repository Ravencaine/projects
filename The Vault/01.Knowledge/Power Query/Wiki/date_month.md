---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.Month

Returns the month component of the provided datetime value, dateTime.

## Signature

```m
Date.Month(dateTime as any) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable number

### Example 1

Find the month in #datetime(2011, 12, 31, 9, 15, 36).

```m
Date.Month(#datetime(2011, 12, 31, 9, 15, 36))
```

// Output
```
12
```

