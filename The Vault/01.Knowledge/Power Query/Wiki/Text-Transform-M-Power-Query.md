---
created: 2026-08-05
updated: 2026-08-05
source: 10 Excel Data Cleaning Hacks That Save Hours Every Week (DigitalBYKewat)
note_type: reference
tags: [power-query, m-code, text-transform, text.trim, text.clean, text.proper]
---

# Text Transform M Functions in Power Query

Power Query equivalents for Excel's TRIM, CLEAN, PROPER, UPPER, and LOWER functions — for repeatable, formula-driven text cleaning in the Power Query Editor.

## The M Equivalents

| Excel | Power Query M | What it does |
|-------|--------------|-------------|
| `=TRIM(A2)` | `Text.Trim(text)` | Removes leading/trailing spaces; collapses multiple spaces |
| `=CLEAN(A2)` | `Text.Clean(text)` | Removes non-printable characters (includes CHAR(160)) |
| `=PROPER(A2)` | `Text.Proper(text)` | Capitalises the first letter of each word |
| `=UPPER(A2)` | `Text.Upper(text)` | Converts all letters to uppercase |
| `=LOWER(A2)` | `Text.Lower(text)` | Converts all letters to lowercase |

## CLEAN Difference: M vs Excel

Power Query's `Text.Clean` removes a broader set of characters than Excel's `CLEAN()` — specifically it handles CHAR(160) (non-breaking space) which Excel's CLEAN does not. For PDF-copied or web-scraped data, `Text.Clean` is more thorough.

## Combining Trim and Clean

```m
Text.Clean(Text.Trim([ColumnName]))
```

Same pattern as Excel's `CLEAN(TRIM())` — Trim first, then Clean.

## Applying in Power Query

1. Select the column
2. **Transform → Format** (ribbon group)
3. Choose: Trim, Clean, To Upper, To Lower, To Capitalize Each Word

Or write directly in the formula bar:

```m
= Table.TransformColumns(Source, {{"ColumnName", each Text.Clean(Text.Trim(_)), type text}})
```

## Repeatable vs One-Time

Power Query transformations are stored as query steps — they replay on every data refresh. Excel formulas are cell-level and must be re-applied manually. Use Power Query for any dataset that will be refreshed or reused.

## Related

- [[TRIM-CLEAN-Functions]] (Excel) — Excel-side TRIM and CLEAN
- [[Text-Case-Functions]] (Excel) — Excel-side PROPER, UPPER, LOWER
- [[Inconsistent-Categories-Normalisation]] (Data Modeling) — Power Query dimension lookup tables for legacy name mapping
