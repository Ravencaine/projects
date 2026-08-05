---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["datetime", "m-function"]
---


# DateTime.AddZone

Adds timezone information to the dateTime value. The timezone information includes timezoneHours and optionally timezoneMinutes, which specify the desired offset from UTC time.

## Signature

```m
DateTime.AddZone(
dateTime as nullable datetime,
timezoneHours as number,
optional timezoneMinutes as nullable number
) as nullable datetimezone
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | nullable datetime | |
| timezoneHours | number | |
| optional timezoneMinutes | nullable number | |

## Returns

nullable datetimezone

### Example 1

Set the timezone to UTC+7:30 (7 hours and 30 minutes past UTC).

```m
DateTime.AddZone(#datetime(2010, 12, 31, 11, 56, 02), 7, 30)
```

// Output
```
#datetimezone(2010, 12, 31, 11, 56, 2, 7, 30)
```

