---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [binary, m-function]
---


# Binary.InferContentType

Returns a record with field Content.Type that contains the inferred MIME-type. If the inferred content type is text/*, and an encoding code page is detected, then additionally returns field Content.Encoding that contains the encoding of the stream. If the inferred content type is text/csv, and the format is delimited, additionally returns field Csv.PotentialDelimiter containing a table for analysis of potential delimiters. If the inferred content type is text/csv, and the format is fixed-width, additionally returns field Csv.PotentialPositions containing a list for analysis of potential fixed width column positions. --- PAGE 430 ---

## Signature

```m
Binary.InferContentType(source as binary) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| source | binary | |

## Returns

record

