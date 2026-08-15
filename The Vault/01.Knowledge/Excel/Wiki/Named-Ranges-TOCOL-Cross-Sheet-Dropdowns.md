---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Drop-Down Lists in Excel • My Online Training Hub"
note_type: atomic
tags: [excel, dropdown, data-validation, named-ranges, tocol, cross-sheet, define-name, dynamic-arrays]
---

# Named Ranges + TOCOL for Cross-Sheet Dropdowns

`=SORT(UNIQUE(TOCOL(DeptTable[Department],1)))` — Define Name creates a named range from a spill formula, enabling cross-sheet dynamic dropdowns. TOCOL(...,1) ignores blank cells in the source.

## Formula

```
=SORT(UNIQUE(TOCOL(DepartmentTable[Department],1)))
```

| Step | Expression | Output |
|------|-----------|--------|
| 1 | `DepartmentTable[Department]` | All values from table column |
| 2 | `TOCOL(..., 1)` | Stack into single column; 1 = ignore blanks |
| 3 | `UNIQUE(...)` | Distinct values only |
| 4 | `SORT(...)` | Alphabetically sorted |

## How to Use

1. Define a name: Formulas → Define Name → Name: `DepartmentList`
2. In Source, enter `=DepartmentList`
3. Data Validation dropdown uses the named range

## Cross-Sheet Capability

Unlike a direct table reference (same-sheet only), a named range points to a formula that evaluates on any sheet. The list can live on a separate hidden sheet.

## TOCOL(..., 1) — Ignore Blanks

The second argument `1` tells TOCOL to skip blank cells. Without it, blank rows in the source table produce empty entries in the dropdown.

## Related

- [[Source-Dynamic-Drop-Down-Lists-Mynda-Treacy]] — source
- [[Auto-Updating-Dropdowns-via-Excel-Table]] — same-sheet alternative
- [[TOCOL-Ignore-Blanks-for-Clean-Dropdown-Lists]] — dedicated TOCOL blank-skipping note
