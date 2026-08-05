---
created: 2026-08-02
updated: 2026-08-02
source: How to Build a Clean P&L in Power BI — Select Distinct.md
note_type: pattern
tags: [power-bi, pattern, conditional-formatting, matrix-visual, cell-elements, color-rules]
---

# P&L Conditional Formatting

Use Power BI conditional formatting on the Matrix visual to highlight key subtotal rows — Gross Profit and Operating Profit — with a professional sage green background. This gives the P&L visual hierarchy and makes key figures scanable at a glance.

## Setup

1. Select the Matrix visual
2. Open the **Format** pane (paintbrush icon)
3. Expand **Cell elements**
4. Select the series for the **Dynamic P&L** measure
5. Find **Background colour** → click the **fx** button

## Conditional Formatting Rules

| Condition | Field | Operator | Value | Colour |
|---|---|---|---|---|
| Gross Profit highlight | (row label) | is | Gross Profit | `#E3E8E1` (sage green) |
| Operating Profit highlight | (row label) | is | Operating Profit | `#E3E8E1` (sage green) |

## Important

The **conditional formatting toggle** in the formatting pane card must be switched **on** for the rules to render. If the sage green does not appear, check that the toggle is enabled.

## How It Works

The Matrix applies background colour to any row whose label matches "Gross Profit" or "Operating Profit". This requires the row labels in the Matrix to exactly match the section names in the P&L Structure table.

## Related

- [[pl-styling]] — `pattern`
- [[pl-dynamic-matrix-visual]] — `pattern`
- [[executive-pl-statement-structure]] — `atomic`
- [[pl-executive-sidebar]] — `pattern`
