---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["single", "m-function"]
---


# Single.From

Returns a Single number value from the given value. If the given value is null, Single.From returns null. If the given value is number within the range of Single, value is returned, otherwise an error is returned. If value is of any other type, it will first be converted to a number using Number.FromText. An optional culture may also be provided (for example, "en-US").

## Signature

```m
Single.From(value as any, optional culture as nullable text) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| optional culture | nullable text | |

## Returns

nullable number

### Example 1

Get the Single number value of "1.5".

```m
Single.From("1.5")
```

// Output
```
1.5
```

## Related

[[culture_and_text_formatting]]
[[record_functions]]

[[these_functions_create_and_manipulate_record_values]]
[[information]]
[[table_expandrecordcolumn]]
[[name_description]]
[[record_fieldcount_returns_the_number_of_fields_in_a_record]]
[[record_hasfields_returns_true_if_the_field_name_or_field_names_are_present_in_a_record]]
[[transformation]]

