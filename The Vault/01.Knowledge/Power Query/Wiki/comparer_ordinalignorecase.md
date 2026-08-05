---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["comparer", "m-function"]
---


# Comparer.OrdinalIgnoreCase

Returns a case-insensitive comparer function which uses Ordinal rules to compare the provided values x and y. A comparer function accepts two arguments and returns -1, 0, or 1 based on whether the first value is less than, equal to, or greater than the second.

## Signature

```m
Comparer.OrdinalIgnoreCase(x as any, y as any) as number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | any | |
| y | any | |

## Returns

number

### Example 1

Using case-insensitive Ordinal rules, compare "Abc" with "abc". Note "Abc" is less than "abc" using Comparer.Ordinal.

```m
Comparer.OrdinalIgnoreCase("Abc", "abc")
```

// Output
```
0
Date functions
Article • 05/28/2025
These functions create and manipulate the date component of date, datetime, and
datetimezone values.
ﾉ Expand table
Name Description
Date.AddDays Returns a Date/DateTime/DateTimeZone value with the day portion
incremented by the number of days provided. It also handles incrementing
the month and year portions of the value as appropriate.
Date.AddMonths Returns a DateTime value with the month portion incremented by n
months.
Date.AddQuarters Returns a Date/DateTime/DateTimeZone value incremented by the number
of quarters provided. Each quarter is defined as a duration of three months.
It also handles incrementing the year portion of the value as appropriate.
Date.AddWeeks Returns a Date/DateTime/DateTimeZone value incremented by the number
of weeks provided. Each week is defined as a duration of seven days. It also
handles incrementing the month and year portions of the value as
appropriate.
Date.AddYears Returns a DateTime value with the year portion incremented by n years.
Date.Day Returns the day for a DateTime value.
Date.DayOfWeek Returns a number (from 0 to 6) indicating the day of the week of the
provided value.
Date.DayOfWeekName Returns the day of the week name.
Date.DayOfYear Returns a number that represents the day of the year from a DateTime
value.
Date.DaysInMonth Returns the number of days in the month from a DateTime value.
Date.EndOfDay Returns the end of the day.
Date.EndOfMonth Returns the end of the month.
Date.EndOfQuarter Returns the end of the quarter.
Date.EndOfWeek Returns the end of the week.
Date.EndOfYear Returns the end of the year.
Date.From Returns a date value from a value.
Name Description
Date.FromText Creates a Date from local, universal, and custom Date formats.
Date.IsInCurrentDay Indicates whether the given datetime value dateTime occurs during the
current day, as determined by the current date and time on the system.
Date.IsInCurrentMonth Returns a logical value indicating whether the given
Date/DateTime/DateTimeZone occurred during the current month, as
determined by the current date and time on the system.
Date.IsInCurrentQuarter Returns a logical value indicating whether the given
Date/DateTime/DateTimeZone occurred during the current quarter, as
determined by the current date and time on the system.
Date.IsInCurrentWeek Returns a logical value indicating whether the given
Date/DateTime/DateTimeZone occurred during the current week, as
determined by the current date and time on the system.
Date.IsInCurrentYear Returns a logical value indicating whether the given
Date/DateTime/DateTimeZone occurred during the current year, as
determined by the current date and time on the system.
Date.IsInNextDay Indicates whether the given datetime value dateTime occurs during the
next day, as determined by the current date and time on the system.
Date.IsInNextMonth Returns a logical value indicating whether the given
Date/DateTime/DateTimeZone occurred during the next month, as
determined by the current date and time on the system.
Date.IsInNextNDays Indicates whether the given datetime value dateTime occurs during the
next number of days, as determined by the current date and time on the
system.
Date.IsInNextNMonths Indicates whether the given datetime value dateTime occurs during the
next number of months, as determined by the current date and time on the
system.
Date.IsInNextNQuarters Indicates whether the given datetime value dateTime occurs during the
next number of quarters, as determined by the current date and time on
the system.
Date.IsInNextNWeeks Indicates whether the given datetime value dateTime occurs during the
next number of weeks, as determined by the current date and time on the
system.
Date.IsInNextNYears Indicates whether the given datetime value dateTime occurs during the
next number of years, as determined by the current date and time on the
system.
Date.IsInNextQuarter Returns a logical value indicating whether the given
Date/DateTime/DateTimeZone occurred during the next quarter, as
Name Description
determined by the current date and time on the system.
Date.IsInNextWeek Returns a logical value indicating whether the given
Date/DateTime/DateTimeZone occurred during the next week, as
determined by the current date and time on the system.
Date.IsInNextYear Returns a logical value indicating whether the given
Date/DateTime/DateTimeZone occurred during the next year, as
determined by the current date and time on the system.
Date.IsInPreviousDay Indicates whether the given datetime value dateTime occurs during the
previous day, as determined by the current date and time on the system.
Date.IsInPreviousMonth Returns a logical value indicating whether the given
Date/DateTime/DateTimeZone occurred during the previous month, as
determined by the current date and time on the system.
Date.IsInPreviousNDays Indicates whether the given datetime value dateTime occurs during the
previous number of days, as determined by the current date and time on
the system.
Date.IsInPreviousNMonths Indicates whether the given datetime value dateTime occurs during the
previous number of months, as determined by the current date and time on
the system.
Date.IsInPreviousNQuarters Indicates whether the given datetime value dateTime occurs during the
previous number of quarters, as determined by the current date and time
on the system.
Date.IsInPreviousNWeeks Indicates whether the given datetime value dateTime occurs during the
previous number of weeks, as determined by the current date and time on
the system.
Date.IsInPreviousNYears Indicates whether the given datetime value dateTime occurs during the
previous number of years, as determined by the current date and time on
the system.
Date.IsInPreviousQuarter Returns a logical value indicating whether the given
Date/DateTime/DateTimeZone occurred during the previous quarter, as
determined by the current date and time on the system.
Date.IsInPreviousWeek Returns a logical value indicating whether the given
Date/DateTime/DateTimeZone occurred during the previous week, as
determined by the current date and time on the system.
Date.IsInPreviousYear Returns a logical value indicating whether the given
Date/DateTime/DateTimeZone occurred during the previous year, as
determined by the current date and time on the system.
Name Description
Date.IsInYearToDate Returns a logical value indicating whether the given
Date/DateTime/DateTimeZone occurred in the period starting January 1st
of the current year and ending on the current day, as determined by the
current date and time on the system.
Date.IsLeapYear Returns a logical value indicating whether the year portion of a DateTime
value is a leap year.
Date.Month Returns the month from a DateTime value.
Date.MonthName Returns the name of the month component.
Date.QuarterOfYear Returns a number between 1 and 4 for the quarter of the year from a
DateTime value.
Date.StartOfDay Returns the start of the day.
Date.StartOfMonth Returns the start of the month.
Date.StartOfQuarter Returns the start of the quarter.
Date.StartOfWeek Returns the start of the week.
Date.StartOfYear Returns the start of the year.
Date.ToRecord Returns a record containing parts of a Date value.
Date.ToText Returns a text value from a Date value.
Date.WeekOfMonth Returns a number for the count of week in the current month.
Date.WeekOfYear Returns a number for the count of week in the current year.
Date.Year Returns the year from a DateTime value.
#date Creates a date value from year, month, and day.
```

