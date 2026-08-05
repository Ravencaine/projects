---
created: 2026-08-02
updated: 2026-08-02
source: How to Build a Clean P&L in Power BI — Select Distinct.md
note_type: pattern
tags: [power-bi, pattern, data-modeling, relationship, mapping-table, chart-of-accounts]
---

# P&L Relationship & Data Model

The P&L in Power BI requires a four-table data model with carefully constructed 1-to-Many relationships. The mapping tables drive both the structure and the sorting order of the visual.

## Tables

| Table | Role |
|---|---|
| Transactions | Raw financial line items (from Xero export) |
| Chart of Accounts | Master account codes and categories |
| P&L Section Mapping | Section names + Custom sort order |
| P&L Structure | Account-to-section mapping (the row hierarchy) |

## Relationships

Build **1-to-Many** relationships:

```
Chart of Accounts[Account Code] ───1:Many─── Transactions[Account Code]
P&L Structure[Account Code]       ───1:Many─── Transactions[Account Code]
P&L Section Mapping[Section]       ───1:Many─── P&L Structure[Section]
```

## Sort-by Configuration

Sort the **Section** column in the P&L Section Mapping table by the **Custom sort order** column. This ensures the P&L flows in correct financial order: Revenue → Direct Costs → Gross Profit → Operating Expenses → Operating Profit → Net Profit.

## Null Value Trap

If the 1-to-Many relationship fails to validate, **filter out null values in the Date column** via Power Query, then click **Close & Apply**.

## Related

- [[pl-null-date-break-relationships]] — `gotcha`
- [[pl-mapping-table-pattern]] — `pattern`
- [[executive-pl-statement-structure]] — `atomic`
- [[xero-power-bi-pl-pipeline]] — `pattern`
