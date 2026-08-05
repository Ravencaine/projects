---
created: 2026-08-05
updated: 2026-08-05
source: Automate Excel Formulas and Functions with Python A Complete Guide.md
note_type: pattern
tags: [excel, python, spire-xls, cross-sheet]
---

# Cross-Sheet Formula References (Spire.XLS)

Reference cells and ranges from other worksheets within a workbook by prefixing the reference with the sheet name and an exclamation mark.

## Purpose

Build formulas that aggregate or transform data across multiple worksheets in an automated workbook — the same cross-sheet reference syntax used in manual Excel entry.

## Components

- Sheet name + `!` prefix — the Excel cross-sheet reference syntax
- `workbook.Worksheets.Add(name)` — add a named worksheet
- `sheet.Name` — rename an existing worksheet

## Structure

```python
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()

# Create and name worksheets
data_sheet = workbook.Worksheets[0]
data_sheet.Name = "Data"
calc_sheet = workbook.Worksheets.Add("Calculation")

# Set data in the first worksheet
data_sheet.Range["A1"].NumberValue = 100
data_sheet.Range["A2"].NumberValue = 200

# Reference data from the first worksheet in the second worksheet
calc_sheet.Range["A1"].Formula = "=Data!A1+Data!A2"

workbook.CalculateAllValue()

workbook.SaveToFile("CrossSheetFormula.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Syntax

```
=SheetName!CellReference
=SheetName!RangeStart:RangeEnd
```

Spaces in sheet names require single quotes: `'Sheet Name'!A1`.

## Related

- [[insert-basic-formulas-spire-xls]] — single-sheet formula basics
- [[insert-named-ranges-spire-xls]] — cross-sheet named range references
