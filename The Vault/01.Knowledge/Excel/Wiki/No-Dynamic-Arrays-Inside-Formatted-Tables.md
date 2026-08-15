---
created: 2026-08-09
updated: 2026-08-09
source: "Build a Dynamic Excel Report with Just 4 Formulas • My Online Training Hub"
note_type: gotcha
tags: [excel, dynamic-arrays, tables, formatted-tables, limitations, spill, report-design]
---

# No Dynamic Arrays Inside Formatted Tables

Dynamic array formulas (FILTER, UNIQUE, SORT, etc.) do not work inside formatted Excel Tables. They spill outside the table structure and the two features are incompatible.

## Why

Excel Tables have their own auto-expansion behavior and structured reference system. Dynamic array formulas expect full control of their output range. The two mechanisms conflict.

## Implication

When building dynamic reports:
- Source data → Excel Table (structured references, auto-expansion)
- Report/dashboard layer → separate sheet outside tables
- Dynamic array formulas live on the report sheet, not inside the data table

## Practical Layout

| Sheet | Contains | Table/Formula |
|-------|----------|-------------|
| Data | Raw source data | Excel Table (SalesData) |
| Report | Filtered output, summaries | Dynamic array formulas (outside any table) |

## Related

- [[Source-Dynamic-Excel-Report-4-Formulas-Mynda-Treacy]] — source
- [[SPILL-Error-Cell-in-Spill-Range]] — #SPILL! from blocking cells
