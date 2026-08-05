---
created: 2026-08-02
updated: 2026-08-02
source: How to Build a Clean P&L in Power BI — Select Distinct.md
note_type: reference
tags: [data-modeling, reference, pl, financial-reporting, account-codes, chart-of-accounts]
---

# P&L Line Structure Reference

Standard account code and P&L line structure used when building a corporate Profit & Loss statement in Power BI. This is the reference layout for mapping via the P&L Structure table.

## Account Code Ranges

| Code Range | Category |
|---|---|
| 100–199 | Revenue |
| 200–299 | Cost of Sales / Direct Costs |
| 300–399 | Gross Profit (calculated) |
| 400–499 | Operating Expenses |
| 500–599 | Operating Profit (calculated) |
| 600+ | Other Expenses, Tax, Net Profit |

## Standard P&L Sections

1. **Revenue:** top-line sales and other income
2. **Cost of Sales:** direct costs attributable to revenue
3. **Gross Profit:** Revenue minus Cost of Sales *(calculated subtotal)*
4. **Operating Expenses:** overhead costs
5. **Operating Profit:** Gross Profit minus Operating Expenses *(calculated subtotal)*
6. **Net Profit:** Operating Profit minus tax and other expenses *(final subtotal)*

## Mapping in Power BI

Each account code in the Chart of Accounts is mapped to a P&L Section via the P&L Structure table. Subtotals (Gross Profit, Operating Profit, Net Profit) are handled as calculated rows in the Dynamic P&L measure — they do not have corresponding raw transaction rows.

## Related

- [[pl-mapping-table-pattern]] — `pattern`
- [[executive-pl-statement-structure]] — `atomic`
- [[dynamic-pl-measure]] — `function`
- [[xero-power-bi-pl-pipeline]] — `pattern`
