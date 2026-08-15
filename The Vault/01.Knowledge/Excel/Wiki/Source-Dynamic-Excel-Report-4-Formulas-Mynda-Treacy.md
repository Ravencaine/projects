---
created: 2026-08-09
updated: 2026-08-09
source: "Build a Dynamic Excel Report with Just 4 Formulas • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/build-a-dynamic-excel-report-with-just-4-formulas"
published: 2026-05-05
note_type: source
tags: [excel, dynamic-arrays, filter, unique, sort, groupby, take, choosecols, report, automation, dropdowns]
---

# Build a Dynamic Excel Report with Just 4 Formulas — My Online Training Hub / Mynda Treacy

Source: My Online Training Hub. Published 2026-05-05. Author: Mynda Treacy — already in vault (6th source).

## Summary

Four core dynamic array functions (UNIQUE, SORT, FILTER, GROUPBY) drive a self-updating report. No PivotTables, no macros. Steps: Excel Table → dynamic dropdown lists → FILTER data → GROUPBY summary. Plus dependent dropdowns, #SPILL! gotchas, and version requirements.

## The Four Core Functions

| # | Function | Role |
|----|----------|------|
| 1 | `UNIQUE` | Extracts distinct values from a column |
| 2 | `SORT` | Sorts the result alphabetically |
| 3 | `FILTER` | Returns only rows matching criteria |
| 4 | `GROUPBY` | Aggregates data by category (Excel 365/2024+) |

## Key Formula Patterns

| Pattern | Formula |
|---------|---------|
| Country dropdown list | `=SORT(UNIQUE(SalesData[Country]))` |
| Category dropdown list | `=SORT(UNIQUE(SalesData[Category]))` |
| Filter by two criteria | `=FILTER(SalesData, (Country=D4)*(Category=D5), "No results")` |
| Dependent category dropdown | `=SORT(UNIQUE(FILTER(SalesData[Category], SalesData[Country]=D4)))` |
| Top salesperson | `=IFERROR(TAKE(GROUPBY(CHOOSECOLS(C8#,7), CHOOSECOLS(C8#,8,10), SUM, 0, 0, -3), 1), "")` |

## Key Insight

Boolean multiplication (`*`) = AND logic; Boolean addition (`+`) = OR logic. Used inside FILTER conditions to combine criteria.

## Key Insights Extracted

- [[UNIQUE-SORT-Dynamic-Dropdowns]] — `atomic` — `=SORT(UNIQUE(table[column]))`; replaces manual copy/remove-duplicates/sort
- [[FILTER-Boolean-AND-OR-Logic]] — `pattern` — `(cond1)*(cond2)` = AND; `(cond1)+(cond2)` = OR; works in FILTER and other dynamic array functions
- [[Dependent-Dropdown-via-FILTER-UNIQUE-SORT]] — `atomic` — nested FILTER inside UNIQUE → category list updates based on country selection
- [[GROUPBY-CHOOSECOLS-TAKE-Top-N-Summary]] — `pattern` — GROUPBY aggregates by key; CHOOSECOLS selects columns; TAKE limits to top N; -3 = sort descending by 3rd agg column
- [[SPILL-Error-Cell-in-Spill-Range]] — `gotcha` — #SPILL! when something blocks the spill range; fix: clear blocking cells
- [[No-Dynamic-Arrays-Inside-Formatted-Tables]] — `gotcha` — dynamic array formulas do not work inside Excel Tables; keep spill outputs outside tables
- [[Excel-365-Version-Requirements-Dynamic-Functions]] — `atomic` — FILTER = Excel 365/2021+; GROUPBY/TAKE/CHOOSECOLS = Excel 365/2024+

## Author

- [[Author-Mynda-Treacy]] — extended (6th source)
