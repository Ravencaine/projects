---
created: 2026-08-05
updated: 2026-08-05
source: Automate Excel Formulas and Functions with Python A Complete Guide.md
note_type: pattern
tags: [excel, python, spire-xls, formulas]
---

# Insert Basic Formulas (Spire.XLS)

Insert Excel formulas into a worksheet by assigning a formula string to the cell's `Formula` property. All Excel formula syntax applies — constants, cell references, operators, function calls.

## Purpose

Programmatically populate Excel cells with formulas using Spire.XLS for Python. Automates bulk formula insertion in data processing pipelines.

## Components

- `spire.xls.Workbook` — the workbook container
- `spire.xls.Worksheet` — the target sheet
- `cell.Formula` — assigns a formula string (always begins with `=`)
- `workbook.CalculateAllValue()` — forces recalculation of all formulas

## Structure

```python
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]

# Arithmetic
sheet.Range["B5"].Formula = "=1+2+3+4+5-6-7+8-9"
sheet.Range["B6"].Formula = "=33*3/4-2+10"

# Cell references (absolute)
sheet.Range["B7"].Formula = "=Sheet1!$B$2"

# Range references
sheet.Range["B8"].Formula = "=AVERAGE(Sheet1!$B$2:$D$2)"

workbook.SaveToFile("output.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Example

```python
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]

# Set test data
sheet.Range["B2"].NumberValue = 7.3
sheet.Range["C2"].NumberValue = 5
sheet.Range["D2"].NumberValue = 8.2

# Formula using a range reference
sheet.Range["B8"].Formula = "=AVERAGE(Sheet1!$B$2:$D$2)"

# Force calculation
workbook.CalculateAllValue()

workbook.SaveToFile("BasicFormulas.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Key Points

- Always prefix formulas with `=` — the string assigned to `.Formula` must be a valid Excel formula
- `.Text` vs `.Formula`: `.Text` sets the displayed string; `.Formula` evaluates it as a formula
- Absolute references (`$`) and range references (`:`) work identically to manual Excel entry
- Always call `workbook.Dispose()` to release resources

## Related

- [[insert-array-formulas-spire-xls]] — array formula insertion with `FormulaArray`
- [[insert-named-ranges-spire-xls]] — named ranges for formula readability
- [[cross-sheet-formula-references-spire-xls]] — referencing other worksheets
