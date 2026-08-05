---
created: 2026-08-05
updated: 2026-08-05
source: Automate Excel Formulas and Functions with Python A Complete Guide.md
note_type: reference
tags: [excel, python, spire-xls, reference]
---

# Spire.XLS Python API Quick Reference

Cheat sheet for the Spire.XLS for Python API as used in Excel formula automation workflows.

## Quick Reference

### Installation

```bash
pip install Spire.XLS
```

### Core Imports

```python
from spire.xls import *
from spire.xls.common import *
```

### Workbook Lifecycle

```python
workbook = Workbook()           # Create
workbook.SaveToFile("out.xlsx", ExcelVersion.Version2010)  # Save
workbook.Dispose()             # Release resources — always call
```

### Worksheet Access

```python
sheet = workbook.Worksheets[0]              # By index
sheet = workbook.Worksheets["SheetName"]    # By name
sheet = workbook.Worksheets.Add("NewSheet") # Add new sheet
sheet.Name = "Data"                         # Rename sheet
```

### Cell Operations

| Operation | API |
|-----------|-----|
| Set value | `sheet.Range["A1"].Value = "10"` |
| Set number | `sheet.Range["A1"].NumberValue = 7.3` |
| Set formula | `sheet.Range["A1"].Formula = "=SUM(B1:B10)"` |
| Set array formula | `sheet.Range["A1:B2"].FormulaArray = "=LINEST(...)"` |
| Get value | `sheet.Range["A1"].Value` |
| Format cell | `sheet.Range["A1"].Style.NumberFormat = "yyyy-MM-DD"` |
| Background colour | `sheet.Range["A1"].Style.Color = Color.get_LightYellow()` |
| Borders | `sheet.Range["A1"].Style.Borders[BordersLineType.EdgeTop].LineStyle = LineStyleType.Thin` |

### Named Ranges

```python
namedRange = workbook.NameRanges.Add("MyRange")
namedRange.RefersToRange = sheet.Range["A1:A10"]
```

### Formula Calculation

```python
workbook.CalculateAllValue()  # Force recalculate all formulas
```

## Notes

- All formula strings must begin with `=`
- `Formula` vs `Text`: use `Formula` for evaluation, `Text` for literal display
- Always dispose workbook to prevent file locks
- ExcelVersion options: `ExcelVersion.Version2010`, `Version2013`, `Version2016`, etc.

## Related

- [[insert-basic-formulas-spire-xls]] — basic formula insertion pattern
- [[insert-array-formulas-spire-xls]] — array formula insertion
- [[insert-named-ranges-spire-xls]] — named ranges pattern
- [[format-formula-cells-spire-xls]] — formatting formula cells
- [[cross-sheet-formula-references-spire-xls]] — cross-sheet references
