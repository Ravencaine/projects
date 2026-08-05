---
created: 2026-08-01
updated: 2026-08-02
source: "Mastering Multi-Criteria Lookups in Excel with XLOOKUP and SUMPRODUCT.md"
note_type: atomic
tags: [excel, xlookup, lookup, multi-criteria, intermediate, concatenation]
---

# XLOOKUP Multi-Criteria via Concatenation

XLOOKUP was designed for single-criterion lookups. To use it with multiple criteria, concatenate all criteria into one string and concatenate all search columns the same way.

## The Technique

Combine each criterion into a single string with `&`, and do the same to the search columns:

```c
=XLOOKUP(F1 & F2 & F3, A2:A7 & B2:B7 & C2:C7, D2:D7)
```

- `F1 & F2 & F3` — cell references containing criteria (e.g. "Electronics", "TV", "South")
- `A2:A7 & B2:B7 & C2:C7` — concatenation of all three search columns produces one combined value per row
- `D2:D7` — return column

The result: `"ElectronicsTVSouth"` matched against each row's combined value.

## With Hard-Coded Criteria

```c
=XLOOKUP("Electronics" & "TV" & "South", A2:A7 & B2:B7 & C2:C7, D2:D7)
```

Returns `300` — the sales for Electronics / TV / South.

## Why This Works

- Each row's three columns are concatenated: `"ElectronicsTVSouth"` in row 1, `"ClothingT-ShirtNorth"` in row 2, etc.
- XLOOKUP searches for the exact combined string in that array
- Returns the corresponding value from `D2:D7`

## Dynamic Version (Recommended)

Replace hard-coded strings with cell references so the formula adapts:

```c
=XLOOKUP(F1 & F2 & F3, A2:A7 & B2:B7 & C2:C7, D2:D7)
```

Change F1, F2, or F3 — the lookup updates automatically.

## Limitations

- All concatenated values must match exactly (case-sensitive in some contexts)
- Performance degrades with very large ranges
- Returns only the first match — use FILTER if multiple matches are needed

## Related

- [[filter-function-multi-match]] — return all matching rows instead of just the first
- [[sumproduct-multi-criteria-summing]] — sum all matching values rather than returning individual rows
