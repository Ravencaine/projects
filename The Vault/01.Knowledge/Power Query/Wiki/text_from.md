---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.From

Returns the text representation of a specified value. value: The value to convert to text. The value can be a number, date, time, datetime, datetimezone, logical, duration, or binary value. If the given value is null, this function returns null. culture: (Optional) The culture to use when converting the value to text (for example, "en-US").

## Signature

```m
Text.From(value as any, optional culture as nullable text) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| optional culture | nullable text | |

## Returns

nullable text

### Example 1

Create a text value from the number 3.

```m
Text.From(3)
```

// Output
```
"3"
```

### Example 2

Get the text equivalent of the specified date and time.

```m
Text.From(#datetime(2024, 6, 24, 14, 32, 22))
```

// Output
```
"6/24/2024 2:32:22 PM"
```

### Example 3

Get the German text equivalent of the specified date and time.

```m
Text.From(#datetime(2024, 6, 24, 14, 32, 22), "de-DE")
```

// Output
```
"24.06.2024 14:32:22"
```

### Example 4

Get a binary value from text encoded as hexadecimal and change the value back to text.

```m
Text.From(Binary.FromText("10FF", BinaryEncoding.Hex))
```

// Output
```
"EP8="
```

### Example 5

Get the rows in the table that contain data for France and convert the dates to text using the French culture.

```m
let
Source = #table(type table [Company ID = text, Country = text, Date = date],
{
{"JS-464", "USA", #date(2024, 3, 24)},
{"LT-331", "France", #date(2024, 10, 5)},
{"XE-100", "USA", #date(2024, 5, 21)},
{"RT-430", "Germany", #date(2024, 1,18)},
{"LS-005", "France", #date(2023, 12, 31)},
{"UW-220", "Germany", #date(2024, 2, 25)}
}),
#"Convert Dates" = Table.TransformColumns(
Table.SelectRows(Source, each [Country] = "France"),
{"Date", each Text.From(_, "fr-FR")}
)
in
#"Convert Dates"
```

// Output
```
#table(type table [Company ID = text, Country = text, Date = text],
{
{"LT-331", "France", "05/10/2024"},
{"LS-005", "France", "31/12/2023"}
})
```

## Related

[[culture_and_text_formatting]]
[[standard_numeric_format_strings]]
[[custom_numeric_format_strings]]
[[standard_date_and_time_format_strings]]
[[custom_date_and_time_format_strings]]

