---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["splitter", "m-function"]
---


# Splitter.SplitTextByEachDelimiter

Returns a function that splits text into a list of text at each specified delimiter in sequence.

## Signature

```m
Splitter.SplitTextByEachDelimiter(
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

Split the input by comma, then semicolon, starting from the beginning of the input.

```m
Splitter.SplitTextByEachDelimiter({",", ";"})("a,b;c,d")
```

// Output
```
{"a", "b", "c,d"}
```

### Example 2

Split the input by comma, then semicolon, treating quotes like any other character and starting from the end of the input.

```m
let
startAtEnd = true
in
Splitter.SplitTextByEachDelimiter({",", ";"}, QuoteStyle.None, startAtEnd)
("a,""b;c"",d")
```

// Output
```
{"a,""b", "c""", "d"}
```

