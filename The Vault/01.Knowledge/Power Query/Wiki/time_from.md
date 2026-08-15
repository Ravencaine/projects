---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [time, m-function]
---


# Time.From

Returns a time value from the given value. An optional culture may also be provided (for example, "en-US"). If the given value is null, Time.From returns null. If the given value is time, value is returned. Values of the following types can be converted to a time value: text: A time value from textual representation. Refer to Time.FromText for details. datetime: The time component of the value. datetimezone: The time component of the local datetime equivalent of value. number: A time equivalent to the number of fractional days expressed by value. If value is negative or greater or equal to 1, an error is returned. If value is of any other type, an error is returned.

## Signature

```m
Time.From(value as any, optional culture as nullable text) as nullable time
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| optional culture | nullable text | |

## Returns

nullable time

### Example 1

Convert 0.7575 to a time value.

```m
Time.From(0.7575)
```

// Output
```
#time(18, 10, 48)
```

### Example 2

```m
Time.From(#datetime(1899, 12, 30, 06, 45, 12))
```

// Output
```
#time(06, 45, 12)
```

## Related

[[culture_and_text_formatting]]
[[standard_date_and_time_format_strings]]
[[custom_date_and_time_format_strings]]

