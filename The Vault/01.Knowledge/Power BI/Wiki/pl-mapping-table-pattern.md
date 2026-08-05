---
created: 2026-08-02
updated: 2026-08-02
source: How to Build a Clean P&L in Power BI — Select Distinct.md
note_type: pattern
tags: [power-bi, pattern, mapping-table, data-modeling, custom-sort]
---

# P&L Mapping Table Pattern

The P&L mapping table is a manually created calculated/enter-data table that maps each account line to its P&L section and controls the sort order. It is the backbone of a clean, dynamic P&L Matrix in Power BI.

## Purpose

Without a mapping table, the Matrix visual shows accounts in alphabetical or raw order — not in the standard financial statement sequence (Revenue → Gross Profit → Operating Profit → Net Profit).

The mapping table converts raw account codes into a structured, sorted hierarchy.

## Two Required Mapping Tables

### P&L Section Mapping
Defines the sections and their display order:

| Section | Sort Order |
|---|---|
| Revenue | 1 |
| Cost of Sales | 2 |
| Gross Profit | 3 |
| Operating Expenses | 4 |
| Operating Profit | 5 |
| Net Profit | 6 |

Sort the **Section** column by the **Sort Order** column.

### P&L Structure Table
Maps each account to its section:

| Account Code | Account Name | Section |
|---|---|---|
| 100 | Sales Revenue | Revenue |
| 200 | Cost of Goods Sold | Cost of Sales |
| 300 | Gross Profit | *(calculated subtotal)* |
| ... | ... | ... |

## Key Properties

- Created via **Home** → **Enter Data** in Power BI Desktop
- Connected via 1-to-Many relationships to the Transactions table
- The Section Mapping table's sort-by configuration is critical — without it, sections appear alphabetically
- The Structure table drives the **Rows** field of the Matrix visual

## Relationship: Section Mapping → P&L Structure

P&L Structure[Section] ───1:Many─── Section Mapping[Section]

## Related

- [[pl-data-model-relationships]] — `pattern`
- [[pl-dynamic-matrix-visual]] — `pattern`
- [[executive-pl-statement-structure]] — `atomic`
- [[xero-power-bi-pl-pipeline]] — `pattern`
