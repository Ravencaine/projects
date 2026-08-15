---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [text, m-function]
---


# Text.Remove

Returns a copy of the text value text with all the characters from removeChars removed.

## Signature

```m
Text.Remove(text as nullable text, removeChars as any) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| removeChars | any | |

## Returns

nullable text

### Example 1

Remove characters , and ; from the text value.

```m
Text.Remove("a,b;c", {",",";"})
```

// Output
```
"abc"
```

