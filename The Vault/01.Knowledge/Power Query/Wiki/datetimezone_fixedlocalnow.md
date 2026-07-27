---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["datetimezone", "m-function"]
---


# DateTimeZone.FixedLocalNow

Returns a datetime value set to the current date and time on the system. The returned value contains timezone information representing the local timezone. This value is fixed and will not change with successive calls, unlike DateTimeZone.LocalNow, which may return different values over the course of execution of an expression. Related content Local, fixed, and UTC variants of current time functions --- PAGE 598 ---

## Signature

```m
DateTimeZone.FixedLocalNow() as datetimezone
```

## Returns

datetimezone

