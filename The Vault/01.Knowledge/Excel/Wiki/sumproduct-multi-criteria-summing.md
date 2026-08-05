---
created: 2026-08-01
updated: 2026-08-02
source: "Mastering Multi-Criteria Lookups in Excel with XLOOKUP and SUMPRODUCT.md"
note_type: atomic
tags: [excel, sumproduct, lookup, multi-criteria, summing, intermediate]
---

# SUMPRODUCT: Multi-Criteria Conditional Summing

SUMPRODUCT multiplies boolean arrays by values — useful for summing all rows that meet multiple criteria, without needing an array formula (Ctrl+Shift+Enter).

## Formula

```c
=SUMPRODUCT((A2:A7="Electronics") * (B2:B7="TV") * (C2:C7="South") * D2:D7)
```

## How It Works

Each condition `(A2:A7="Electronics")` etc. produces a TRUE/FALSE array. Excel treats TRUE as `1` and FALSE as `0`.

Multiplying all conditions together with `*` gives `1` only when every condition is met.

```
Condition arrays:  {1,0,1,0,...} × {1,1,0,1,...} × {1,0,0,1,...} × {300,400,200,500,...}
                            ↓
                 {1×1×1×300, 0×...×400, 1×0×0×200, ...}
                 = {300, 0, 0, 0, ...}
```

SUMPRODUCT sums the resulting array: `300`.

## With Cell References

```c
=SUMPRODUCT((A2:A7=F1) * (B2:B7=F2) * (C2:B7=F3) * D2:D7)
```

## SUMPRODUCT vs SUMIF / SUMIFS

| Function | Criteria | Returns |
|----------|----------|---------|
| SUMIF | One column, one condition | Sum of matches |
| SUMIFS | Multiple columns, multiple conditions | Sum of matches |
| SUMPRODUCT | Any number of conditions, any logic | Sum of matches |

SUMPRODUCT is more flexible than SUMIFS because any condition can be multiplied together (AND logic). For OR logic, add the arrays instead of multiplying.

## Key Advantage

- No Ctrl+Shift+Enter needed — SUMPRODUCT handles arrays natively
- Works in all modern Excel versions (365, 2021, 2019)
- More readable than array formulas for complex conditions

## Related

- [[xlookup-multi-criteria-concatenation]] — returning a single lookup value
- [[filter-function-multi-match]] — returning all matching rows instead of summed total
