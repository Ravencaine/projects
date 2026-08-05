---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["number", "m-function"]
---


# Number.FromText

Returns a number value from the given text value, text. text: The textual representation of a number value. The representation must be in a common number format, such as "15", "3,423.10", or "5.0E-10". culture: An optional culture that controls how text is interpreted (for example, "en-US").

## Signature

```m
Number.FromText(text as nullable text, optional culture as nullable text) as
nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| optional culture | nullable text | |

## Returns

nullable number

### Example 1

Get the number value of "4".

```m
Number.FromText("4")
```

// Output
```
4
```

### Example 2

Get the number value of "5.0e-10".

```m
Number.FromText("5.0e-10")
```

// Output
```
5E-10
```

## Related

[[culture_and_text_formatting]]
[[standard_numeric_format_strings]]
[[custom_numeric_format_strings]]

