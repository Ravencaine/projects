---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.Proper

Returns the result of capitalizing only the first letter of each word in text value text. All other letters are returned in lowercase. An optional culture may also be provided (for example, "en-US").

## Signature

```m
Text.Proper(text as nullable text, optional culture as nullable text) as nullable
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

Use Text.Proper on a simple sentence.

```m
Text.Proper("the QUICK BrOWn fOx jUmPs oVER tHe LAzy DoG")
```

// Output
```
"The Quick Brown Fox Jumps Over The Lazy Dog"
```

## Related

[[culture_and_text_formatting]]
[[exchange]]
[[summarize_this_article_for_me]]

[[exchange]]




[[about]]

