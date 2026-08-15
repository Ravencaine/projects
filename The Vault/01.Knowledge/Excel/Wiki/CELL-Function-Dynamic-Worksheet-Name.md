---
created: 2026-08-09
updated: 2026-08-09
source: "5 Boring Excel Functions That Are Secretly Brilliant • My Online Training Hub"
note_type: atomic
tags: [excel, functions, cell, worksheet-name, dynamic, filename, info-function]
---

# CELL: Dynamic Worksheet Name from File Path

`CELL(info_type, reference)` is an information function — it returns metadata about a cell rather than performing calculations. The key practical use: extracting the current worksheet name from the workbook's full file path, so the sheet tab name can drive a dynamic report title.

## Syntax

```
=CELL(info_type, reference)
```

Common `info_type` values:
| info_type | Returns |
|-----------|---------|
| `"address"` | Absolute cell reference (e.g. `$F$4`) |
| `"type"` | `v` (value), `l` (label), `b` (blank) |
| `"contents"` | Cell's raw contents |

## Key Application: Dynamic Worksheet Name

```
=MID(
  CELL("filename", A1),
  FIND("]", CELL("filename", A1)) + 1,
  31
)
```

Breaking it down:
1. `CELL("filename", A1)` returns the full path: `C:\Reports\[July 2026.xlsx]Sheet1`
2. `FIND("]", ...)` locates the closing bracket before the sheet name
3. `MID(..., pos+1, 31)` extracts up to 31 characters of the sheet name

## Practical Uses

- **Monthly reports:** One template, renamed each month — title updates automatically
- **Dashboard tabs:** Sheet name drives the page title without manual editing
- **Duplicated worksheets:** Copy a sheet, rename it — formulas update without adjustment
- **Templates:** Build once, rename on deployment — all references update

## Caveat

> The workbook must be saved first. Until the file has a name, `CELL("filename")` returns nothing.

## Related

- [[Source-5-Boring-Excel-Functions-Mynda-Treacy]] — source
