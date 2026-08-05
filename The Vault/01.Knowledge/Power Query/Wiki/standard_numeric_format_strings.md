---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: reference
tags: ["m-language", "formatting", "numbers"]
---


# Standard Numeric Format Strings

Standard format strings in M use single-letter format specifiers with optional precision. Supported formats: `D` (decimal), `E`/`e` (scientific), `F` (fixed-point), `G`/`g` (general), `N` (number), `P` (percent), `R` (round-trip), `C` (currency), `X`/`x` (hexadecimal).

## Quick Reference

| Specifier | Name | Example | Description |
|-----------|------|---------|-------------|
| `D` or `d` | Decimal | `"42"` | Integers only; pad with leading zeros |
| `E` or `e` | Scientific | `"4.2E+001"` | Exponential notation |
| `F` or `f` | Fixed-point | `"42.00"` | Fixed decimal places |
| `G` or `g` | General | `"42"`, `"0.0001"` | Compact notation |
| `N` or `n` | Number | `"42.00"` | With thousand separators |
| `P` or `p` | Percent | `"4,200.00%"` | Multiplies by 100 |
| `R` or `r` | Round-trip | `"42"` | Lossless round-trip for doubles |
| `C` or `c` | Currency | `"$42.00"` | Locale-aware currency |
| `X` or `x` | Hex | `"2A"` | Hexadecimal integers |

## Syntax

```
Number.ToText(number, format as text, optional culture as text)
```

## Examples

```m
Number.ToText(1234.567, "N2")         // "1,234.57"
Number.ToText(0.42, "P1")             // "42.0%"
Number.ToText(255, "X")               // "FF"
Number.ToText(255, "X4")              // "00FF"
Number.ToText(3.14159, "R")           // "3.14159"
```

## Related

- [[custom_numeric_format_strings]] — custom format patterns
- [[culture_and_text_formatting]] — culture-aware formatting
