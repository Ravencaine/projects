---
created: 2026-08-13
source: How to Build a Clean P&L in Power BI
note_type: pattern
tags: [power-bi, financial-reporting, p&l, matrix-visual, conditional-formatting, formatting, executive-report]
---

# P&L Matrix Formatting: Section Mapping + Conditional Formatting

<!-- Formatting recipe for converting a raw Power BI matrix into an executive-grade P&L: custom section mapping, spacing, borders, conditional totals, and KPI sidebar. -->

## The Goal

Turn a standard matrix visual into a clean corporate Profit & Loss statement with:
- Section headers (Revenue, Cost of Sales, Gross Profit, Expenses, Net Profit)
- Clean spacing between sections
- Highlighted key totals (Gross Profit, Operating Profit)
- Executive KPI sidebar alongside the P&L

## Section Mapping Table Pattern

Use a dedicated mapping table to control P&L row order. This is the critical step that makes a P&L work in Power BI's matrix visual.

```
PLSectionMapping table:
  Column 1: Section Name   (Revenue, Cost of Sales, Gross Profit, Expenses, Net Profit)
  Column 2: Custom Sort Order  (1, 2, 3, 4, 5)

Sort the Section Name column by Custom Sort Order in Power BI field properties.
```

Each account in the main structure table maps to a section via the section name column.

## Matrix Visual Styling

### Column Headers
- Font: Bold
- Alignment: Centre
- Background: Light Grey

### Values
- Background: White

### Gridlines
- Horizontal: On — Light Grey, 1px (easy multi-column scanning)
- Vertical: Off

### Row Spacing
- Blank Rows: On — adds spacing between P&L sections
- Row Padding: Off — keeps totals and headers tight

### Hierarchy Cleanup
- Expand/Collapse Icons: Off — static corporate report view
- Row Subtotals: Off (or selectively per section)
- Section Header Trick: Place company logo in top-left of the matrix to cover the default Section field header text

### General Polish
- Title: On — name the report (e.g., "Xero Demo Company Profit & Loss (£)")
- Grid Borders: Black — sharp container outline
- Canvas Background: Slightly deep grey — makes white matrix visual pop

## Conditional Formatting for Key Totals

Highlight Gross Profit and Operating Profit with a soft sage green (#E3E8E1):

1. Select the matrix → Format pane → Cell elements → Dynamic P&L measure
2. Background colour → fx (format by Rules)
3. Configure:
   - Format style: Rules
   - Apply to: Values and Totals
   - What field should we base this on: P&L (the row label field)

4. Add rules:
   - If value is "Gross Profit" → colour #E3E8E1
   - If value is "Operating Profit" → colour #E3E8E1

5. Ensure the conditional formatting toggle is switched ON in the formatting pane card.

## Executive KPI Sidebar

Complement the P&L matrix with a YTD snapshot sidebar:

### KPI Cards
| Card | DAX Pattern |
|------|-------------|
| Total YTD Revenue | `SUM(Transactions[Total])` filtered to Revenue |
| Total YTD Gross Profit | Revenue - Cost of Sales |
| YTD Operating Profit | Total Revenue - All Expenses |
| Operating Margin % | `DIVIDE([Operating Profit], [Total Revenue])` |

### Trend Visual
Column + Line chart: Revenue (columns) vs Operating Profit (line) by Month/Year.

## Related

- [[Power-BI-PL-Dashboard-Xero-to-Power-BI]] — end-to-end build pattern (data extraction + model + measures)
- [[matrix-layout-setup-workflow]] — general matrix formatting techniques
