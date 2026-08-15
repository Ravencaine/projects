---
created: 2026-08-09
updated: 2026-08-09
source: "Build a Dynamic Excel Report with Just 4 Formulas • My Online Training Hub"
note_type: atomic
tags: [excel, excel-365, version, dynamic-arrays, groupby, take, choosecols, filter, sort, unique, compatibility]
---

# Excel 365 Version Requirements for Dynamic Functions

Dynamic array functions are not available in all Excel versions. FILTER arrived in Excel 365/2021+. GROUPBY, TAKE, and CHOOSECOLS require Excel 365/2024+.

## Version Requirements

| Function | Minimum Excel Version |
|----------|----------------------|
| `UNIQUE` | Excel 365 / Excel 2021+ |
| `SORT` | Excel 365 / Excel 2021+ |
| `FILTER` | Excel 365 / Excel 2021+ |
| `GROUPBY` | Excel 365 / Excel 2024+ |
| `TAKE` | Excel 365 / Excel 2024+ |
| `CHOOSECOLS` | Excel 365 / Excel 2024+ |

## How to Check

1. Type `=FunctionName(` in a cell
2. If the function name appears in IntelliSense autocomplete, it is available
3. If not recognized, the version does not support it

## Progressive Enhancement Pattern

Build reports that work with FILTER as the minimum (Excel 365/2021+), then add GROUPBY/TAKE/CHOOSECOLS for Excel 365/2024+ as a layer on top.

## Related

- [[Source-Dynamic-Excel-Report-4-Formulas-Mynda-Treacy]] — source
- [[GROUPBY-CHOOSECOLS-TAKE-Top-N-Summary]] — requires Excel 365/2024+
