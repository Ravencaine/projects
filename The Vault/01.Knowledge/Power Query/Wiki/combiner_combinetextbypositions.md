---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["combiner", "m-function"]
---


# Combiner.CombineTextByPositions

Returns a function that combines a list of text values into a single text value using the specified output positions. Example Combine a list of text values by placing them in the output at the specified positions. Usage Power Query M Combiner.CombineTextByPositions({0, 5, 10})({"abc", "def", "ghi"}) Output "abc def ghi" Last updated on 04/02/2026 --- PAGE 476 ---

## Signature

```m
Combiner.CombineTextByPositions(positions as list, optional template as nullable
text) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| positions | list | |
| optional template | nullable text | |

## Returns

function

