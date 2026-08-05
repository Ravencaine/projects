---
created: 2026-08-05
updated: 2026-08-05
source: Automate Excel Formulas and Functions with Python A Complete Guide.md
note_type: function
tags: [excel, functions, aggregation, subtotal]
---

# SUBTOTAL (Excel)

Calculates a specified aggregate function over a range, automatically ignoring hidden (filtered-out) rows. Does not ignore cells containing other SUBTOTAL results.

## Signature

```
=SUBTOTAL(function_num, ref1, [ref2, ...])
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `function_num` | integer | Controls which aggregate to compute (see table below) |
| `ref1` | range | First range to aggregate |
| `ref2` | range | Optional additional ranges |

## Function Numbers

| Number | Function | Ignores hidden rows |
|--------|----------|---------------------|
| 1 | AVERAGE | Yes |
| 2 | COUNT | Yes |
| 3 | COUNTA | Yes |
| 4 | MAX | Yes |
| 5 | MIN | Yes |
| 9 | SUM | Yes |

Numbers 101–111 perform the same operations but ignore **all** hidden rows (including manually hidden).

## Returns

A single scalar value — the result of the aggregate function over the specified range(s).

## Examples

```python
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]

# Prepare data
for row in range(1, 4):
    sheet.Range[f"A{row}"].NumberValue = row
    sheet.Range[f"B{row}"].NumberValue = row + 3
    sheet.Range[f"C{row}"].NumberValue = row + 6

# Insert SUBTOTAL functions using different function numbers
sheet.Range["A5"].Formula = "=SUBTOTAL(1,A1:C3)"  # AVERAGE
sheet.Range["B5"].Formula = "=SUBTOTAL(2,A1:C3)"  # COUNT
sheet.Range["C5"].Formula = "=SUBTOTAL(5,A1:C3)"  # MIN

workbook.CalculateAllValue()
workbook.SaveToFile("SubtotalFormulas.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Notes

- SUBTOTAL ignores rows hidden by AutoFilter — ideal for interactive reports
- Does **not** ignore manually hidden rows unless using function numbers 101–111
- Nested SUBTOTAL calls within the range are excluded from the outer calculation
- Incompatible with 3D references

## Related

- [[insert-basic-formulas-spire-xls]] — inserting SUBTOTAL via Spire.XLS
