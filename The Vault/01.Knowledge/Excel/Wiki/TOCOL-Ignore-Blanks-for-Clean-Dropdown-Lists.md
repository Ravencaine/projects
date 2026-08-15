---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Drop-Down Lists in Excel • My Online Training Hub"
note_type: atomic
tags: [excel, tocol, ignore-blanks, dynamic-arrays, stack, spill, dropdown, blanks]
---

# TOCOL with Ignore Blanks for Clean Dropdown Lists

`TOCOL(source, 1)` stacks a range into a single column and ignores blank cells. The second argument `1` = scan mode: ignore blanks. Essential for building clean dropdown lists from ranges that contain empty rows.

## TOCOL Arguments

```
=TOCOL(array, scan_mode, [ignore_blanks])
```

| scan_mode | Behavior |
|-----------|----------|
| 1 | Scan by column (default) |
| 2 | Scan by row |
| 3 | Scan by column, wrap to next column after reaching height |
| 4 | Scan by row, wrap to next row after reaching width |

| ignore_blanks | Behavior |
|---------------|----------|
| Omitted | Treat blanks as zero or error |
| 1 | Ignore blanks — critical for dropdowns |

## Use Case

```
=SORT(UNIQUE(TOCOL(DeptTable[Department], 1)))
```

If `DeptTable` has 10 rows but 2 are blank, `TOCOL(..., 1)` returns 8 values (not 10 with 2 blanks). Without `1`, the formula produces empty entries in the dropdown.

## Why It Matters for Dropdowns

Blank entries in a dropdown source cause empty rows to appear in the selection list. Using `TOCOL(..., 1)` eliminates them.

## Related

- [[Source-Dynamic-Drop-Down-Lists-Mynda-Treacy]] — source
- [[Named-Ranges-TOCOL-Cross-Sheet-Dropdowns]] — practical use of TOCOL for cross-sheet dropdowns
