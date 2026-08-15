---
created: 2026-08-09
updated: 2026-08-09
source: "10 Excel Custom Number Formatting Tricks • My Online Training Hub"
note_type: atomic
tags: [excel, formatting, number-format, hide, security, temporary, visibility]
---

# Hide All Cell Values (;;;;)

`;;;;` as a custom number format hides all four value types (positive, negative, zero, text). The data remains in the cell and formula bar — formulas can still reference it. Not a security feature.

## Format

```
;;;
```

Four empty sections = nothing is displayed for any value type.

## What Gets Hidden

| Value type | Displayed |
|------------|-----------|
| Positive | blank |
| Negative | blank |
| Zero | blank |
| Text | blank |

## What Remains

- **Formula bar:** the actual cell value is visible and editable
- **Formulas:** other cells can still reference this cell's value
- **Copy/paste:** the underlying numeric value pastes normally

## Not Security

Anyone can view the value in the formula bar or by changing the format. Use worksheet protection for actual security.

## Use Cases

- Temporary hiding during work-in-progress (before sharing)
- Hiding intermediate calculation cells on a report
- Placeholder cells with data not relevant to end users

## Related

- [[Source-10-Custom-Number-Formatting-Tricks-Mynda-Treacy]] — source
- [[Four-Section-Number-Format-Structure]] — four empty sections hide all value types
