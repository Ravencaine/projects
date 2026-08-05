---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: atomic
tags: ["m-language", "operators"]
---


# M Operators

M includes operators for arithmetic, comparison, logic, text, lists, and records. Most operators have context-dependent meaning depending on the types of their operands.

## Key Points

- **Arithmetic**: `+`, `-`, `*`, `/`, `^` (power)
- **Comparison**: `=`, `<>`, `>`, `<`, `>=`, `<=`
- **Logical**: `and`, `or`, `not`
- **Text**: `&` (concatenation)
- **List**: `&` (concatenation)
- **Record**: `&` (merge)
- **Null-coalesce**: `??` (returns right operand if left is null)
- Operator meaning depends on operand types

## Examples

```m
// Arithmetic on numbers
1 + 2   // 3
5 - 2   // 3
"Hello" & " " & "World"  // "Hello World"

// Null-coalesce
null ?? "default"   // "default"
"value" ?? "default"  // "value"

// List concatenation
{1, 2} & {3, 4}  // {1, 2, 3, 4}

// Record merge
[A = 1] & [B = 2]   // [A = 1, B = 2]
```

## Related

- [[m_operator_behaviour]] — detailed operator reference
