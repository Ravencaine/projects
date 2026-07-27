---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["binary", "m-function"]
---


# Binary.Buffer

Buffers the binary value in memory. The result of this call is a stable binary value, which means it will have a deterministic length and order of bytes.

## Signature

```m
Binary.Buffer(binary as nullable binary) as nullable binary
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| binary | nullable binary | |

## Returns

nullable binary

### Example 1

Create a stable version of the binary value.

```m
Binary.Buffer(Binary.FromList({0..10}))
```

// Output
```
#binary({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
```

