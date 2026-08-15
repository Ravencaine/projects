---
created: 2026-08-09
updated: 2026-08-09
source: "10 Excel Custom Number Formatting Tricks • My Online Training Hub"
note_type: atomic
tags: [excel, formatting, number-format, custom-format, syntax, structure]
---

# Four-Section Number Format Structure

All custom number formats have up to 4 sections, each separated by a semicolon. Each section controls how one type of value is displayed.

## Syntax

```
Positive ; Negative ; Zero ; Text
```

| Section | Controls |
|---------|----------|
| 1st | Positive numbers |
| 2nd | Negative numbers |
| 3rd | Zero values |
| 4th | Text values |

## Shorthand Rules

- **1 section:** applies to all number types
- **2 sections:** 1st = positive/zero, 2nd = negative
- **3 sections:** positive, negative, zero (in that order)
- **4 sections:** positive, negative, zero, text

## Color and Condition

Each section can also include inline color codes and conditions:

```
[Blue]#,##0;[Red]-#,##0;-
```

- `[Blue]` — color name in square brackets before the format
- `[>=0.5]` — condition in square brackets before the literal text

## Key Principle

The underlying cell value never changes — only the display. Formulas, PivotTables, and charts always use the real numeric value.

## Related

- [[Source-10-Custom-Number-Formatting-Tricks-Mynda-Treacy]] — source
- [[Hide-Zero-Values-with-Format]] — empty 3rd section hides zeros
- [[Inline-Colors-in-Number-Format]] — [Blue]/[Red] color codes
- [[Pass-Fail-via-Number-Format]] — [>=0.5] condition + "Pass"/"Fail" text
