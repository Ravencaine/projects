---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["splitter", "m-function"]
---


# Splitter.SplitTextByRepeatedLengths

Returns a function that splits text into a list of text after the specified length repeatedly.

## Signature

```m
Splitter.SplitTextByRepeatedLengths(length as number, optional startAtEnd as
nullable logical) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| length | number | |
| optional startAtEnd | nullable logical | |

## Returns

function

### Example 1

Repeatedly split the input into chunks of three characters, starting from the beginning of the input.

```m
Splitter.SplitTextByRepeatedLengths(3)("12345678")
```

// Output
```
{"123", "456", "78"}
```

### Example 2

Repeatedly split the input into chunks of three characters, starting from the end of the input.

```m
let
startAtEnd = true
in
Splitter.SplitTextByRepeatedLengths(3, startAtEnd)("87654321")
```

// Output
```
{"87", "654", "321"}
```

