---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.ReplaceValue

Searches a list of values, list, for the value oldValue and replaces each occurrence with the replacement value newValue.

## Signature

```m
List.ReplaceValue(
list as list,
oldValue as any,
newValue as any,
replacer as function
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| oldValue | any | |
| newValue | any | |
| replacer | function | |

## Returns

list

### Example 1

Replace all the "a" values in the list {"a", "B", "a", "a"} with "A".

```m
List.ReplaceValue({"a", "B", "a", "a"}, "a", "A", Replacer.ReplaceText)
```

// Output
```
{"A", "B", "A", "A"}
```

