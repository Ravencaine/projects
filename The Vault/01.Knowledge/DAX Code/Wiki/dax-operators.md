---
created: 2026-07-26
source: dax.pdf
note_type: reference
tags: [dax, reference, operators]
---

# DAX Operators

DAX supports arithmetic, comparison, logical, concatenation, and IN operators for building expressions.

## Quick Reference

### Arithmetic Operators

| Operator | Description |
|----------|-------------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division (returns error on divide-by-zero) |
| `^` | Exponentiation |

### Comparison Operators

| Operator | Description |
|----------|-------------|
| `=` | Equal to |
| `<>` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

### Logical Operators

| Operator | Description |
|----------|-------------|
| `&&` | AND (both conditions must be true) |
| `||` | OR (either condition must be true) |
| `NOT` | Logical negation |

### Text Operators

| Operator | Description |
|----------|-------------|
| `&` | Concatenation (always produces string) |
| `=` | Equal (string comparison is case-insensitive) |
| `<>` | Not equal |

### IN Operator

```dax
'Product'[Color] IN {"Red", "Blue", "Green"}
'Date'[Year] IN {2020, 2021, 2022}
```

The IN operator checks membership. `NOT IN` is not a DAX operator — use `NOT <expression> IN {...}`.

## Notes

- DAX string comparison is **case-insensitive** (unlike SQL)
- The `&` operator always returns a string, even when concatenating numbers
- Mixing text and numeric types with `+` can produce unexpected results — use `CONCATENATE` or `&` for strings
- Parentheses control operator precedence: `(2 + 3) * 4 = 20` vs `2 + 3 * 4 = 14`

## Related

- [[dax-syntax]] — reference
- [[dax-overview]] — atomic
