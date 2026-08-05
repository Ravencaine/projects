---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["replacer", "m-function"]
---


# Replacer.ReplaceText

Replaces the old text in the original text with the new text. This replacer function can be used in List.ReplaceValue and Table.ReplaceValue.

## Signature

```m
Replacer.ReplaceText(
text as nullable text,
old as text,
new as text
) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| old | text | |
| new | text | |

## Returns

nullable text

### Example 1

Replace the text "hE" with "He" in the string "hEllo world".

```m
Replacer.ReplaceText("hEllo world", "hE", "He")
```

// Output
```
"Hello world"
```

