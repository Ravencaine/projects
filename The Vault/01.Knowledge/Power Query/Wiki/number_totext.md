---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.ToText

Converts the numeric value number to a text value according to the format specified by format. The format is a text value indicating how the number should be converted. For more details on the supported format values, go to Standard numeric format strings and Custom numeric format strings. An optional culture may also be provided (for example, "en-US") to control the culture- dependent behavior of format.

## Signature

```m
Number.ToText(
number as nullable number,
optional format as nullable text,
optional culture as nullable text
) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number | nullable number | |
| optional format | nullable text | |
| optional culture | nullable text | |

## Returns

nullable text

### Example 1

Convert a number to text without specifying a format.

```m
Number.ToText(4)
```

// Output
```
"4"
```

### Example 2

Convert a number to exponential format.

```m
Number.ToText(4, "e")
```

// Output
```
"4.000000e+000"
```

### Example 3

Convert a number to percentage format with only one decimal place.

```m
Number.ToText(-0.1234, "P1")
```

// Output
```
"-12.3 %"
```

## Related

[[culture_and_text_formatting]]
[[standard_numeric_format_strings]]
[[custom_numeric_format_strings]]

