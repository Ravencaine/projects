---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["datetimezone", "m-function"]
---


# DateTimeZone.ToLocal

Changes timezone information of the datetimezone value dateTimeZone to the local timezone information. If dateTimeZone does not have a timezone component, the local timezone information is added.

## Signature

```m
DateTimeZone.ToLocal(dateTimeZone as nullable datetimezone) as nullable
datetimezone
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTimeZone | nullable datetimezone | |

## Returns

nullable datetimezone

### Example 1

Change timezone information for #datetimezone(2010, 12, 31, 11, 56, 02, 7, 30) to local timezone (assuming PST).

```m
DateTimeZone.ToLocal(#datetimezone(2010, 12, 31, 11, 56, 02, 7, 30))
```

// Output
```
#datetimezone(2010, 12, 31, 12, 26, 2, -8, 0)
```

