---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [datetimezone, m-function]
---


# DateTimeZone.UtcNow

Returns the current date and time in UTC (the GMT timezone).

## Signature

```m
DateTimeZone.UtcNow() as datetimezone
```

## Returns

datetimezone

### Example 1

Get the current date & time in UTC.

```m
DateTimeZone.UtcNow()
```

// Output
```
#datetimezone(2011, 8, 16, 23, 34, 37.745, 0, 0)
```

## Related

[[local_fixed_and_utc_variants_of_current_time_functions]]

