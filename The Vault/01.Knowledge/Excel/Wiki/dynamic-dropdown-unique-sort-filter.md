---
created: 2026-07-31
updated: 2026-08-02
source: "🧠 Mastering Excel's Superpower FILTER, UNIQUE, SORT, and CHOOSE (a.k.a. Data Magic).md"
source_url: "https://medium.com/@markchen69/mastering-excels-superpower-filter-unique-sort-and-choose-a-k-a-data-magic-b5dbeeb02f0d"
note_type: pattern
tags: [excel, dynamic-arrays, data-validation, dropdown]
---

# Dynamic Dropdown with UNIQUE + SORT + FILTER

Creates a sorted, deduplicated, blank-free dropdown list from a source column using only array formulas — no helper columns or named ranges required.

## Purpose

Data Validation dropdowns in Excel typically require a static named range or helper column. This pattern generates the dropdown source dynamically so the list updates automatically as source data changes.

## Components

- `FILTER()` — strips blanks and any other unwanted values
- `UNIQUE()` — deduplicates the result
- `SORT()` — sorts alphabetically (or by a custom key)
- Data Validation → List → formula reference

## Structure

```excel
=SORT(UNIQUE(FILTER(<source_range>, <source_range><>"")))
```

## Example

Source data in A2:A100 (with possible blanks):

```excel
=SORT(UNIQUE(FILTER(A2:A100, A2:A100<>"")))
```

Enter this as the Data Validation List source:
1. Select the target cell → Data → Data Validation
2. Allow: List
3. Source: `=SORT(UNIQUE(FILTER(A2:A100, A2:A100<>"")))`

The dropdown updates automatically when the source data changes.

## Variations

**Case-insensitive sort (Excel sorts by internal Unicode order — this is default behaviour):**
Not needed — UNIQUE and SORT are already case-insensitive in Excel 365.

**Add a default "Select..." placeholder at the top:**
Not directly possible in a single formula. Workaround: use `VSTACK({"Select..."}, SORT(...))` in a helper cell and point the validation at that cell instead.

**Sort descending:**
```excel
=SORT(UNIQUE(FILTER(A2:A100, A2:A100<>"")),,FALSE)
```

## Related

- [[filter-function-excel]] — `atomic` — FILTER function mechanics
- [[sort-unique-choose-non-adjacent-columns]] — `pattern` — more complex SORT-UNIQUE-CHOOSE pipeline
- [[excel-data-validation]] — `pattern` — data validation patterns
