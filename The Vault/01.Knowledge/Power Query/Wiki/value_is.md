---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [value, m-function]
---


# Value.Is

Determines whether a value is compatible with the specified type. This is equivalent to the "is" operator in M, with the exception that it can accept identifier type references such as Number.Type. Example Compare two ways of determining if a number is compatible with type number. Usage Power Query M Value.Is(123, Number.Type) = (123 is number) Output true Last updated on 03/24/2026 --- PAGE 1318 ---

## Signature

```m
Value.Is(value as any, type as type) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| type | type | |

## Returns

logical

