---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["splitter", "m-function"]
---


# Splitter.SplitTextByAnyDelimiter

Returns a function that splits text into a list of text at any of the specified delimiters.

## Signature

```m
Splitter.SplitTextByAnyDelimiter(
delimiters as list,
optional quoteStyle as nullable number,
optional startAtEnd as nullable logical
) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| delimiters | list | |
| optional quoteStyle | nullable number | |
| optional startAtEnd | nullable logical | |

## Returns

function

### Example 1

Split the input by comma or semicolon, ignoring quotes and quoted delimiters and starting from the beginning of the input.

```m
Splitter.SplitTextByAnyDelimiter({",", ";"}, QuoteStyle.Csv)("a,b;""c,d;e"",f")
```

// Output
```
{"a", "b", "c,d;e", "f"}
```

### Example 2

Split the input by comma or semicolon, ignoring quotes and quoted delimiters and starting from the end of the input.

```m
let
startAtEnd = true
in
Splitter.SplitTextByAnyDelimiter({",", ";"}, QuoteStyle.Csv, startAtEnd)
("a,""b;c,d")
```

// Output
```
{"a,b", "c", "d"}
```

