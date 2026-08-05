---
created: 2026-08-02
updated: 2026-08-02
source: How to Build a Clean P&L in Power BI — Select Distinct.md
note_type: atomic
tags: [power-bi, atomic, pl-statement, financial-reporting, structure, hierarchy]
---

# Executive P&L Statement Structure

A properly structured P&L in Power BI presents financial data in the standard executive sequence, with clear subtotal rows that aggregate from detailed accounts up to the key profit milestones.

## Standard P&L Hierarchy

```
Revenue
├── Sales Revenue
├── Other Income
└── Total Revenue

Cost of Sales
├── Direct Materials
├── Direct Labour
└── Total Cost of Sales

Gross Profit  ← key subtotal (Revenue − Cost of Sales)

Operating Expenses
├── Salaries
├── Rent
├── Utilities
└── Total Operating Expenses

Operating Profit  ← key subtotal (Gross Profit − OpEx)

Other Expenses / Tax
└── Net Profit  ← final subtotal
```

## What Makes a P&L "Clean"

- **Account codes** map to sections via a P&L Structure mapping table
- **Subtotals** (Gross Profit, Operating Profit, Net Profit) are calculated rows, not raw accounts
- **Sort order** is controlled by a Custom Sort column in the Section Mapping table — not alphabetical
- **Conditional formatting** distinguishes subtotal rows from detail rows
- **Matrix styling** uses horizontal gridlines (light grey) and no vertical gridlines for readability
- **Date columns** use Year or Month/Year hierarchy — never day-level — to prevent overflow

## Related

- [[pl-mapping-table-pattern]] — `pattern`
- [[pl-dynamic-matrix-visual]] — `pattern`
- [[pl-styling]] — `pattern`
- [[pl-conditional-formatting]] — `pattern`
- [[dynamic-pl-measure]] — `function`
- [[ytd-kpi-measures-pl]] — `function`
