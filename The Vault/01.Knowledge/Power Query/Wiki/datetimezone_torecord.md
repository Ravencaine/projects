---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["datetimezone", "m-function"]
---


# DateTimeZone.ToRecord

Returns a record containing the parts of the given datetimezone value, dateTimeZone. dateTimeZone: A datetimezone value for from which the record of its parts is to be calculated.

## Signature

```m
DateTimeZone.ToRecord(dateTimeZone as datetimezone) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTimeZone | datetimezone | |

## Returns

record

### Example 1

Convert the #datetimezone(2011, 12, 31, 11, 56, 2, 8, 0) value into a record containing Date, Time, and Zone values.

```m
DateTimeZone.ToRecord(#datetimezone(2011, 12, 31, 11, 56, 2, 8, 0))
```

// Output
```
[
Year = 2011,
Month = 12,
Day = 31,
Hour = 11,
Minute = 56,
Second = 2,
ZoneHours = 8,
ZoneMinutes = 0
]
```

