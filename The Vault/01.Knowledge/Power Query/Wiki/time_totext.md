---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["time", "m-function"]
---


# Time.ToText

Returns a textual representation of time. An optional record parameter, options, may be provided to specify additional properties. culture is only used for legacy workflows. The record can contain the following fields: Format: A text value indicating the format to use. For more details, go to Standard date and time format strings and Custom date and time format strings. Omitting this field or providing null will result in formatting the date using the default defined by Culture. Culture: When Format is not null, Culture controls some format specifiers. For example, in "en-US" "tt" is "AM" or "PM", while in "ar-EG" "tt" is "ص" or "م". When Format is null, Culture controls the default format to use. When Culture is null or omitted, Culture.Current is used. To support legacy workflows, options and culture may also be text values. This has the same behavior as if options = [Format = options, Culture = culture].

## Signature

```m
Time.ToText(
time as nullable time,
optional options as any,
optional culture as nullable text
) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| time | nullable time | |
| optional options | any | |
| optional culture | nullable text | |

## Returns

nullable text

### Example 1

Convert #time(01, 30, 25) into a text value. Result output may vary depending on current culture.

```m
Time.ToText(#time(11, 56, 2))
```

// Output
```
"11:56 AM"
```

### Example 2

Convert using a custom format and the German culture.

```m
Time.ToText(#time(11, 56, 2), [Format="hh:mm", Culture="de-DE"])
```

// Output
```
"11:56"
```

### Example 3

Convert using standard time format.

```m
Time.ToText(#time(11, 56, 2), [Format="T", Culture="de-DE"])
```

// Output
```
"11:56:02"
```

## Related

[[culture_and_text_formatting]]
[[standard_date_and_time_format_strings]]
[[custom_date_and_time_format_strings]]






