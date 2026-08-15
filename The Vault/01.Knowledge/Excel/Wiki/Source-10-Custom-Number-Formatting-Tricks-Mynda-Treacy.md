---
created: 2026-08-09
updated: 2026-08-09
source: "10 Excel Custom Number Formatting Tricks • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/10-excel-custom-number-formatting-tricks"
published: 2026-06-16
note_type: source
tags: [excel, formatting, number-format, custom-format, display, presentation]
---

# 10 Custom Number Formatting Tricks — My Online Training Hub / Mynda Treacy

Source: My Online Training Hub. Published 2026-06-16. Author: Mynda Treacy — already in vault (4th source).

## Summary

10 custom number format tricks that change how numbers display without touching the underlying value. Formulas, PivotTables, and charts continue to work. No helper columns or rewritten formulas needed.

## Core Concept

Custom number formats have 4 sections separated by semicolons:

```
Positive ; Negative ; Zero ; Text
```

Access via Ctrl+1 → Custom.

## The 10 Tricks

| # | Trick | Format Pattern |
|----|-------|---------------|
| 1 | Scale to K/M | `#,##0.00,,"M"` |
| 2 | Inline colours | `[Blue]#,##0;[Red]-#,##0;-` |
| 3 | Pass/Fail text | `[Blue][>=0.5]"Pass";[Red][<0.5]"Fail"` |
| 4 | Hide zeros | `#,##0;-#,##0;` |
| 5 | Symbol arrows | `[Blue]▲ $#,##0;"K";[Red]▼ $#,##0;"K"` |
| 6 | Phone numbers | `"+1 "(000) 000 0000` |
| 7 | Custom dates | `dd-mmm-yy`, `mmmm d, yyyy`, etc. |
| 8 | Inline units | `0" km"`, `0" kg"` |
| 9 | Hide all values | `;;;` |
| 10 | Leading/trailing chars | `@*_` (underscore fill), `*.@` (dot leader) |

## Key Insight

Custom number formats change display only — underlying values remain numeric and usable in formulas and charts.

## Key Insights Extracted

- [[Four-Section-Number-Format-Structure]] — `atomic` — Positive; Negative; Zero; Text — each section controls one value type
- [[Scale-Numbers-to-K-or-M]] — `atomic` — `#,##0.00,,"M"` removes 6 digits; `#,##0.00,"K"` removes 3; keep scale consistent; units in column header
- [[Inline-Colors-in-Number-Format]] — `atomic` — `[Blue]` / `[Red]` inline in format string; replaces conditional formatting for sign-based colour
- [[Pass-Fail-via-Number-Format]] — `atomic` — `[>=0.5]"Pass";[<0.5]"Fail"`; keeps numeric value; no IF formula needed
- [[Hide-Zero-Values-with-Format]] — `atomic` — empty third section (`...;;`) hides zeros; value remains numeric for formulas
- [[Symbol-Arrows-in-Number-Format]] — `atomic` — `▲` / `▼` symbols for positive/negative; `█` in Wingdings for bar charts
- [[Phone-Number-Format-Preserving-Zeroes]] — `atomic` — `"+1 "(000) 000 0000`; leading zeros preserved; consistent formatting
- [[Custom-Date-Formats]] — `atomic` — d/m/yy variants; underlying value stays a real date; grouping and calculations still work
- [[Inline-Units-via-Number-Format]] — `atomic` — `0" km"`; value stays numeric; units in header preferred for large datasets
- [[Hide-All-Cell-Values-Format]] — `atomic` — `;;;` hides all sections; not security; visible in formula bar
- [[Leading-Trailing-Characters-in-Format]] — `atomic` — `@*_` repeats underscore to cell edge; `*.@` creates dot leader; signature lines, TOC entries

## Author

- [[Author-Mynda-Treacy]] — extended (4th source)
