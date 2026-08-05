---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.FromText

Creates a date value from a textual representation. text: A text value to covert to a date. options: An optional record that can be provided to specify additional properties. The record can contain the following fields: Format: A text value indicating the format to use. For more details, go to Standard date and time format strings and Custom date and time format strings. Omitting this field or providing null results in parsing the date using a best effort. Culture: When Format isn't null, Culture controls some format specifiers. For example, in "en-US" "MMM" is "Jan", "Feb", "Mar", ..., while in "ru-RU" "MMM" is "янв", "фев", "мар", .... When Format is null, Culture controls the default format to use. When Culture is null or omitted, Culture.Current is used. To support legacy workflows, options can also be a text value. This has the same behavior as if options = [Format = null, Culture = options].

## Signature

```m
Date.FromText(text as nullable text, optional options as any) as nullable date
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| optional options | any | |

## Returns

nullable date

### Example 1

Convert "2010-12-31" into a date value.

```m
Date.FromText("2010-12-31")
```

// Output
```
#date(2010, 12, 31)
```

### Example 2

Convert using a custom format and the German culture.

```m
Date.FromText("30 Dez 2010", [Format="dd MMM yyyy", Culture="de-DE"])
```

// Output
```
#date(2010, 12, 30)
```

### Example 3

Find the date in the Gregorian calendar that corresponds to the beginning of 1400 in the Hijri calendar.

```m
Date.FromText("1400", [Format="yyyy", Culture="ar-SA"])
```

// Output
```
#date(1979, 11, 20)
```

### Example 4

Convert the Italian text dates with abbreviated months in the Posted Date column to date values.

```m
let
Source = #table(type table [Account Code = text, Posted Date = text, Sales =
number],
{
{"US-2004", "20 gen. 2023", 580},
{"CA-8843", "18 lug. 2024", 280},
{"PA-1274", "12 gen. 2023", 90},
{"PA-4323", "14 apr. 2023", 187},
{"US-1200", "14 dic. 2023", 350},
{"PTY-507", "4 giu. 2024", 110}
}),
#"Converted Date" = Table.TransformColumns(
Source,
{"Posted Date", each Date.FromText(_, [Culture = "it-IT"]), type date}
)
in
#"Converted Date"
```

// Output
```
#table(type table [Account Code = text, Posted Date = date, Sales = number],
{
{"US-2004", #date(2023, 1, 20), 580},
{"CA-8843", #date(2024, 7, 18), 280},
{"PA-1274", #date(2023, 1, 12), 90},
{"PA-4323", #date(2023, 4, 14), 187},
{"US-1200", #date(2023, 12, 14), 350},
{"PTY-507", #date(2024, 6, 4), 110}
})
```

## Related

[[culture_and_text_formatting]]
[[standard_date_and_time_format_strings]]
[[custom_date_and_time_format_strings]]

