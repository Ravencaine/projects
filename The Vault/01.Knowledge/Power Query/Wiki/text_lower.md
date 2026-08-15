---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [text, m-function]
---


# Text.Lower

Returns the result of converting all characters in text to lowercase. An optional culture may also be provided (for example, "en-US").

## Signature

```m
Text.Lower(text as nullable text, optional culture as nullable text) as nullable
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

Get the lowercase version of "AbCd".

```m
Text.Lower("AbCd")
```

// Output
```
"abcd"
```

## Related

[[culture_and_text_formatting]]

