---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Drop-Down Lists in Excel • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/dynamic-drop-down-lists-in-excel"
published: 2025-10-28
note_type: source
tags: [excel, dropdown, data-validation, dynamic-arrays, tables, named-ranges, dependent-dropdown, xlookup, filter, unique]
---

# Dynamic Drop-Down Lists in Excel — My Online Training Hub / Mynda Treacy

Source: My Online Training Hub. Published 2025-10-28. Author: Mynda Treacy — already in vault (8th source).

## Summary

Five dynamic drop-down list methods that update automatically, filter by category, and pull related data. Methods 1-2 are static lists (auto-update via table or named range). Methods 3-5 are dynamic (cascading, auto-fill, exclusion). Plus TOCOL for blank handling and search-as-you-type in modern Excel.

## The Five Methods

| # | Method | Technique | Use Case |
|----|--------|-----------|----------|
| 1 | Table-based | Table column in DV source | Auto-updates; same sheet only |
| 2 | Named range | Define Name → DV source | Cross-sheet auto-updating list |
| 3 | Cascading | SORT + FILTER → XLOOKUP | Category drives sub-category |
| 4 | Auto-fill related | XLOOKUP → Employee data | Dropdown populates multiple fields |
| 5 | Exclude items | FILTER + UNIQUE + SORT | Only Active products, no Discontinued |

## Key Formula Patterns

| Pattern | Formula |
|---------|---------|
| Clean list (no blanks, no dupes) | `=SORT(UNIQUE(TOCOL(DeptTable[Department],1)))` |
| Cascading product list | `=SORT(FILTER(ProductsTbl[Product], ProductsTbl[Category]=D6))` |
| Auto-fill department | `=XLOOKUP([@[Employee]], EmpTbl[Employee], EmpTbl[Dept], "")` |
| Exclude discontinued | `=SORT(UNIQUE(FILTER(ProductsTbl[Product], ProductsTbl[Status]="Active", "")))` |

## Key Insights Extracted

- [[Auto-Updating-Dropdowns-via-Excel-Table]] — `atomic` — table column as DV source; auto-expands when data added; same-sheet only
- [[Named-Ranges-TOCOL-Cross-Sheet-Dropdowns]] — `atomic` — Define Name + TOCOL; TOCOL(...,1) ignores blanks; cross-sheet
- [[Cascading-Dropdowns-SORT-FILTER-XLOOKUP]] — `pattern` — SORT(FILTER(products, category=D6)); XLOOKUP spills to DV; dependent dropdown; cross-references [[Dependent-Dropdown-via-FILTER-UNIQUE-SORT]]
- [[XLOOKUP-AutoFill-Related-Data-from-Dropdown]] — `atomic` — XLOOKUP from dropdown value populates multiple related fields (Dept, Rate); interactive form pattern
- [[FILTER-UNIQUE-SORT-Excluding-Dropdown-Items]] — `atomic` — FILTER excludes by condition (Status="Active"); UNIQUE removes dupes; SORT orders; always current list
- [[TOCOL-Ignore-Blanks-for-Clean-Dropdown-Lists]] — `atomic` — TOCOL(range, 1) ignores blanks; 1 = skip blanks; prevents empty entries in dropdowns
- [[Search-as-You-Type-in-Modern-Excel-Dropdowns]] — `atomic` — built-in in newer Excel versions; filters dropdown list as user types; no formula needed

## Author

- [[Author-Mynda-Treacy]] — extended (8th source)
