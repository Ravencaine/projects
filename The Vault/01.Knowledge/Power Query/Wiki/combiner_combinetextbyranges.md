---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["combiner", "m-function"]
---


# Combiner.CombineTextByRanges

Returns a function that combines a list of text values into a single text value using the specified output positions and lengths. A null length indicates that the entire text value should be included. Example Combine a list of text values using the specified output positions and lengths. Usage Power Query M Combiner.CombineTextByRanges({{0, 1}, {3, 2}, {6, null}})({"abc", "def", "ghijkl"}) Output "a de ghijkl" Last updated on 04/02/2026 --- PAGE 477 --- Comparer functions Article • 11/22/2024 These functions test equality and determine ordering. ﾉ Expand table Name Description Comparer.Equals Returns a logical value based on the equality check over the two given values. Comparer.FromCulture Returns a comparer function based on the specified culture and case-sensitivity. Comparer.Ordinal Returns a comparer function which uses Ordinal rules to compare values. Comparer.OrdinalIgnoreCase Returns a case-insensitive comparer function which uses Ordinal rules to compare the provided values. Feedback Was this page helpful?  Yes  No Provide product feedback | Ask the community --- PAGE 478 ---

## Signature

```m
Combiner.CombineTextByRanges(ranges as list, optional template as nullable text) as
function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| ranges | list | |
| optional template | nullable text | |

## Returns

function

