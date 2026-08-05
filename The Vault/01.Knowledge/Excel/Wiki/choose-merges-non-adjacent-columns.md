---
created: 2026-07-31
updated: 2026-08-02
source: "Sorting Non - Adjacent Column Pairs in Excel.md"
note_type: atomic
tags: [excel, dynamic-arrays, arrays, choose]
---

# CHOOSE Merges Non-Adjacent Columns into a Virtual Array

`CHOOSE({1,2}, range1, range2)` stacks two non-adjacent columns into a virtual 2D array that dynamic array functions can process as a single unit.

## Definition

`CHOOSE(index_num, value1, [value2], ...)` normally returns a single value from a list. When given an array constant `{1,2}` as the index, it returns all referenced values simultaneously — producing a 2-column spill array from two separate ranges.

This allows non-adjacent columns to participate in `UNIQUE()`, `SORT()`, `FILTER()`, and other dynamic array functions without being physically moved.

## Key Points

- `CHOOSE({1,2}, A2:A100, C2:C100)` → virtual 2-column array
- Works with 3+ columns: `CHOOSE({1,2,3}, col1, col2, col3)`
- The column order in the array follows the `{1,2,...}` index order, not the sheet column order
- Compatible with `UNIQUE()`, `SORT()`, `FILTER()`, and any other dynamic array function
- Works in Power BI as well (same function signatures)

## Examples

**Two non-adjacent columns as a pair:**
```excel
=CHOOSE({1,2}, A2:A100, C2:C100)
```

**Three columns:**
```excel
=CHOOSE({1,2,3}, A2:A100, D2:D100, G2:G100)
```

**Combined with FILTER to get unique pairs matching a condition:**
```excel
=UNIQUE(CHOOSE({1,2}, FILTER(A2:A100, B2:B100="Sales"), FILTER(C2:C100, B2:B100="Sales")))
```

## Related

- [[sort-unique-choose-non-adjacent-columns]] — `pattern` — the full formula that uses this mechanism
