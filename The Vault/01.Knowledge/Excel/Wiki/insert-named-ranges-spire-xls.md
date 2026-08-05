---
created: 2026-08-05
updated: 2026-08-05
source: Automate Excel Formulas and Functions with Python A Complete Guide.md
note_type: pattern
tags: [excel, python, spire-xls, named-ranges]
---

# Named Ranges in Spire.XLS

Create named ranges and named formulas in a workbook, then reference them in formulas. Improves formula readability and maintainability.

## Purpose

Replace complex cell references with meaningful names. Formulas become self-documenting, and changing the named range reference automatically updates all dependent formulas.

## Components

- `workbook.NameRanges.Add(name)` — creates a new named range
- `namedRange.RefersToRange = sheet.Range[...]` — assigns a cell range to a named range
- Named formula: assign a formula string to `namedRange.NameLocal`
- Formula references named range by name (no quotes needed)

## Structure

```python
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]

# Set data
sheet.Range["A1"].Value = "10"
sheet.Range["A2"].Value = "20"

# Create a named range
namedRange = workbook.NameRanges.Add("SumRange")
namedRange.RefersToRange = sheet.Range["A1:A2"]

# Use the named range in a formula
sheet.Range["C1"].Formula = "=SUM(SumRange)"

# Define a named formula directly
namedFormula = workbook.NameRanges.Add("TotalCalc")
namedFormula.NameLocal = "=SUM(A1+A2)"
sheet.Range["C2"].Formula = "TotalCalc"

workbook.SaveToFile("NamedRangeFormulas.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Advantages

- **Improved readability**: `=SUM(SumRange)` is clearer than `=SUM(A1:A2)`
- **Easier maintenance**: updating the named range reference automatically propagates to all formulas using that name
- **Reduced errors**: avoids manual entry of complex cell references

## Variations

Named formulas (as opposed to named ranges) don't point to a cell range — they encapsulate a calculation expression and can be referenced by name anywhere in the workbook.

## Related

- [[insert-basic-formulas-spire-xls]] — basic formula patterns
- [[insert-array-formulas-spire-xls]] — combining with array formulas
- [[cross-sheet-formula-references-spire-xls]] — cross-sheet named range references
