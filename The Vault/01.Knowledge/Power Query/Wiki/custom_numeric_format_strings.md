---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: reference
tags: [m-language, formatting, numbers]
---


# Custom Numeric Format Strings

Custom numeric format strings use placeholder characters to build format patterns. Supports placeholders (0, #, ., ,, %), literals, and escape sequences.

## Quick Reference

| Character | Meaning |
|-----------|---------|
| `0` | Zero placeholder — digit or trailing zero |
| `#` | Digit placeholder — digit or nothing |
| `.` | Decimal separator |
| `,` | Thousand separator / scale |
| `%` | Percent placeholder — multiplies by 100 |
| `‰` | Per-mille placeholder — multiplies by 1000 |
| `E0`, `E-0` | Scientific notation |

## Examples

```m
Number.ToText(1234.567, "00000")       // "01235" (rounds and pads)
Number.ToText(1234.567, "#####")      // "1235"
Number.ToText(12.34, "0.00")          // "12.34"
Number.ToText(1234567, "#,##0.00")     // "1,234,567.00"
Number.ToText(0.42, "0%")             // "42%"
Number.ToText(42, "00.00")            // "42.00"
Number.ToText(42.5, "00.00")          // "42.50"
Number.ToText(1.5, "0.0#")           // "1.50"
```

## Notes

- `0` forces display of zeros; `#` omits leading/trailing zeros
- Multiple `,` in the format apply grouping (thousands)
- `%%` produces a literal `%`

## Related

- [[standard_numeric_format_strings]] — standard format specifiers
