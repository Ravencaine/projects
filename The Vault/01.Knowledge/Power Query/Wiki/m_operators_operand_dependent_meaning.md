---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: gotcha
tags: ["m-language", "operators", "types"]
---


# Operators Have Operand-Dependent Meaning — Same Operator, Different Behaviour

M operators behave differently depending on the types of their operands. The `+` operator does number addition, text concatenation, and date arithmetic. The `&` operator concatenates text, lists, and merges records.

## Examples

| Expression | Result Type | Meaning |
|-----------|-------------|---------|
| `1 + 2` | number | Addition |
| `"A" & "B"` | text | Text concatenation |
| `#date(2025,1,1) + #duration(1,0,0,0)` | date | Date shifted |
| `{{1}} & {{2,3}}` | list | List concatenation |
| `[a=1] & [b=2]` | record | Record merge |

## Why It Matters

`1 + "2"` is an **error**: you cannot add a number and text. Mixing up the expected types is a common source of errors.

## How to Handle It

- Know the operand types for each operator being used
- Use explicit conversion functions: `Number.From`, `Text.From`
- Check `Value.Type(result)` to understand the result type

## Related

- [[m_operator_behaviour]] — full operator reference
