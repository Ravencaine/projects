---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [binaryformat, m-function]
---


# BinaryFormat.Transform

Returns a binary format that will transform the values read by another binary format. The binaryFormat parameter specifies the binary format that will be used to read the value. The function is invoked with the value read, and returns the transformed value.

## Signature

```m
BinaryFormat.Transform(binaryFormat as function, function as function) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| binaryFormat | function | |
| function | function | |

## Returns

function

### Example 1

Read a byte and add one to it.

```m
let
binaryData = #binary({1}),
transformFormat = BinaryFormat.Transform(
BinaryFormat.Byte,
(x) => x + 1
)
in
transformFormat(binaryData)
```

// Output
```
2
```

