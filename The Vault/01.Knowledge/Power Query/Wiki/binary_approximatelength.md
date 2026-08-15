---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [binary, m-function]
---


# Binary.ApproximateLength

Returns the approximate length of binary, or an error if the data source doesn't support an approximate length.

## Signature

```m
Binary.ApproximateLength(binary as nullable binary) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| binary | nullable binary | |

## Returns

nullable number

### Example 1

Get the approximate length of the binary value.

```m
Binary.ApproximateLength(Binary.FromText("i45WMlSKjQUA", BinaryEncoding.Base64))
```

// Output
```
9
```

