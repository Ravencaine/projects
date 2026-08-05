---
created: 2026-08-01
updated: 2026-08-02
source: "Mastering Multi-Criteria Lookups in Excel with XLOOKUP and SUMPRODUCT.md"
note_type: atomic
tags: [excel, filter, lookup, multi-criteria, intermediate, dynamic-array]
---

# FILTER: Multiple Matches with Multiple Criteria

XLOOKUP returns only the first match. FILTER returns all rows that meet the criteria — no extra columns needed.

## Formula

```c
=FILTER(D2:D7, (A2:A7="Electronics") * (B2:B7="TV") * (C2:C7="South"), "Not Found")
```

- `D2:D7` — return column (the values to return)
- `(A2:A7="Electronics") * (B2:B7="TV") * (C2:C7="South")` — boolean arrays; `*` multiplies them (AND logic)
- `"Not Found"` — value if no rows match

## How the Multiplication Works

Each condition creates an array of TRUE/FALSE:

```
(A2:A7="Electronics") → {TRUE, FALSE, TRUE, FALSE, ...}
(B2:B7="TV")          → {TRUE, TRUE, FALSE, TRUE, ...}
(C2:C7="South")       → {TRUE, FALSE, FALSE, TRUE, ...}
                              ↑
                        Row 1 AND Row 2 AND Row 4 = TRUE (if all three conditions met)
```

Multiplying the arrays: `TRUE * TRUE * TRUE = 1`, any `FALSE` in a row = `0`. The result is a 1/0 array used as a filter mask.

## Dynamic Criteria with Cell References

Replace hard-coded values with cell references:

```c
=FILTER(D2:D7, (A2:A7=F1) * (B2:B7=F2) * (C2:C7=F3), "Not Found")
```

## Returning Multiple Columns

FILTER can return more than one column — specify the columns as a range:

```c
=FILTER(A2:D7, (B2:B7="TV") * (C2:C7="South"))
```

Returns all rows (all columns) where the product is TV and the region is South.

## Notes

- Requires Excel 365 or Excel 2021+ (dynamic array support)
- Spills results into adjacent cells automatically
- If no matches: returns "Not Found" (or any custom message)

## Related

- [[xlookup-multi-criteria-concatenation]] — single-match alternative
- [[sumproduct-multi-criteria-summing]] — conditional summing instead of row-by-row results
