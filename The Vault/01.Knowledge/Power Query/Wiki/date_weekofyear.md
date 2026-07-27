---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.WeekOfYear

Returns a number from 1 to 54 indicating which week of the year the date, dateTime, falls in. dateTime: A datetime value for which the week-of-the-year is determined. firstDayOfWeek: An optional Day.Type value that indicates which day is considered the start of a new week (for example, Day.Sunday). If unspecified, a culture-dependent default is used.

## Signature

```m
Date.WeekOfYear(dateTime as any, optional firstDayOfWeek as nullable number) as
nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |
| optional firstDayOfWeek | nullable number | |

## Returns

nullable number

### Example 1

Determine which week of the year contains March 27th, 2011.

```m
Date.WeekOfYear(#date(2011, 03, 27))
```

// Output
```
14
```

### Example 2

Determine which week of the year contains March 27th, 2011, using Monday as the start of the week.

```m
Power Query M
Date.WeekOfYear(#date(2011, 03, 27), Day.Monday)
```

// Output
```
13
```

## Related

[[culture_and_text_formatting]]

