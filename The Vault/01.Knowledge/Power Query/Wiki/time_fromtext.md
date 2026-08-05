---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["time", "m-function"]
---


# Time.FromText

Creates a time value from a textual representation, text. An optional record parameter, options, may be provided to specify additional properties. The record can contain the following fields: Format: A text value indicating the format to use. For more details, go to Standard date and time format strings and Custom date and time format strings. Omitting this field or providing null will result in parsing the time using a best effort. Culture: When Format is not null, Culture controls some format specifiers. For example, in "en-US" "tt" is "AM" or "PM", while in "ar-EG" "tt" is "ص" or "م". When Format is null, Culture controls the default format to use. When Culture is null or omitted, Culture.Current is used. To support legacy workflows, options may also be a text value. This has the same behavior as if options = [Format = null, Culture = options].

## Signature

```m
Time.FromText(text as nullable text, optional options as any) as nullable time
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| optional options | any | |

## Returns

nullable time

### Example 1

Convert "10:12:31am" into a Time value.

```m
Time.FromText("10:12:31am")
```

// Output
```
#time(10, 12, 31)
```

### Example 2

Convert "1012" into a Time value.

```m
Time.FromText("1012")
```

// Output
```
#time(10, 12, 00)
```

### Example 3

Convert "10" into a Time value.

```m
Time.FromText("10")
```

// Output
```
#time(10, 00, 00)
```

## Related

[[culture_and_text_formatting]]
[[standard_date_and_time_format_strings]]
[[custom_date_and_time_format_strings]]

