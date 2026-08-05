---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["splitter", "m-function"]
---


# Splitter.SplitTextByPositions

Returns a function that splits text into a list of text at each specified position.

## Signature

```m
Splitter.SplitTextByPositions(positions as list, optional startAtEnd as nullable
logical) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| positions | list | |
| optional startAtEnd | nullable logical | |

## Returns

function

### Example 1

Split the input at the specified positions, starting from the beginning of the input.

```m
Splitter.SplitTextByPositions({0, 3, 4})("ABC|12345")
```

// Output
```
{"ABC", "|", "12345"}
```

### Example 2

Split the input at the specified positions, starting from the end of the input.

```m
let
startAtEnd = true
in
Splitter.SplitTextByPositions({0, 5}, startAtEnd)("Redmond98052")
```

// Output
```
{"Redmond", "98052"}
```

