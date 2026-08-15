---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [datetimezone, m-function]
---


# DateTimeZone.ZoneHours

Returns the time zone hour component of a datetimezone value. dateTimeZone: A datetimezone value from which the time zone hour component is extracted. If dateTimeZone is null, the function returns null.

## Signature

```m
DateTimeZone.ZoneHours(dateTimeZone as nullable datetimezone) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTimeZone | nullable datetimezone | |

## Returns

nullable number

### Example 1

Get the time zone hours component of the specified datetimezone value.

```m
DateTimeZone.ZoneHours(#datetimezone(2024, 4, 28, 13, 24, 22, 7, 30))
```

// Output
```
7
```

