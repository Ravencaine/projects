---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["datetimezone", "m-function"]
---


# DateTimeZone.From

Creates a datetimezone from the given value. value: The value used to create a datetimezone. culture: (Optional) The culture to use when transforming the value (for example, "en-US"). Values of the following types can be converted to a datetimezone value: text: Returns a datetimezone value from textual representation. Refer to DateTimeZone.FromText for details. date: Returns a datetimezone with value as the date component, 12:00:00 AM as the time component, and the offset corresponding the local time zone. datetime: Returns a datetimezone with value as the datetime and the offset corresponding the local time zone. datetimezone: Returns value. time: Returns a datetimezone with the date equivalent of the OLE Automation Date of 0 as the date component, value as the time component, and the offset corresponding the local time zone. The OLE Automation Date consists of a floating-point number whose integral component is the number of days before or after midnight, 30 December 1899, and whose fractional component represents the time on that day divided by 24. For example, midnight, 31 December 1899 is represented by 1.0; 6 A.M., 1 January 1900 is represented by 2.25; midnight, 29 December 1899 is represented by -1.0; and 6 A.M., 29 December 1899 is represented by -1.25. The base value is midnight, 30 December 1899. The minimum value is midnight, 1 January 0100. The maximum value is the last moment of 31 December 9999. number: Returns a datetimezone with the datetime equivalent of the OLE Automation Date expressed by value and the offset corresponding the local time zone. --- PAGE 600 --- null: Returns null. If value is of any other type, an error is returned. The value of the offset corresponding to the local time zone is different when running this function locally as opposed to running it online. When run locally, the local time zone is returned. When run online, the UTC time zone (+00:00) is returned.

## Signature

```m
DateTimeZone.From(value as any, optional culture as nullable text) as nullable
datetimezone
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| optional culture | nullable text | |

## Returns

nullable datetimezone

### Example 1

Convert the textual representation of a date, time, and timezone to a datetimezone value.

```m
DateTimeZone.From("2020-10-30T01:30:00-08:00")
```

// Output
```
#datetimezone(2020, 10, 30, 01, 30, 00, -8, 00)
```

### Example 2

Convert the textual representation of Brazilian Portuguese date, time, and timezone to a datetimezone value.

```m
DateTimeZone.From("13 de agosto de 2025 15:43:00 -03:00", "pt-BR")
```

// Output
```
#datetimezone(2025, 08, 13, 15, 43, 00, -3, 00)
```

### Example 3

Convert a number representing January 1, 2025 at 12 PM to a datetimezone value. The timezone in the result depends on whether the example is run locally or online.

```m
DateTimeZone.From(45658.5)
```

// Output
```
#datetimezone(2025, 01, 01, 12, 00, 00, 0, 00)
```

## Related

[[culture_and_text_formatting]]
[[local_fixed_and_utc_variants_of_current_time_functions]]
[[standard_date_and_time_format_strings]]
[[custom_date_and_time_format_strings]]
[[number_from]]

