---
created: 2026-08-02
updated: 2026-08-02
source: How to Build a Clean P&L in Power BI — Select Distinct.md
note_type: pattern
tags: [power-bi, pattern, matrix-visual, styling, formatting, gridlines]
---

# P&L Matrix Styling

Transform a default Power BI Matrix into a clean, executive-ready financial statement through deliberate grid, title, and border configuration.

## Matrix & Grid Styling

| Setting | Value | Reason |
|---|---|---|
| **Horizontal Gridlines** | On — Light Grey, 1px | Makes multi-column tracking easy to read |
| **Vertical Gridlines** | Off | Reduces visual clutter; not needed in a P&L |
| **Grid Borders** | Black | Sharp container outline for professional look |

## Visual-Level Polish

| Setting | Value |
|---|---|
| **Title** | On — e.g., "Xero Demo Company Profit & Loss (£)" |
| **Subtitle** | Optional — current period or YTD label |
| **Font** | Professional, consistent with brand |

## Hierarchy Cleanup

Power BI auto-generates expand/collapse toggles on row hierarchies. Ensure:
- Only the Section and P&L Line levels are visible
- Suppress any empty placeholder levels from the mapping tables

## Related

- [[pl-dynamic-matrix-visual]] — `pattern`
- [[pl-conditional-formatting]] — `pattern`
- [[pl-executive-sidebar]] — `pattern`
- [[executive-pl-statement-structure]] — `atomic`
