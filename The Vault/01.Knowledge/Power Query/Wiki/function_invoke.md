---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["function", "m-function"]
---


# Function.Invoke

Invokes the given function using the specified list of arguments and returns the result. Example Invokes Record.FieldNames with one argument [A=1,B=2]. Usage Power Query M Function.Invoke(Record.FieldNames, {[A = 1, B = 2]}) Output {"A", "B"} Last updated on 04/03/2026 --- PAGE 650 ---

## Signature

```m
Function.Invoke(function as function, args as list) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| function | function | |
| args | list | |

## Returns

any

