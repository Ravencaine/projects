---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["replacer", "m-function"]
---


# Replacer.ReplaceValue

Replaces the old value in the original value with the new value. This replacer function can be used in List.ReplaceValue and Table.ReplaceValue. Example Replace the value 11 with the value 10. Usage Power Query M Replacer.ReplaceValue(11, 11, 10) Output 10 Last updated on 04/03/2026 --- PAGE 913 --- Splitter functions Article • 08/04/2022 These functions split text. Name Description Splitter.SplitByNothing Returns a function that does no splitting, returning its argument as a single element list. Splitter.SplitTextByCharacterTransition Returns a function that splits text into a list of text according to a transition from one kind of character to another. Splitter.SplitTextByAnyDelimiter Returns a function that splits text by any supported delimiter. Splitter.SplitTextByDelimiter Returns a function that will split text according to a delimiter. Splitter.SplitTextByEachDelimiter Returns a function that splits text by each delimiter in turn. Splitter.SplitTextByLengths Returns a function that splits text according to the specified lengths. Splitter.SplitTextByPositions Returns a function that splits text according to the specified positions. Splitter.SplitTextByRanges Returns a function that splits text according to the specified ranges. Splitter.SplitTextByRepeatedLengths Returns a function that splits text into a list of text after the specified length repeatedly. Splitter.SplitTextByWhitespace Returns a function that splits text according to whitespace. Feedback Was this page helpful? ﾂ Yes ﾄ No Get help at Microsoft Q&A --- PAGE 914 ---

## Signature

```m
Replacer.ReplaceValue(
value as any,
old as any,
new as any
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| old | any | |
| new | any | |

## Returns

any

