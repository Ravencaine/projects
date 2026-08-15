---
created: 2026-08-09
updated: 2026-08-09
source: "Advanced Conditional Formatting in Excel Using Formulas • My Online Training Hub"
note_type: atomic
tags: [excel, conditional-formatting, countif, duplicate, expanding-range, relative-reference, first-occurrence]
---

# COUNTIF Expanding Range for Duplicates

`=COUNTIF($E$5:$E5,$E5)>1` flags duplicate entries while leaving the first occurrence clean. The expanding range (`$E$5:$E5`) grows as CF evaluates downward — the top is locked, the bottom is relative.

## Formula

```
=COUNTIF($E$5:$E5,$E5)>1
```

## How It Works

| Row evaluated | COUNTIF range | Counts within |
|---------------|---------------|---------------|
| Row 5 | `$E$5:$E5` (1 row) | Row 5 itself → count = 1 → no format |
| Row 6 | `$E$5:$E6` (2 rows) | If row 6 value already appears in row 5 → count = 2 → format |
| Row 7 | `$E$5:$E7` (3 rows) | If row 7 value appears in rows 5-6 → count ≥ 2 → format |

The first occurrence always has a range of one row → count = 1 → condition is FALSE → no formatting. Duplicates (count ≥ 2) get formatted.

## Lock Pattern

```
$E$5:$E5
 ^^^  ^^^
 |    └── Relative row (bottom) — shifts as Excel moves down
 └── Fixed row (top) — always the first data row
```

## Why Not `>0`

`>0` would flag the first occurrence (count = 1 → TRUE). Use `>1` to highlight only duplicates.

## Related

- [[Source-Advanced-Conditional-Formatting-Formulas-Mynda-Treacy]] — source
- [[COUNTIFS-for-Multi-Column-Duplicates]] — multi-column duplicate detection
