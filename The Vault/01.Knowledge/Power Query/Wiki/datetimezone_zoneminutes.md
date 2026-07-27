---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["datetimezone", "m-function"]
---


# DateTimeZone.ZoneMinutes

Returns the time zone minutes component of a datetimezone value. dateTimeZone: A datetimezone value from which the time zone minutes component is extracted. If dateTimeZone is null, the function returns null. Example Get the time zone minutes component of the specified datetimezone value. Usage Power Query M DateTimeZone.ZoneMinutes(#datetimezone(2024, 4, 28, 13, 24, 22, 7, 30)) Output 30 Last updated on 04/03/2026 --- PAGE 617 --- #datetimezone 09/16/2025 Syntax #datetimezone( year as number, month as number, day as number, hour as number, minute as number, second as number, offsetHours as number, offsetMinutes as number ) as datetimezone About Creates a datetimezone value from numbers representing the year, month, day, hour, minute, (fractional) second, (fractional) offset-hours, and offset-minutes. Raises an error if these conditions are not true: 1 ≤ year ≤ 9999 1 ≤ month ≤ 12 1 ≤ day ≤ 31 0 ≤ hour ≤ 23 0 ≤ minute ≤ 59 0 ≤ second < 60 -14 ≤ offset-hours + offset-minutes / 60 ≤ 14 --- PAGE 618 --- Duration functions Article • 01/29/2025 These functions create and manipulate duration values. ﾉ Expand table Name Description Duration.Days Returns the days portion of a duration. Duration.From Creates a duration from the given value. Duration.FromText Returns a duration value from a text value. Duration.Hours Returns the hours portion of a duration. Duration.Minutes Returns the minutes portion of a duration. Duration.Seconds Returns the seconds portion of a duration. Duration.ToRecord Returns a record containing the parts of the duration. Duration.TotalDays Returns the total days this duration spans. Duration.TotalHours Returns the total hours this duration spans. Duration.TotalMinutes Returns the total minutes this duration spans. Duration.TotalSeconds Returns the total seconds this duration spans. Duration.ToText Returns the text of the form "d.h:m:s". #duration Creates a duration value from days, hours, minutes, and seconds. Feedback Was this page helpful?  Yes  No Provide product feedback | Ask the community --- PAGE 619 ---

## Signature

```m
DateTimeZone.ZoneMinutes(dateTimeZone as nullable datetimezone) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTimeZone | nullable datetimezone | |

## Returns

nullable number

