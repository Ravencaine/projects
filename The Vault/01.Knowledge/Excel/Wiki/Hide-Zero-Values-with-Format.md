---
created: 2026-08-09
updated: 2026-08-09
source: "10 Excel Custom Number Formatting Tricks • My Online Training Hub"
note_type: atomic
tags: [excel, formatting, number-format, zero, hide, clutter, display]
---

# Hide Zero Values with Format

Hide zeros in a range by leaving the third (zero) section of the format string empty. Zeros are hidden from display but the cell retains its numeric value — formulas and PivotTables continue to use the real value.

## Format

```
#,##0;-#,##0;
```

The trailing semicolon with no third section = zeros are not displayed.

## Effect

| Cell value | Displayed as |
|------------|-------------|
| 1250 | 1,250 |
| -380 | -380 |
| 0 | *(blank)* |

## Use When

- Reports with sparse data where zeros add clutter
- KPI or scorecard tables where 0 means "no activity"
- Dashboards where zero is the default and non-zero values carry the meaning

## Note

The zero value is hidden, not removed. The cell still equals 0. Use in formulas, SUM, PivotTables — they see the real number.

## Related

- [[Source-10-Custom-Number-Formatting-Tricks-Mynda-Treacy]] — source
- [[Four-Section-Number-Format-Structure]] — empty third section = no display for zeros
