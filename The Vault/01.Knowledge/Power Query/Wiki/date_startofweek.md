---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.StartOfWeek

Returns the start of the week that contains dateTime. dateTime must be a date, datetime, or datetimezone value.

## Signature

```m
Date.StartOfWeek(dateTime as any, optional firstDayOfWeek as nullable number) as
any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| optional firstDayOfWeek | nullable number | |

## Returns

any

### Example 1

Find the start of the week for Tuesday, October 11th, 2011.

```m
Date.StartOfWeek(#datetime(2011, 10, 11, 8, 10, 32))
```

// Output
```
// Sunday, October 9th, 2011
#datetime(2011, 10, 9, 0, 0, 0)
```

### Example 2

Find the start of the week for Tuesday, October 11th, 2011, using Monday as the start of the week.

```m
Date.StartOfWeek(#datetime(2011, 10, 11, 8, 10, 32), Day.Monday)
```

// Output
```
// Monday, October 10th, 2011
#datetime(2011, 10, 10, 0, 0, 0)
```

