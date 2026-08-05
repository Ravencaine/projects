---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.Upper

Returns the result of converting all characters in text to uppercase. An optional culture may also be provided (for example, "en-US").

## Signature

```m
Text.Upper(text as nullable text, optional culture as nullable text) as nullable
text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| optional culture | nullable text | |

## Returns

nullable text

### Example 1

Get the uppercase version of "aBcD".

```m
Text.Upper("aBcD")
```

// Output
```
"ABCD"
```

## Related

[[culture_and_text_formatting]]
[[time_functions]]

[[these_functions_create_and_manipulate_time_values]]
[[name_description]]
[[time_endofhour_returns_the_end_of_the_hour]]
[[time_from_returns_a_time_value_from_a_value]]
[[time_fromtext_creates_a_time_from_local_universal_and_custom_time_formats]]
[[time_hour_returns_an_hour_value_from_a_datetime_value]]
[[time_minute_returns_a_minute_value_from_a_datetime_value]]

