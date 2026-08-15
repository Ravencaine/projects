---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Drop-Down Lists in Excel • My Online Training Hub"
note_type: atomic
tags: [excel, dropdown, data-validation, table, excel-table, auto-update, same-sheet]
---

# Auto-Updating Dropdowns via Excel Table

Reference an Excel Table column directly in Data Validation's source field. When data is added to the table, the dropdown updates automatically — no manual list editing required.

## Setup

1. Create an Excel Table from the list data (Insert → Table or Ctrl+T)
2. Name the table meaningfully (e.g. DeptTable)
3. Select the input cell → Data → Data Validation → Allow: List
4. In Source, click and drag to select the table column — or type `=DeptTable[Department]`

## How It Works

Excel Tables auto-expand when new rows are added to the last row. Data Validation reads from the table's current range, so new entries appear in the dropdown immediately.

## Limitation

Works only when the table and the dropdown are on the same sheet. For cross-sheet lists, use named ranges.

## Related

- [[Source-Dynamic-Drop-Down-Lists-Mynda-Treacy]] — source
- [[Named-Ranges-TOCOL-Cross-Sheet-Dropdowns]] — cross-sheet version using named ranges
