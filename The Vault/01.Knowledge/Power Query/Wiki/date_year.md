---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.Year

Returns the year component of the provided datetime value, dateTime. Example Find the year in #datetime(2011, 12, 31, 9, 15, 36). Usage Power Query M Date.Year(#datetime(2011, 12, 31, 9, 15, 36)) Output 2011 Last updated on 03/24/2026 --- PAGE 559 --- #date 09/16/2025 Syntax #date( year as number, month as number, day as number ) as date About Creates a date value from whole numbers representing the year, month, and day. Raises an error if these conditions are not true: 1 ≤ year ≤ 9999 1 ≤ month ≤ 12 1 ≤ day ≤ 31

## Signature

```m
Date.Year(dateTime as any) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

nullable number

### Example 1

Create a date representing December 26, 2023.

```m
#date(2023, 12, 26)
```

// Output
```
#date(2023, 12, 26)
```

### Example 2

Convert a date to text using a custom format and the German culture.

```m
Power Query M
Date.ToText(#date(2023, 12, 26), [Format="dd MMM yyyy", Culture="de-DE"])
```

// Output
```
"26 Dez 2023"
```

### Example 3

Get the rows from a table that contain a date in 2023.

```m
let
Source = #table(type table [Account Code = text, Posted Date = date, Sales =
number],
{
{"US-2004", #date(2023,1,20), 580},
{"CA-8843", #date(2023,7,18), 280},
{"PA-1274", #date(2022,1,12), 90},
{"PA-4323", #date(2023,4,14), 187},
{"US-1200", #date(2022,12,14), 350},
{"PTY-507", #date(2023,6,4), 110}
}),
#"Filtered rows" = Table.SelectRows(
Source,
each Date.Year([Posted Date]) = 2023
)
in
#"Filtered rows"
```

// Output
```
#table (type table [Account Code = text, Posted Date = date, Sales = number],
{
{"US-2004", #date(2023, 1, 20), 580},
{"CA-8843", #date(2023, 7, 18), 280},
{"PA-4323", #date(2023, 4, 14), 187},
{"PTY-507", #date(2023, 6, 4), 110}
})
DateTime functions
Article • 11/22/2024
These functions create and manipulate datetime and datetimezone values.
ﾉ Expand table
Name Description
DateTime.AddZone Adds timezone information to the datetime value.
DateTime.Date Returns the date component of the given date, datetime, or
datetimezone value.
DateTime.FixedLocalNow Returns the current date and time in the local timezone. This
value is fixed and doesn't change with successive calls.
DateTime.From Creates a datetime from the given value.
DateTime.FromFileTime Creates a datetime from a 64-bit long number.
DateTime.FromText Creates a datetime from local and universal datetime formats.
DateTime.IsInCurrentHour Indicates whether this datetime occurs during the current hour,
as determined by the current date and time on the system.
DateTime.IsInCurrentMinute Indicates whether this datetime occurs during the current
minute, as determined by the current date and time on the
system.
DateTime.IsInCurrentSecond Indicates whether this datetime occurs during the current
second, as determined by the current date and time on the
system.
DateTime.IsInNextHour Indicates whether this datetime occurs during the next hour, as
determined by the current date and time on the system. This
function returns false when passed a value that occurs within
the current hour.
DateTime.IsInNextMinute Indicates whether this datetime occurs during the next minute,
as determined by the current date and time on the system. This
function returns false when passed a value that occurs within
the current minute.
DateTime.IsInNextNHours Indicates whether this datetime occurs during the next number
of hours, as determined by the current date and time on the
system. This function returns false when passed a value that
occurs within the current hour.
Name Description
DateTime.IsInNextNMinutes Indicates whether this datetime occurs during the next number
of minutes, as determined by the current date and time on the
system. This function returns false when passed a value that
occurs within the current minute.
DateTime.IsInNextNSeconds Indicates whether this datetime occurs during the next number
of seconds, as determined by the current date and time on the
system. This function returns false when passed a value that
occurs within the current second.
DateTime.IsInNextSecond Indicates whether this datetime occurs during the next second,
as determined by the current date and time on the system. This
function returns false when passed a value that occurs within
the current second.
DateTime.IsInPreviousHour Indicates whether this datetime occurs during the previous
hour, as determined by the current date and time on the
system. This function returns false when passed a value that
occurs within the current hour.
DateTime.IsInPreviousMinute Indicates whether this datetime occurs during the previous
minute, as determined by the current date and time on the
system. This function returns false when passed a value that
occurs within the current minute.
DateTime.IsInPreviousNHours Indicates whether this datetime occurs during the previous
number of hours, as determined by the current date and time
on the system. This function returns false when passed a
value that occurs within the current hour.
DateTime.IsInPreviousNMinutes Indicates whether this datetime occurs during the previous
number of minutes, as determined by the current date and
time on the system. This function returns false when passed a
value that occurs within the current minute.
DateTime.IsInPreviousNSeconds Indicates whether this datetime occurs during the previous
number of seconds, as determined by the current date and
time on the system. This function returns false when passed a
value that occurs within the current second.
DateTime.IsInPreviousSecond Indicates whether this datetime occurs during the previous
second, as determined by the current date and time on the
system. This function returns false when passed a value that
occurs within the current second.
DateTime.LocalNow Returns the current date and time in the local timezone.
DateTime.Time Returns the time part of the given datetime value.
Name Description
DateTime.ToRecord Returns a record containing the datetime value's parts.
DateTime.ToText Returns a textual representation of the datetime value.
#datetime Creates a datetime value from year, month, day, hour, minute,
and second.
Feedback
Was this page helpful?  Yes  No
Provide product feedback | Ask the community
```

