---
created: 2026-08-09
updated: 2026-08-09
source: "Advanced Conditional Formatting in Excel Using Formulas • My Online Training Hub"
note_type: atomic
tags: [excel, conditional-formatting, subtotal, mod, filter, banding, visible-rows, alternate-row]
---

# MOD(SUBTOTAL(3,...),2) for Filter-Aware Banding

`=MOD(SUBTOTAL(3,$C$5:$C5),2)` creates alternating row banding that respects filters. SUBTOTAL(3,...) counts only visible rows; MOD alternates between 0 and 1; hidden rows are skipped in the count.

## Formula

```
=MOD(SUBTOTAL(3,$C$5:$C5),2)
```

## How It Works

| Component | Value |
|-----------|-------|
| `SUBTOTAL(3, range)` | COUNTA of visible rows only (ignores filtered-out rows) |
| `MOD(result, 2)` | Alternates between 0 and 1 as visible row count increases |
| CF applies format when result = 0 (or 1, depending on which band you want) | Alternating bands on visible rows only |

`SUBTOTAL` with function number 3 (COUNTA) ignores rows hidden by filter. Only the visible row count increases, so MOD's alternation stays synchronized with what the user can see.

## Why Not Standard Table Banding

Excel Tables offer banded rows but don't work well with dynamic arrays. The CF approach is filter-aware, array-compatible, and fully controllable.

## Lock Pattern

```
$C$5:$C5
^^^^  ^^^
 |    └── Relative row — expands as Excel moves down
 └── Fixed start — always the first data row
```

Same expanding range pattern as COUNTIF duplicate detection.

## Related

- [[Source-Advanced-Conditional-Formatting-Formulas-Mynda-Treacy]] — source
