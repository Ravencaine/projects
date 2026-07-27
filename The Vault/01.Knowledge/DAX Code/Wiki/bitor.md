---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# BITOR

Returns a bitwise OR of two numbers.

## Syntax

```dax
BITOR(<number1>, <number2>)
```

## Parameters

| Term | Definition |
|------|------------|
| `number1` | Any scalar expression that returns a number. Non-integers are truncated. |
| `number2` | Any scalar expression that returns a number. Non-integers are truncated. |

## Return Value

A single integer value representing the bitwise OR result.

## Remarks

Each bit position in the result is 1 if either corresponding bit in the inputs is 1. Equivalent to: value1 | value2 in binary representation.