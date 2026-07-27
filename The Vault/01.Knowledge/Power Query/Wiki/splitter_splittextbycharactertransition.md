---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["splitter", "m-function"]
---


# Splitter.SplitTextByCharacterTransition

Returns a function that splits text into a list of text according to a transition from one kind of character to another. The before and after parameters can either be a list of characters, or a function that takes a character and returns true/false. Example Split the input whenever an upper or lowercase letter is followed by a digit. Usage Power Query M Splitter.SplitTextByCharacterTransition({"A".."Z", "a".."z"}, {"0".."9"})("Abc123") Output {"Abc", "123"} Last updated on 03/24/2026 --- PAGE 918 ---

## Signature

```m
Splitter.SplitTextByCharacterTransition(before as anynonnull, after as anynonnull)
as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| before | anynonnull | |
| after | anynonnull | |

## Returns

function

