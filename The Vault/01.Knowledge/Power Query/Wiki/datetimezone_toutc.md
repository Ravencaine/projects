---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [datetimezone, m-function]
---


# DateTimeZone.ToUtc

Changes timezone information of the datetime value dateTimeZone to the UTC or Universal Time timezone information. If dateTimeZone does not have a timezone component, the UTC timezone information is added.

## Signature

```m
DateTimeZone.ToUtc(dateTimeZone as nullable datetimezone) as nullable datetimezone
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTimeZone | nullable datetimezone | |

## Returns

nullable datetimezone

### Example 1

Change timezone information for #datetimezone(2010, 12, 31, 11, 56, 02, 7, 30) to UTC timezone.

```m
DateTimeZone.ToUtc(#datetimezone(2010, 12, 31, 11, 56, 02, 7, 30))
```

// Output
```
#datetimezone(2010, 12, 31, 4, 26, 2, 0, 0)
```

