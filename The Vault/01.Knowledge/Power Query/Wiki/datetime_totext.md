---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["datetime", "m-function"]
---


# DateTime.ToText

Returns a textual representation of dateTime. An optional record parameter, options, may be provided to specify additional properties. culture is only used for legacy workflows. The record can contain the following fields: Format: A text value indicating the format to use. For more details, go to Standard date and time format strings and Custom date and time format strings. Omitting this field or providing null will result in formatting the date using the default defined by Culture. Culture: When Format is not null, Culture controls some format specifiers. For example, in "en-US" "MMM" is "Jan", "Feb", "Mar", ..., while in "ru-RU" "MMM" is "янв", "фев", "мар", .... When Format is null, Culture controls the default format to use. When Culture is null or omitted, Culture.Current is used. To support legacy workflows, options and culture may also be text values. This has the same behavior as if options = [Format = options, Culture = culture].

## Signature

```m
DateTime.ToText(
dateTime as nullable datetime,
optional options as any,
optional culture as nullable text
) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | nullable datetime | |
| optional options | any | |
| optional culture | nullable text | |

## Returns

nullable text

### Example 1

Convert #datetime(2010, 12, 31, 01, 30, 25) into a text value. Result output may vary depending on current culture.

```m
DateTime.ToText(#datetime(2010, 12, 31, 01, 30, 25))
```

// Output
```
"12/31/2010 1:30:25 AM"
```

### Example 2

Convert using a custom format and the German culture.

```m
DateTime.ToText(#datetime(2010, 12, 30, 2, 4, 50.36973), [Format="dd MMM yyyy
HH:mm:ss.ffffff", Culture="de-DE"])
```

// Output
```
"30 Dez 2010 02:04:50.369730"
```

### Example 3

Convert using the ISO 8601 pattern.

```m
DateTime.ToText(#datetime(2000, 2, 8, 3, 45, 12),[Format="yyyy-MM-
dd'T'HH:mm:ss'Z'", Culture="en-US"])
```

// Output
```
"2000-02-08T03:45:12Z"
```

## Related

[[culture_and_text_formatting]]
[[standard_date_and_time_format_strings]]
[[custom_date_and_time_format_strings]]






