---
created: 2026-07-31
updated: 2026-08-02
source: "Sorting Non - Adjacent Column Pairs in Excel.md"
note_type: pattern
tags: [excel, dynamic-arrays, sorting, deduplication, arrays]
---

# SORT-UNIQUE-CHOOSE for Non-Adjacent Column Pairs

Deduplicate and alphabetically sort pairs of non-adjacent columns in a single formula — without helper columns or moving source data.

## Purpose

When two related columns (e.g., Account Type in column A, Ledger Account in column C) exist far apart in a table, you often want a clean, sorted, deduplicated list of unique pairs. Traditional approaches require copying/moving columns. This pattern avoids that entirely.

## Components

- `CHOOSE({1,2}, range1, range2)` — merges two non-adjacent columns into a virtual 2-column array
- `UNIQUE(array)` — deduplicates rows in the array
- `SORT(array, sort_keys, sort_orders)` — sorts by specified columns

## Structure

```excel
=SORT(UNIQUE(CHOOSE({1,2}, <col1>, <col2>)), {1,2}, {TRUE,TRUE})
```

Parameters:
- `{1,2}` — sort first by column 1, then by column 2
- `{TRUE,TRUE}` — both columns in ascending order

## Example

Columns A and C contain Account Type and Ledger Account respectively (rows 2–100):

```excel
=SORT(UNIQUE(CHOOSE({1,2}, A2:A100, C2:C100)), {1,2}, {TRUE,TRUE})
```

Result: a spill range with all unique Account Type + Ledger Account pairs, sorted A→Z by Account Type, then A→Z by Ledger Account.

## Variations

**Sort descending on second column only:**
```excel
=SORT(UNIQUE(CHOOSE({1,2}, A2:A100, C2:C100)), {1,2}, {TRUE,FALSE})
```

**Performance-optimized with LET:**
```excel
=LET(
  data, CHOOSE({1,2}, A2:A100, C2:C100),
  SORT(UNIQUE(data), {1,2}, {TRUE,TRUE})
)
```

**Three non-adjacent columns:**
```excel
=SORT(UNIQUE(CHOOSE({1,2,3}, A2:A100, C2:C100, E2:E100)), {1,2,3}, {TRUE,TRUE,TRUE})
```

## Related

- [[choose-merges-non-adjacent-columns]] — `atomic` — the mechanism that makes this pattern work
- [[pivot-tables]] — `function` — alternative aggregation approach
- [[excel-data-validation]] — `pattern` — data validation patterns
