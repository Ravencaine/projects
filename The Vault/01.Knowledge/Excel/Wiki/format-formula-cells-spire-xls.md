---
created: 2026-08-05
updated: 2026-08-05
source: Automate Excel Formulas and Functions with Python A Complete Guide.md
note_type: pattern
tags: [excel, python, spire-xls, formatting]
---

# Format Formula Cells (Spire.XLS)

Apply visual formatting to formula cells to distinguish them from data cells. Useful for building automation reports where formula cells need visual highlighting.

## Purpose

Automatically format cells containing formulas — background colour, borders, number formats — so that formula results are visually distinct in automated Excel outputs.

## Components

- `cell.Style.Color` — set background fill colour
- `cell.Style.NumberFormat` — set number/date format string
- `cell.Style.Borders[BordersLineType.EdgeXxx]` — apply border formatting

## Structure

```python
from spire.xls import *
from spire.xls.common import *

workbook = Workbook()
sheet = workbook.Worksheets[0]

# Insert formula
sheet.Range["A1"].Formula = "=SUM(B1:B10)"

# Set background colour (light yellow)
sheet.Range["A1"].Style.Color = Color.get_LightYellow()

# Add borders
sheet.Range["A1"].Style.Borders[BordersLineType.EdgeTop].LineStyle = LineStyleType.Thin
sheet.Range["A1"].Style.Borders[BordersLineType.EdgeBottom].LineStyle = LineStyleType.Thin

# Number format for date/time results
sheet.Range["B1"].Formula = "=NOW()"
sheet.Range["B1"].Style.NumberFormat = "yyyy-MM-DD HH:mm:ss"

workbook.SaveToFile("FormattedFormula.xlsx", ExcelVersion.Version2010)
workbook.Dispose()
```

## Common Number Formats

| Format string | Result example |
|---|---|
| `yyyy-MM-DD` | 2026-08-05 |
| `HH:mm:ss` | 14:30:00 |
| `yyyy-MM-DD HH:mm:ss` | 2026-08-05 14:30:00 |
| `#,##0.00` | 1,234.56 |

## Related

- [[insert-basic-formulas-spire-xls]] — formula insertion
- [[insert-array-formulas-spire-xls]] — array formula formatting
