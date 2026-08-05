---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["datetime", "m-function"]
---


# DateTime.Time

Returns the time part of the given datetime value, dateTime.

## Signature

```m
DateTime.Time(dateTime as any) as nullable time
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable time

### Example 1

Find the time value of #datetime(2010, 12, 31, 11, 56, 02).

```m
DateTime.Time(#datetime(2010, 12, 31, 11, 56, 02))
```

// Output
```
#time(11, 56, 2)
```

