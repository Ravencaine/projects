---
created: 2026-07-31
updated: 2026-08-02
source: "🧠 Mastering Excel's Superpower FILTER, UNIQUE, SORT, and CHOOSE (a.k.a. Data Magic).md"
source_url: "https://medium.com/@markchen69/mastering-excels-superpower-filter-unique-sort-and-choose-a-k-a-data-magic-b5dbeeb02f0d"
note_type: atomic
tags: [excel, dynamic-arrays, filter]
---

# FILTER Function (Excel)

Returns a filtered array based on one or more conditions — without helper columns or VBA.

## Definition

`FILTER(array, include, [if_empty])` evaluates a condition array against a source range and returns only the rows where the condition is TRUE. The result spills into adjacent cells automatically.

## Key Points

- `include` must be a boolean array of the same row count as `array` — Excel uses row-by-row AND logic
- Multiple conditions use multiplication (`*`) for AND and addition (`+`) for OR
- `[if_empty]` defaults to error if nothing matches; set it to suppress the error
- Compatible with all dynamic array functions: `SORT()`, `UNIQUE()`, `CHOOSE()`, `LET()`
- Works in Excel 365 and Excel for the web; not available in older Excel versions

## Examples

**Single condition — exclude blanks and zeros:**
```excel
=FILTER(A2:B100, (B2:B100<>0)*(B2:B100<>""))
```

**Two conditions — AND logic:**
```excel
=FILTER(A2:C100, (B2:B100="Active")*(C2:C100>10000))
```

**Two conditions — OR logic:**
```excel
=FILTER(A2:C100, (B2:B100="Active")+(B2:B100="Pending"))
```

**Safe fallback with IFERROR:**
```excel
=IFERROR(FILTER(A2:C100, B2:B100="Active"), "No matching records")
```

**Dynamic dropdown source (excludes blanks):**
```excel
=SORT(UNIQUE(FILTER(A2:A100, A2:A100<>"")))
```

## Related

- [[sort-unique-choose-non-adjacent-columns]] — `pattern` — FILTER inside a SORT-UNIQUE-CHOOSE pipeline
- [[choose-merges-non-adjacent-columns]] — `atomic` — virtual column stacking with CHOOSE
- [[excel-data-validation]] — `pattern` — data validation patterns
