---
created: 2026-08-08
updated: 2026-08-08
source: 11 Power BI Tips
note_type: atomic
tags: [power-bi, measure, model-view, productivity, best-practice]
---

# Bulk Edit Measure Properties in Model View

Multi-select measures in Model View to apply format strings, display folders, summarizations, and other properties to all selected measures at once.

## Definition

Power BI Model View supports multi-select (Ctrl+click or "Select All Measures"). Multi-selected compatible properties can be changed in one operation, saving dozens of individual clicks when formatting large sets of measures.

## Key Points

- **Multi-select**: Ctrl+click individual measures, or right-click → Select All Measures
- **Compatible properties** that can be bulk-edited:
  - Format string (Currency, Decimal, Percentage, etc.) + decimal places
  - Display folder
  - Summarization type (Sum, Average, Count, Don't Summarize, etc.)
  - Data type
- All selected measures must share a compatible format for the bulk edit to apply correctly
- Useful for: applying currency formatting to all revenue measures, setting all ratio measures to Percentage, grouping into display folders
- Works together with [[Measure-Table-Dedicated]] — select all measures in the measure table for a full-format sweep

## Example

**Apply currency format to all revenue measures:**
1. Go to Model View
2. Ctrl+click to select: `Total Revenue`, `Room Revenue`, `Experience Revenue`, `Net Revenue`
3. Properties → Format → Currency → set decimal places
4. All selected measures update simultaneously

**Move all measures to measure table:**
1. Right-click → Select All Measures
2. Properties → General → Table → choose `Measures`

## Related

- [[Measure-Table-Dedicated]] — where to organize measures
- [[Organizing-Measures-Display-Folders]] — organizing with display folders
