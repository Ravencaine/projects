---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["binary", "m-function"]
---


# Binary.ViewFunction

Creates a view function based on function that can be handled in a view created by Binary.View. The OnInvoke handler of Binary.View can be used to define a handler for the view function. As with the handlers for built-in operations, if no OnInvoke handler is specified, or if it does not handle the view function, or if an error is raised by the handler, function is applied on top of the view. Refer to the published Power Query custom connector documentation for a more complete description of Binary.View and custom view functions. --- PAGE 439 --- BinaryFormat.7BitEncodedSignedInteger 09/16/2025 Syntax BinaryFormat.7BitEncodedSignedInteger(binary as binary) as any About A binary format that reads a 64-bit signed integer that was encoded using a 7-bit variable- length encoding. --- PAGE 440 --- BinaryFormat.7BitEncodedUnsignedInteger 09/16/2025 Syntax BinaryFormat.7BitEncodedUnsignedInteger(binary as binary) as any About A binary format that reads a 64-bit unsigned integer that was encoded using a 7-bit variable- length encoding. --- PAGE 441 ---

## Signature

```m
Binary.ViewFunction(function as function) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| function | function | |

## Returns

function

