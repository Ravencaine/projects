---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["splitter", "m-function"]
---


# Splitter.SplitTextByDelimiter

Returns a function that splits text into a list of text according to the specified delimiter.

## Signature

```m
Splitter.SplitTextByDelimiter(
delimiter as text,
optional quoteStyle as nullable number,
optional csvStyle as nullable number
) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| delimiter | text | |
| optional quoteStyle | nullable number | |
| optional csvStyle | nullable number | |

## Returns

function

### Example 1

Split the input by comma, ignoring quoted commas.

```m
Splitter.SplitTextByDelimiter(",", QuoteStyle.Csv)("a,""b,c"",d")
```

// Output
```
{"a", "b,c", "d"}
```

