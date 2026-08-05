---
created: 2026-07-31
updated: 2026-08-02
source: "🧠 Mastering Excel's Superpower FILTER, UNIQUE, SORT, and CHOOSE (a.k.a. Data Magic).md"
source_url: "https://medium.com/@markchen69/mastering-excels-superpower-filter-unique-sort-and-choose-a-k-a-data-magic-b5dbeeb02f0d"
note_type: pattern
tags: [excel, dynamic-arrays, unique, deduplication, blanks]
---

# Remove Duplicates Ignoring Blanks

Deduplicates a column range while automatically excluding empty cells — in a single formula, no helper columns.

## Purpose

`UNIQUE()` by itself returns blank cells as distinct values, creating phantom rows in the output. This pattern wraps `UNIQUE()` with `FILTER()` to exclude blanks before deduplication, producing a clean unique list.

## Components

- `FILTER()` — removes blanks before deduplication
- `UNIQUE()` — deduplicates the filtered result

## Structure

```excel
=UNIQUE(FILTER(<range>, <range><>""))
```

## Example

Column A contains values with blanks scattered throughout:

```excel
=UNIQUE(FILTER(A2:A100, A2:A100<>""))
```

Output: a spill range of only the distinct, non-blank values.

## Variations

**Sort after deduplication:**
```excel
=SORT(UNIQUE(FILTER(A2:A100, A2:A100<>"")))
```

**Exclude zeros AND blanks:**
```excel
=UNIQUE(FILTER(A2:A100, (A2:A100<>"")*(A2:A100<>0)))
```

**Flatten two columns then deduplicate:**
```excel
=UNIQUE(FILTER(VSTACK(A2:A100, C2:C100), VSTACK(A2:A100, C2:C100)<>""))
```

## Related

- [[filter-function-excel]] — `atomic` — FILTER mechanics
- [[vstack-flatten-columns-unique]] — `pattern` — VSTACK + UNIQUE for multiple columns
- [[dynamic-dropdown-unique-sort-filter]] — `pattern` — full dropdown pattern
