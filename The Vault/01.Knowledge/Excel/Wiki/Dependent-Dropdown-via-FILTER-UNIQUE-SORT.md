---
created: 2026-08-09
updated: 2026-08-09
source: "Build a Dynamic Excel Report with Just 4 Formulas • My Online Training Hub"
note_type: atomic
tags: [excel, dynamic-arrays, filter, unique, sort, dependent-dropdown, cascading, automation]
---

# Dependent Dropdown via FILTER → UNIQUE → SORT

A dependent dropdown shows only the options relevant to the current selection in another dropdown. Achieved by nesting FILTER inside UNIQUE → SORT: `=SORT(UNIQUE(FILTER(table[Column], table[OtherColumn]=SelectedCell)))`.

## Pattern

```
=SORT(UNIQUE(FILTER(SalesData[Category], SalesData[Country]=D4)))
```

| Step | Expression | Output |
|------|-----------|--------|
| 1 | `SalesData[Country]=D4` | TRUE/FALSE array for each row |
| 2 | `FILTER(SalesData[Category], ...)` | Only categories matching the country |
| 3 | `UNIQUE(...)` | Distinct categories |
| 4 | `SORT(...)` | Alphabetically sorted |

## How It Works

When D4 = "Japan", FILTER returns only the categories sold in Japan. UNIQUE removes any duplicates. SORT puts them in order. The dropdown updates when the country selection changes.

## Result

- Selecting Japan → dropdown shows only Japan-relevant categories
- Selecting Germany → dropdown shows only Germany-relevant categories
- No categories appear that don't exist for the selected country

## Related

- [[Source-Dynamic-Excel-Report-4-Formulas-Mynda-Treacy]] — source
- [[UNIQUE-SORT-Dynamic-Dropdowns]] — standalone dynamic dropdown
- [[FILTER-Boolean-AND-OR-Logic]] — FILTER's boolean logic that powers the dependent filtering
