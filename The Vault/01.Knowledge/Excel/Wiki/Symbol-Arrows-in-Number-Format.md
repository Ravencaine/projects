---
created: 2026-08-09
updated: 2026-08-09
source: "10 Excel Custom Number Formatting Tricks • My Online Training Hub"
note_type: atomic
tags: [excel, formatting, number-format, symbols, arrows, icons, up-down, delta]
---

# Symbol Arrows in Number Format

Add directional symbols (▲/▼) directly into the number format string for at-a-glance interpretation of positive and negative values — no formulas or conditional formatting needed.

## Format

```
[Blue]▲ $#,##0,"K";[Red]▼ $#,##0,"K";
```

| Section | Display |
|---------|---------|
| Positive | ▲ in blue, formatted value |
| Negative | ▼ in red, formatted value |
| Zero | blank |

## Symbol Sources

- **Wingdings / Wingdings 3** font: arrow characters (█ for bar charts, P/Q/R for directional)
- **Unicode symbols:** ▲ ▼ △ ▽ ↑ ↓ ✔ ✘ ★ ●
- **Insert tab → Symbols:** browse full character set

## Related

- [[Source-10-Custom-Number-Formatting-Tricks-Mynda-Treacy]] — source
- [[Inline-Colors-in-Number-Format]] — colour codes combine with symbols
- [[Scale-Numbers-to-K-or-M]] — combine scaling with directional symbols
