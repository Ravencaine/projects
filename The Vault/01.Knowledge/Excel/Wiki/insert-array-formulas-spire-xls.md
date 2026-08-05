---
created: 2026-08-05
updated: 2026-08-05
source: Automate Excel Formulas and Functions with Python A Complete Guide.md
note_type: pattern
tags: [excel, python, spire-xls, array-formulas]
---

# Array Formulas via FormulaArray (Spire.XLS)

Insert Excel array formulas using `FormulaArray` property. Array formulas perform calculations on multiple values and can return single or multiple results.

## Purpose

Execute matrix operations and batch data processing with array formulas via Spire.XLS — specifically the LINEST linear regression pattern and multi-cell array output.

## Components

- `cell.FormulaArray` — inserts an array formula (instead of `.Formula`)
- `workbook.CalculateAllValue()` — required after setting array formulas
- Cell range must span the correct output dimensions

## Structure

```python
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]

# Prepare data arrays
sheet.Range["A1"].NumberValue = 1
sheet.Range["A2"].NumberValue = 2
sheet.Range["A3"].NumberValue = 3
sheet.Range["B1"].NumberValue = 4
sheet.Range["B2"].NumberValue = 5
sheet.Range["B3"].NumberValue = 6
sheet.Range["C1"].NumberValue = 7
sheet.Range["C2"].NumberValue = 8
sheet.Range["C3"].NumberValue = 9

# Insert array formula — must span multiple cells for multi-result output
sheet.Range["A5:C6"].FormulaArray = "=LINEST(A1:A3,B1:C3,TRUE,TRUE)"

# Calculate all formula values
workbook.CalculateAllValue()

workbook.SaveToFile("ArrayFormulas.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Example

The example above runs `LINEST` (linear regression) with output spanning `A5:C6` (2 rows × 3 columns), matching LINEST's multi-cell output shape.

## Key Points

- Use `FormulaArray` instead of `Formula` for array formulas
- The target cell range must match the expected output dimensions of the array formula
- **Always call `CalculateAllValue()`** after inserting array formulas — without it, formulas remain unevaluated
- Common array formula use cases: matrix multiplication, simultaneous equations, regression analysis

## Related

- [[insert-basic-formulas-spire-xls]] — basic formula insertion
- [[insert-named-ranges-spire-xls]] — combining array formulas with named ranges
