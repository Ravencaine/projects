---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [lines, m-function]
---


# Lines.FromBinary

Converts a binary value to a list of text values split at line breaks. binary: The binary value to convert to the list. quoteStyle: Specifies how line breaks are handled. The value of quoteStyle can be null. The default value is QuoteStyle.None. includeLineSeparators: Specifies whether to include the line break characters in the text. The value of includeLineSeparators can be null. The default value is false. encoding: Specifies the text encoding of the binary value. The value of encoding can be null. The default value is 65001 (UTF-8). If a record is specified for quoteStyle (and includeLineSeparators and encoding are null), the following record fields can be provided: QuoteStyle: Specifies how quoted line breaks are handled. QuoteStyle.Csv: Quoted line breaks are treated as part of the data, not as the end of the current row. QuoteStyle.None: All line breaks are treated as the end of the current row, even when they occur inside a quoted value. This value is the default if the CsvStyle option isn't specified. CsvStyle: Specifies how quotes are handled. Should not be used with QuoteStyle.None. CsvStyle.QuoteAfterDelimiter: Quotes in a field are only significant immediately following the `Delimiter. CsvStyle.QuoteAlways: Quotes in a field are always significant, regardless of where they appear. --- PAGE 658 --- Delimiter: A single character delimiter. Should be used only with CsvStyle.QuoteAfterDelimiter. IncludeLineSeparators: Specifies whether to include the line break characters in the text. The default value is false. Encoding: The text encoding of the binary value. The default value is 65001 (UTF-8). --- PAGE 659 ---

## Signature

```m
Lines.FromBinary(
binary as binary,
optional quoteStyle as any,
optional includeLineSeparators as nullable logical,
optional encoding as nullable number
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| binary | binary | |
| optional quoteStyle | any | |
| optional includeLineSeparators | nullable logical | |
| optional encoding | nullable number | |

## Returns

list

