---
created: 2026-08-09
updated: 2026-08-09
source: "10 Excel Custom Number Formatting Tricks • My Online Training Hub"
note_type: atomic
tags: [excel, formatting, number-format, color, conditional-formatting, red, blue]
---

# Inline Colors in Number Format

Apply colour directly inside a custom number format — no conditional formatting needed. Faster, lighter workbook. Colour applies per section (positive, negative, zero).

## Format

```
[Blue]#,##0;[Red]-#,##0;-
```

| Part | Meaning |
|------|---------|
| `[Blue]` | Positive numbers in blue |
| `[Red]` | Negative numbers in red |
| `-` | Zeros shown as dash |

## Common Colour Names

Excel supports: `[Black]`, `[White]`, `[Red]`, `[Green]`, `[Blue]`, `[Yellow]`, `[Cyan]`, `[Magenta]`, `[Color1-56]`

## Combine with Sign-Aware Scaling

```
[Blue]#,##0.00,,"M";[Red]-#,##0.00,,"M"
```
Blue for positive (millions), red for negative (millions).

## Related

- [[Source-10-Custom-Number-Formatting-Tricks-Mynda-Treacy]] — source
- [[Four-Section-Number-Format-Structure]] — colour codes sit inside each section
- [[Scale-Numbers-to-K-or-M]] — combine with sign-aware colour
