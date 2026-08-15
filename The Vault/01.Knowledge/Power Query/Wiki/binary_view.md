---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [binary, m-function]
---


# Binary.View

Returns a view of binary where the functions specified in handlers are used in lieu of the default behavior of an operation when the operation is applied to the view. If binary is provided, all handler functions are optional. If binary isn't provided, the GetStream handler function is required. If a handler function isn't specified for an operation, the default behavior of the operation is applied to binary instead (except in the case of GetExpression). Handler functions must return a value that is semantically equivalent to the result of applying the operation against binary (or the resulting view in the case of GetExpression). If a handler function raises an error, the default behavior of the operation is applied to the view. Binary.View can be used to implement folding to a data source – the translation of M queries into source-specific operations (for example, to download a section of a file). Refer to the published Power Query custom connector documentation for a more complete description of Binary.View. Example Create a basic view that doesn't require accessing the data in order to determine the length. Usage Power Query M Binary.View( null, [ GetLength = () => 12, GetStream = () => Text.ToBinary("hello world!") --- PAGE 436 --- ] ) Output Text.ToBinary("hello world!") Last updated on 04/02/2026 --- PAGE 437 --- Binary.ViewError Summarize this article for me Syntax Binary.ViewError(errorRecord as record) as record About Creates a modified error record from errorRecord which won't trigger a fallback when raised by a handler defined on a view (via Binary.View). Last updated on 02/11/2026 --- PAGE 438 ---

## Signature

```m
Binary.View(binary as nullable binary, handlers as record) as binary
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| binary | nullable binary | |
| handlers | record | |

## Returns

binary

