---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["datetimezone", "m-function"]
---


# DateTimeZone.RemoveZone

Returns a #datetime value from dateTimeZone with timezone information removed.

## Signature

```m
DateTimeZone.RemoveZone(dateTimeZone as nullable datetimezone) as nullable
datetime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTimeZone | nullable datetimezone | |

## Returns

nullable datetime

### Example 1

Remove timezone information from the value #datetimezone(2011, 12, 31, 9, 15, 36, -7, 0).

```m
DateTimeZone.RemoveZone(#datetimezone(2011, 12, 31, 9, 15, 36, -7, 0))
```

// Output
```
#datetime(2011, 12, 31, 9, 15, 36)
```

