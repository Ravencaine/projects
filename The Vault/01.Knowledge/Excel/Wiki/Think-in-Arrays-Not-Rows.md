---
created: 2026-08-09
updated: 2026-08-09
source: "5 Hidden Excel Formula Rules Every Pro Follows • My Online Training Hub"
note_type: atomic
tags: [excel, formulas, arrays, dynamic-arrays, filter, sort, spill, spill-range, spill-reference]
---

# Think in Arrays, Not Rows

Modern Excel (2020+) works in arrays — one formula that spills into adjacent cells automatically. This shifts the mental model from "write a formula per row" to "write one formula that handles all rows."

## Key Concept: Spill Range

When a dynamic array formula returns multiple values, it "spills" into adjacent cells:

```
={1; 2; 3}  -- spills down into 3 rows
```

Rules:
- Can't type into the spill area → `= #SPILL!` error
- Reference the entire spilled array with `#`: `=J7#`
- Spill updates automatically when source data changes

## Example: Filter and Sort Active Employees

```
=SORT(
  FILTER(C7:F29, E7:E29="Active"),
  2,
  -1
)
```
Returns all active employees, sorted by column 2 (sales) descending, in one formula. Add an employee or change a status → result updates automatically.

## When to Use Arrays

- Filtering data based on conditions (FILTER)
- Sorting without helper columns (SORT, SORTBY)
- Combining lookups across multiple criteria (XLOOKUP with arrays)
- Dynamic lists that update when source data changes

## When NOT to Use Arrays

1. A simpler function will do (e.g. `SUMIF` instead of `SUM(FILTER(...))`)
2. Very large datasets — use Power Query or PivotTables for performance
3. When the formula becomes too complex to debug

## Related

- [[Source-5-Hidden-Excel-Formula-Rules-Mynda-Treacy]] — source
- [[LAMBDA-Custom-Functions-via-Name-Manager]] — LAMBDA can wrap array logic for reuse
