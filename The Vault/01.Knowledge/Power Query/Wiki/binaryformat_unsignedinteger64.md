---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["binaryformat", "m-function"]
---


# BinaryFormat.UnsignedInteger64

A binary format that reads a 64-bit unsigned integer. --- PAGE 468 --- #binary 09/16/2025 Syntax #binary(value as any) as any About Creates a binary value from a list of numbers or a base 64 encoded text value.

## Signature

```m
BinaryFormat.UnsignedInteger64(binary as binary) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| binary | binary | |

## Returns

any

### Example 1

Create a binary value from a list of numbers.

```m
#binary({0x30, 0x31, 0x32})
```

// Output
```
Text.ToBinary("012")
```

### Example 2

Create a binary value from a base 64 encoded text value.

```m
#binary("1011")
```

// Output
```
Binary.FromText("1011", BinaryEncoding.Base64)
Combiner functions
Article • 11/14/2024
These functions are used by other library functions that merge values. For example,
Table.ToList and Table.CombineColumns apply a combiner function to each row in a
table to produce a single value for each row.
ﾉ Expand table
Name Description
Combiner.CombineTextByDelimiter Returns a function that combines a list of text using the
specified delimiter.
Combiner.CombineTextByEachDelimiter Returns a function that combines a list of text using a
sequence of delimiters.
Combiner.CombineTextByLengths Returns a function that combines a list of text using the
specified lengths.
Combiner.CombineTextByPositions Returns a function that combines a list of text using the
specified output positions.
Combiner.CombineTextByRanges Returns a function that combines a list of text using the
specified positions and lengths.
Feedback
Was this page helpful?  Yes  No
Provide product feedback | Ask the community
```

