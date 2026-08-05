---
created: 2026-08-02
updated: 2026-08-02
source: How to Build a Clean P&L in Power BI — Select Distinct.md
note_type: pattern
tags: [power-bi, pattern, matrix-visual, rows-hierarchy, columns, show-items-no-data]
---

# Dynamic P&L Matrix Visual

The Matrix visual is the core of a Power BI P&L. It uses the P&L Structure table for rows and a Dynamic P&L measure for values, driven by a date hierarchy on the columns.

## Configuration

### Rows Field
From the **P&L Structure** table:
- **Section:** top-level grouping (Revenue, Gross Profit, etc.)
- **P&L Line:** individual account rows

This two-level row hierarchy collapses to a clean executive-style P&L.

### Columns Field
From the **Transactions** table:
- **Date:** but **switch from default day hierarchy to Year or Month/Year**. Day-level columns cause horizontal overflow in a P&L report.
- The column hierarchy drives the time period coverage (e.g., monthly or yearly columns)

### Values Field
The **Dynamic P&L** measure (see [[dynamic-pl-measure]]).

## Show Items with No Data

If any rows appear blank, right-click the **Row** field → toggle **Show items with no data** against the **Section** level. This ensures sections like Gross Profit show even when they are calculated subtotals rather than raw accounts.

## Expansion

Expand the toggle arrows (+/-) on each section to reveal line-by-line account figures within that section.

## Related

- [[dynamic-pl-measure]] — `function`
- [[pl-mapping-table-pattern]] — `pattern`
- [[pl-styling]] — `pattern`
- [[pl-conditional-formatting]] — `pattern`
- [[executive-pl-statement-structure]] — `atomic`
