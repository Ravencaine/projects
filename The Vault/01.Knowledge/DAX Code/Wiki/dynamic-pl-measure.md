---
created: 2026-08-02
updated: 2026-08-02
source: How to Build a Clean P&L in Power BI — Select Distinct.md
note_type: function
tags: [dax, function, pl, financial-reporting, matrix, subtotal, dynamic-measure]
---

# Dynamic P&L Measure

The core DAX measure that iterates through the P&L Structure table and returns the correct financial value for each row — handling both standard accounts and calculated subtotal rows cleanly within a single Matrix measure.

## Purpose

A standard `SUM(Transactions[Amount])` works for detail rows but does not handle calculated subtotals (Gross Profit, Operating Profit, Net Profit) correctly in a Matrix visual. The Dynamic P&L measure uses conditional logic to detect whether the current row is a detail account or a subtotal, and returns the appropriate aggregation.

## Key Behavior

- Iterates through the P&L Structure table context
- For **detail rows** (e.g., Sales Revenue): returns the sum of matching transactions
- For **subtotal rows** (e.g., Gross Profit): returns a calculated aggregate (Revenue − Cost of Sales)
- Placed in the **Values** field of the Matrix visual alongside Section and P&L Line from the Structure table

## Core DAX Pattern

The measure uses `IF` or `SWITCH` to detect the P&L Line type and apply the correct aggregation. The exact formula depends on how subtotals are represented in the P&L Structure table — either as marked rows or as calculated sections.

## Placement

- **Visual**: Matrix
- **Fields**: Values → Dynamic P&L Measure
- **Context**: Rows = Section + P&L Line (from P&L Structure table)

## Related

- [[pl-dynamic-matrix-visual]] — `pattern`
- [[executive-pl-statement-structure]] — `atomic`
- [[ytd-kpi-measures-pl]] — `function`
