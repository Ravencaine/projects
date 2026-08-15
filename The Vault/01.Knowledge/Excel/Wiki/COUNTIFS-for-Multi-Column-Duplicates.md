---
created: 2026-08-09
updated: 2026-08-09
source: "Advanced Conditional Formatting in Excel Using Formulas • My Online Training Hub"
note_type: atomic
tags: [excel, conditional-formatting, countifs, duplicate, multi-column, composite-key, exact-match]
---

# COUNTIFS for Multi-Column Duplicates

`=COUNTIFS($E$5:$E5,$E5,$G$5:$G5,$G5)>1` detects duplicates based on a combination of columns — flagging only rows where both email and session match a prior row.

## Formula

```
=COUNTIFS($E$5:$E5, $E5, $G$5:$G5, $G5)>1
```

## How It Works

Both ranges expand as Excel evaluates downward (same expanding range technique as COUNTIF for single-column duplicates):

| Row | Range E | Range G | Evaluates |
|-----|---------|---------|-----------|
| 5 | `$E$5:$E5` | `$G$5:$G5` | First row — count always 1 → no format |
| 6 | `$E$5:$E6` | `$G$5:$G6` | If E6+G6 match any prior row → count > 1 → format |
| 7 | `$E$5:$E7` | `$G$5:$G7` | Same logic |

Both conditions must be satisfied simultaneously — composite key for exact duplicates.

## Use Cases

- Email + date duplicates (same person, same session)
- Product + region duplicates (same item, same territory)
- Invoice + line number duplicates (same document reference)

## Hierarchy Effect

Combine with the single-column COUNTIF rule for partial duplicates: exact matches (COUNTIFS) get a stronger format, partial matches (COUNTIF) get a lighter format.

## Related

- [[Source-Advanced-Conditional-Formatting-Formulas-Mynda-Treacy]] — source
- [[COUNTIF-Expanding-Range-for-Duplicates]] — single-column version
