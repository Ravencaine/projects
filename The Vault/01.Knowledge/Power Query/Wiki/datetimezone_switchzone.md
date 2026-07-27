---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["datetimezone", "m-function"]
---


# DateTimeZone.SwitchZone

Changes timezone information to on the datetimezone value dateTimeZone to the new timezone information provided by timezoneHours and optionally timezoneMinutes. If dateTimeZone does not have a timezone component, an error is raised.

## Signature

```m
DateTimeZone.SwitchZone(
dateTimeZone as nullable datetimezone,
timezoneHours as number,
optional timezoneMinutes as nullable number
) as nullable datetimezone
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTimeZone | nullable datetimezone | |
| timezoneHours | number | |
| optional timezoneMinutes | nullable number | |

## Returns

nullable datetimezone

### Example 1

Change timezone information for #datetimezone(2010, 12, 31, 11, 56, 02, 7, 30) to 8 hours.

```m
DateTimeZone.SwitchZone(#datetimezone(2010, 12, 31, 11, 56, 02, 7, 30), 8)
```

// Output
```
#datetimezone(2010, 12, 31, 12, 26, 2, 8, 0)
```

### Example 2

Change timezone information for #datetimezone(2010, 12, 31, 11, 56, 02, 7, 30) to -30 minutes.

```m
DateTimeZone.SwitchZone(#datetimezone(2010, 12, 31, 11, 56, 02, 7, 30), 0, -30)
```

// Output
```
#datetimezone(2010, 12, 31, 3, 56, 2, 0, -30)
Last updated on 01/22/2026
```

