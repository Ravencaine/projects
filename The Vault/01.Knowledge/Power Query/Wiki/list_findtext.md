---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.FindText

Returns a list of the values from the list list which contained the value text.

## Signature

```m
List.FindText(list as list, text as text) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| text | text | |

## Returns

list

### Example 1

Find the text values in the list {"a", "b", "ab"} that match "a".

```m
List.FindText({"a", "b", "ab"}, "a")
```

// Output
```
{"a", "ab"}
```

