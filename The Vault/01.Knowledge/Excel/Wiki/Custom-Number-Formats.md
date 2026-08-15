---
created: 2026-08-08
updated: 2026-08-08
source: "6 Excel features I use in every spreadsheet I create"
source_url: https://www.howtogeek.com/microsoft-excel-features-i-use-in-every-spreadsheet/
author:
  - name: Tony Phillips
    source: How-To Geek
note_type: atomic
tags: [excel, number-format, display, units, abbreviation]
related:
  - "[[conditional-formatting]]"
  - "[[Excel-Table-Ctrl-T]]"
---

# Custom Number Formats

Custom number formats (Format Cells → Ctrl+1 → Custom) change how values display on-screen without altering the underlying cell value. Formulas, PivotTables, and charts always use the raw number — the format is purely visual.

## Syntax

Custom format codes use sections separated by semicolons:

```
positive; negative; zero; text
```

Each section defines the display format for that data type. A three-section format applies to positive and negative; zero uses the second section; text uses the third.

## Common Patterns

### Abbreviate large numbers

| Code | Raw value | Display |
|------|-----------|---------|
| `0,.0"K"` | 15000 | `15.0K` |
| `0,,.00"M"` | 2500000 | `2.50M` |
| `#,##0"K"` | 123456 | `123K` |

`0,.` removes three zeros (÷ 1000); `0,,.` removes six zeros (÷ 1,000,000).

### Add units

| Code | Raw value | Display |
|------|-----------|---------|
| `0"lbs"` | 42 | `42lbs` |
| `0.0" hrs"` | 3.5 | `3.5 hrs` |
| `"£"#,##0` | 1200 | `£1,200` |
| `0" units"` | 99 | `99 units` |

Units are appended as a text suffix — the cell remains numeric for calculations.

### Suppress zero display

| Code | Raw value | Display |
|------|-----------|---------|
| `0;-0;""` | 0 | *(blank)* |
| `0;-0;"-"` | 0 | `-` |
| `0;-0;"—"` | 0 | `—` |

The third section (text) handles zero values when only three sections are used.

### Color-code signs

| Code | Effect |
|------|--------|
| `[Green]#,##0;[Red]-#,##0` | Green for positive, red for negative |
| `[Blue]#,##0;[Yellow]-#,##0` | Blue positive, yellow negative |
| `0.00;[Red]-0.00` | Standard red-negative accounting |

Color codes in square brackets apply to the preceding format section.

## When to Use

- Space-constrained dashboards where full numbers don't fit
- Reports where units add context without adding a separate column
- Reducing visual noise in tables with many zero values
- Quick colour coding without conditional formatting overhead

## Custom Format vs Conditional Formatting

| | Custom Format | Conditional Formatting |
|---|---|---|
| Changes | Display only | Display only |
| Trigger | Static | React to data changes |
| Applies to | All cells matching format | Cells meeting a rule |
| Formulas | Not involved | Can use formula-based rules |
| Use when | Display is constant | Display must react to value |

Tony Phillips (HowToGeek, 2026-07-10): *"Use custom formats when you only want to change how a value looks. Use conditional formatting when you want Excel to react to changing data."*
