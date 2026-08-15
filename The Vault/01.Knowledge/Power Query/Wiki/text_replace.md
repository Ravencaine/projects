---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [text, m-function]
---


# Text.Replace

Returns the result of replacing all occurrences of text value old in text value text with text value new. This function is case sensitive.

## Signature

```m
Text.Replace(
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

Replace every occurrence of "the" in a sentence with "a".

```m
Text.Replace("the quick brown fox jumps over the lazy dog", "the", "a")
```

// Output
```
"a quick brown fox jumps over a lazy dog"
```

