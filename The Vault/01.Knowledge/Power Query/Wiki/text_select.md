---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [text, m-function]
---


# Text.Select

Returns a copy of the text value text with all the characters not in selectChars removed.

## Signature

```m
Text.Select(text as nullable text, selectChars as any) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| selectChars | any | |

## Returns

nullable text

### Example 1

Select all characters in the range of 'a' to 'z' from the text value.

```m
Text.Select("a,b;c", {"a".."z"})
```

// Output
```
"abc"
```

