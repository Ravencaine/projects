---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["splitter", "m-function"]
---


# Splitter.SplitTextByRanges

Returns a function that splits text into a list of text according to the specified offsets and lengths. A null length indicates that all remaining input should be included.

## Signature

```m
Splitter.SplitTextByRanges(ranges as list, optional startAtEnd as nullable logical)
as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| ranges | list | |
| optional startAtEnd | nullable logical | |

## Returns

function

### Example 1

Split the input by the specified position and length pairs, starting from the beginning of the input. Note that the ranges in this example overlap.

```m
Splitter.SplitTextByRanges({{0, 4}, {2, 10}})("codelimiter")
```

// Output
```
{"code", "delimiter"}
```

### Example 2

Split the input by the specified position and length pairs, starting from the end of the input.

```m
let
startAtEnd = true
in
Splitter.SplitTextByRanges({{0, 5}, {6, 2}}, startAtEnd)("RedmondWA?98052")
```

// Output
```
{"WA", "98052"}
```

### Example 3

Split the input into a fixed-length postal code followed by a variable-length city name.

```m
Splitter.SplitTextByRanges({{0, 5}, {5, null}})("98052Redmond")
```

// Output
```
{"98052", "Redmond"}
Last updated on 04/03/2026
```

