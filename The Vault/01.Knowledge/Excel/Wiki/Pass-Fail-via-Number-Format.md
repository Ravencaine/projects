---
created: 2026-08-09
updated: 2026-08-09
source: "10 Excel Custom Number Formatting Tricks • My Online Training Hub"
note_type: atomic
tags: [excel, formatting, number-format, pass-fail, text, if-formula, display]
---

# Pass/Fail via Number Format

Replace numeric values with text labels (Pass/Fail) via custom format — without an IF formula. Underlying value stays numeric and usable in formulas and charts.

## Format

```
[Blue][>=0.5]"Pass";[Red][<0.5]"Fail"
```

- `[Blue][>=0.5]"Pass"` — blue text + "Pass" label when value ≥ 0.5
- `[Red][<0.5]"Fail"` — red text + "Fail" label when value < 0.5

## Why No IF Needed

The condition `[>=0.5]` lives inside the format string. Excel evaluates the condition per section. The cell keeps its numeric value — no IF, no helper column, no text conversion.

## General Pattern

```
[color][condition]"True text";"False text"
```

Use any numeric condition in square brackets before the display text.

## Related

- [[Source-10-Custom-Number-Formatting-Tricks-Mynda-Treacy]] — source
- [[Four-Section-Number-Format-Structure]] — condition syntax sits inside each section
