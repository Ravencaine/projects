---
created: 2026-08-09
updated: 2026-08-09
source: "Advanced Conditional Formatting in Excel Using Formulas • My Online Training Hub"
note_type: atomic
tags: [excel, conditional-formatting, mixed-reference, absolute-reference, row-formatting, locked-column]
---

# Mixed References for Row Formatting

In a conditional formatting formula applied to a range, lock the column with `$` but leave the row relative. Excel evaluates each row individually, always checking the same column.

## Pattern

```
=$H2="Cancelled"
```

| Part | Meaning |
|------|---------|
| `$H` | Column H is locked — always check the Status column |
| `2` | Row is relative — increments as Excel moves down the range |

## How It Works

The formula is entered relative to the top-left cell of the selected range. When Excel evaluates row 5, it reads `=$H5="Cancelled"`. When it evaluates row 100, it reads `=$H100="Cancelled"`. The column never shifts; the row always shifts.

## Why Column Lock Is Required

Without `$`, the formula would also shift column reference when Excel moves right — useful for some layouts, but not here. Locking the column ensures the same check applies across the entire row.

## Contrast with Full Relative

A fully relative formula `=H2="Cancelled"` would shift both column and row — the check would move away from the intended column as Excel evaluates different cells.

## Related

- [[Source-Advanced-Conditional-Formatting-Formulas-Mynda-Treacy]] — source
