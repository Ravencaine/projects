---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["splitter", "m-function"]
---


# Splitter.SplitTextByLengths

Returns a function that splits text into a list of text by each specified length.

## Signature

```m
Splitter.SplitTextByLengths(lengths as list, optional startAtEnd as nullable
logical) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| lengths | list | |
| optional startAtEnd | nullable logical | |

## Returns

function

### Example 1

Split the input into the first two characters followed by the next three, starting from the beginning of the input.

```m
Splitter.SplitTextByLengths({2, 3})("AB123")
```

// Output
```
{"AB", "123"}
```

### Example 2

Split the input into the first three characters followed by the next two, starting from the end of the input.

```m
let
startAtEnd = true
in
Splitter.SplitTextByLengths({5, 2}, startAtEnd)("RedmondWA98052")
{"WA", "98052"}
```

