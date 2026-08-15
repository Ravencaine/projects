---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: reference
tags: [m-language, operators]
---


# M Operator Behaviour

M operators behave differently depending on the types of their operands. This reference documents the key behaviours across type combinations.

## Quick Reference

### Arithmetic

| Expression | Result |
|-----------|--------|
| `x + y` | Addition (number), Date+Duration, DateTime+Duration, Text concatenation |
| `x - y` | Subtraction (number), Date-Date, DateTime-DateTime, Duration subtraction |
| `x * y` | Multiplication (number) |
| `x / y` | Division (number) |
| `x ^ y` | Exponentiation (number) |

### Comparison

All comparisons are type-strict. `1 = "1"` is false. `null = null` is `null` (not true).

### Logical

| Operator | Notes |
|----------|-------|
| `and` | Short-circuit evaluation |
| `or` | Short-circuit evaluation |
| `not` | Unary negation |

### Null Coalesce

`x ?? y` returns `x` if `x` is not null, otherwise `y`.

### Combination

| Expression | Result |
|-----------|--------|
| `list1 & list2` | List concatenation |
| `text1 & text2` | Text concatenation |
| `record1 & record2` | Record merge (right overrides left) |

### Metadata

`x meta y` — attach metadata record `y` to value `x`.

### Lookup

| Expression | Result |
|-----------|--------|
| `record[FieldName]` | Field access by name |
| `record[[fieldname]]` | Field access returning record |
| `list{n}` | List item at zero-based index n |
| `list{n}?` | Safe list item (null if out of range) |

## Notes

- Adding incompatible types (e.g., `1 + "2"`) produces an **error**, not null
- Text comparison is **always case-sensitive** in M
- Date arithmetic is only valid between compatible types

## Related

- [[m_operators]] — operators overview
- [[quoted_identifier_syntax]] — literal syntax
