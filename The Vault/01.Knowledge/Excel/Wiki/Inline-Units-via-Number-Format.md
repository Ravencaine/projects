---
created: 2026-08-09
updated: 2026-08-09
source: "10 Excel Custom Number Formatting Tricks • My Online Training Hub"
note_type: atomic
tags: [excel, formatting, number-format, units, kg, km, text, display]
---

# Inline Units via Number Format

Add display units (km, kg, hrs) directly into the number format without converting the cell to text. Value stays numeric — sortable, usable in formulas, charts unaffected.

## Format

```
0" km"      →  150" km"
0.0" kg"    →  75.5" kg"
$#,##0" hrs" →  $1,250 hrs
```

## How It Works

Text in quotes inside the format string is displayed alongside the number. The cell value is unchanged — it is still a pure number.

## Best Practice

For large datasets, put the unit in the column header instead of formatting every cell. Reduces visual noise.

## Related

- [[Source-10-Custom-Number-Formatting-Tricks-Mynda-Treacy]] — source
