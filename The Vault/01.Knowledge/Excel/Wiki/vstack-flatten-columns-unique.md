---
created: 2026-07-31
updated: 2026-08-02
source: "🧠 Mastering Excel's Superpower FILTER, UNIQUE, SORT, and CHOOSE (a.k.a. Data Magic).md"
source_url: "https://medium.com/@markchen69/mastering-excels-superpower-filter-unique-sort-and-choose-a-k-a-data-magic-b5dbeeb02f0d"
note_type: pattern
tags: [excel, dynamic-arrays, vstack, flatten, merge]
---

# VSTACK Flatten Columns into Unique List

Merges two or more separate column ranges into a single deduplicated list using `VSTACK` + `UNIQUE`.

## Purpose

When related data lives in disjointed columns (e.g., "Active Customers" in column A and "Archived Customers" in column C), this pattern produces a unified list of unique values from both — without copy-paste or helper columns.

## Components

- `VSTACK()` — stacks multiple arrays vertically into one
- `UNIQUE()` — deduplicates the combined array

## Structure

```excel
=UNIQUE(VSTACK(<range1>, <range2>))
```

## Example

Merge unique values from two separate columns:

```excel
=UNIQUE(VSTACK(A2:A100, C2:C100))
```

Result: a single spill range of all distinct values from both columns.

## Variations

**Three or more columns:**
```excel
=UNIQUE(VSTACK(A2:A100, C2:C100, E2:E100))
```

**Add FILTER to exclude blanks before stacking:**
```excel
=UNIQUE(VSTACK(
   FILTER(A2:A100, A2:A100<>""),
   FILTER(C2:C100, C2:C100<>"")
))
```

**Sort after flattening:**
```excel
=SORT(UNIQUE(VSTACK(A2:A100, C2:C100)))
```

## Related

- [[filter-function-excel]] — `atomic` — FILTER function mechanics
- [[sort-unique-choose-non-adjacent-columns]] — `pattern` — SORT-UNIQUE-CHOOSE for non-adjacent columns (uses CHOOSE instead of VSTACK)
- [[choose-merges-non-adjacent-columns]] — `atomic` — CHOOSE virtual array mechanism
