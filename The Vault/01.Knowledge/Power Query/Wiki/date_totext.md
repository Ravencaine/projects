---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [date, m-function]
---


# Date.ToText

Returns a textual representation of date. An optional record parameter, options, may be provided to specify additional properties. culture is only used for legacy workflows. The record can contain the following fields: Format: A text value indicating the format to use. For more details, go to Standard date and time format strings and Custom date and time format strings. Omitting this field or providing null will result in formatting the date using the default defined by Culture. Culture: When Format is not null, Culture controls some format specifiers. For example, in "en-US" "MMM" is "Jan", "Feb", "Mar", ..., while in "ru-RU" "MMM" is "янв", "фев", "мар", .... When Format is null, Culture controls the default format to use. When Culture is null or omitted, Culture.Current is used. To support legacy workflows, options and culture may also be text values. This has the same behavior as if options = [Format = options, Culture = culture].

## Signature

```m
Date.ToText(
date as nullable date,
optional options as any,
optional culture as nullable text
) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| date | nullable date | |
| optional options | any | |
| optional culture | nullable text | |

## Returns

nullable text

### Example 1

Convert #date(2010, 12, 31) into a text value. Result output may vary depending on current culture.

```m
Date.ToText(#date(2010, 12, 31))
```

// Output
```
"12/31/2010"
```

### Example 2

Convert using a custom format and the German culture.

```m
Date.ToText(#date(2010, 12, 31), [Format="dd MMM yyyy", Culture="de-DE"])
```

// Output
```
"31 Dez 2010"
```

### Example 3

Find the year in the Hijri calendar that corresponds to January 1st, 2000 in the Gregorian calendar.

```m
Date.ToText(#date(2000, 1, 1), [Format="yyyy", Culture="ar-SA"])
```

// Output
```
"1420"
```

## Related

[[culture_and_text_formatting]]
[[standard_date_and_time_format_strings]]
[[custom_date_and_time_format_strings]]

