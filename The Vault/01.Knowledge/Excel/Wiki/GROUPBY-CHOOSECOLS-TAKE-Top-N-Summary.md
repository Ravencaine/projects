---
created: 2026-08-09
updated: 2026-08-09
source: "Build a Dynamic Excel Report with Just 4 Formulas • My Online Training Hub"
note_type: pattern
tags: [excel, dynamic-arrays, groupby, choosecols, take, aggregation, top-n, sort-descending, summary]
---

# GROUPBY + CHOOSECOLS + TAKE for Top-N Summary

`GROUPBY` aggregates data by a key column; `CHOOSECOLS` selects which columns to use; `TAKE` limits the result to the top N rows; a negative sort index (e.g. `-3`) sorts the aggregation result in descending order.

## Formula

```
=IFERROR(
  TAKE(
    GROUPBY(
      CHOOSECOLS(C8#, 7),
      CHOOSECOLS(C8#, 8, 10),
      SUM,
      0,   -- field_index_num_headers
      0,   -- relationship
      -3   -- sort_index = descending by 3rd aggregation column
    ),
    1  -- TAKE: return only the top row
  ),
"")
```

## How Each Function Contributes

| Function | Role |
|----------|------|
| `C8#` | The spilled FILTER output (the report data) |
| `CHOOSECOLS(C8#, 7)` | Key column: salesperson name (column 7 of the FILTER output) |
| `CHOOSECOLS(C8#, 8, 10)` | Aggregation columns: units and revenue (columns 8 and 10) |
| `SUM` | Aggregation function |
| `-3` | Sort by the 3rd column of the aggregation result (revenue) in descending order |
| `TAKE(..., 1)` | Return only the top row (top performer) |
| `IFERROR(...)` | Handle empty FILTER result (no matching data) |

## The Sort Index

The 6th argument of GROUPBY controls sort order:
- Positive = ascending
- Negative = descending
- `-3` = descending by the 3rd aggregation column (revenue in this case)

## Related

- [[Source-Dynamic-Excel-Report-4-Formulas-Mynda-Treacy]] — source
- [[FILTER-Boolean-AND-OR-Logic]] — FILTER produces the input data (C8#) for GROUPBY
