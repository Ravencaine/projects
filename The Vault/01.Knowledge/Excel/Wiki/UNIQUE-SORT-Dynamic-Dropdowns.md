---
created: 2026-08-09
updated: 2026-08-09
source: "Build a Dynamic Excel Report with Just 4 Formulas • My Online Training Hub"
note_type: atomic
tags: [excel, dynamic-arrays, unique, sort, dropdown, data-validation, spill, automation]
---

# UNIQUE + SORT for Dynamic Dropdowns

`=SORT(UNIQUE(table[column]))` creates a dropdown list that updates automatically when new data is added. UNIQUE extracts distinct values; SORT puts them in alphabetical order; no manual maintenance required.

## Formula

```
=SORT(UNIQUE(SalesData[Country]))
```

| Step | Function | Output |
|------|----------|--------|
| 1 | `SalesData[Country]` | All country values from the table column |
| 2 | `UNIQUE(...)` | Distinct values only (duplicates removed) |
| 3 | `SORT(...)` | Alphabetically sorted |

## How It Powers Dropdowns

1. Enter the formula in a cell (e.g. H2) — it spills its results down
2. Create a Data Validation dropdown on another cell
3. In the dropdown source, reference the first cell of the spill range with `#`: `=H2#`
4. The `#` (spill reference operator) includes the entire spilled range

When UNIQUE detects a new country in SalesData, the spill range expands, the dropdown updates — no formula changes needed.

## Replacing Manual Steps

Before: Copy column → Remove Duplicates → Sort → Copy to dropdown range
After: `=SORT(UNIQUE(SalesData[Country]))` → done

## Related

- [[Source-Dynamic-Excel-Report-4-Formulas-Mynda-Treacy]] — source
- [[Dependent-Dropdown-via-FILTER-UNIQUE-SORT]] — dependent dropdowns: categories filtered by selected country
