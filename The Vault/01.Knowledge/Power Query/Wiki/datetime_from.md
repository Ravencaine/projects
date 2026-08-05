---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["datetime", "m-function"]
---


# DateTime.From

Returns a datetime value from the given value. An optional culture may also be provided (for example, "en-US"). If the given value is null, DateTime.From returns null. If the given value is datetime, value is returned. Values of the following types can be converted to a datetime value: text: A datetime value from textual representation. Refer to DateTime.FromText for details. date: A datetime with value as the date component and 12:00:00 AM as the time component. datetimezone: The local datetime equivalent of value. time: A datetime with the date equivalent of the OLE Automation Date of 0 as the date component and value as the time component. number: A datetime equivalent of the OLE Automation Date expressed by value. If value is of any other type, an error is returned.

## Signature

```m
DateTime.From(value as any, optional culture as nullable text) as nullable
datetime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| optional culture | nullable text | |

## Returns

nullable datetime

### Example 1

Convert #time(06, 45, 12) to a datetime value.

```m
DateTime.From(#time(06, 45, 12))
```

// Output
```
#datetime(1899, 12, 30, 06, 45, 12)
```

### Example 2

Convert #date(1975, 4, 4) to a datetime value.

```m
DateTime.From(#date(1975, 4, 4))
```

// Output
```
#datetime(1975, 4, 4, 0, 0, 0)
```

## Related

[[culture_and_text_formatting]]
[[standard_date_and_time_format_strings]]
[[custom_date_and_time_format_strings]]

