---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["combiner", "m-function"]
---


# Combiner.CombineTextByEachDelimiter

Returns a function that combines a list of text values into a single text value using a sequence of delimiters.

## Signature

```m
Combiner.CombineTextByEachDelimiter(delimiters as list, optional quoteStyle as
nullable number) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| delimiters | list | |
| optional quoteStyle | nullable number | |

## Returns

function

### Example 1

Combine a list of text values using a sequence of delimiters.

```m
Combiner.CombineTextByEachDelimiter({"=", "+"})({"a", "b", "c"})
```

// Output
```
"a=b+c"
```

