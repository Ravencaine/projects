---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["binary", "m-function"]
---


# Binary.From

Returns a binary value from the given value. If the given value is null, Binary.From returns null. If the given value is binary, value is returned. Values of the following types can be converted to a binary value: text: A binary value from the text representation. Refer to Binary.FromText for details. If value is of any other type, an error is returned. Example Get the binary value of "1011". Usage Power Query M Binary.From("1011") Output Binary.FromText("1011", BinaryEncoding.Base64) Last updated on 03/24/2026 --- PAGE 426 ---

## Signature

```m
Binary.From(value as any, optional encoding as nullable number) as nullable binary
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| optional encoding | nullable number | |

## Returns

nullable binary

