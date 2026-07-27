---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["lines", "m-function"]
---


# Lines.ToBinary

Converts a list of text into a binary value using the specified encoding and lineSeparator.The specified lineSeparator is appended to each line. If not specified then the carriage return and line feed characters are used. --- PAGE 662 ---

## Signature

```m
Lines.ToBinary(
lines as list,
optional lineSeparator as nullable text,
optional encoding as nullable number,
optional includeByteOrderMark as nullable logical
) as binary
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| lines | list | |
| optional lineSeparator | nullable text | |
| optional encoding | nullable number | |
| optional includeByteOrderMark | nullable logical | |

## Returns

binary

