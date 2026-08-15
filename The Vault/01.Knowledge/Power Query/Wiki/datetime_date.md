---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [datetime, m-function]
---


# DateTime.Date

Returns the date component of the dateTime parameter if the parameter is a date, datetime, or datetimezone value, or null if the parameter is null.

## Signature

```m
DateTime.Date(dateTime as any) as nullable date
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable date

### Example 1

Find date value of #datetime(2010, 12, 31, 11, 56, 02).

```m
DateTime.Date(#datetime(2010, 12, 31, 11, 56, 02))
```

// Output
```
#date(2010, 12, 31)
```

