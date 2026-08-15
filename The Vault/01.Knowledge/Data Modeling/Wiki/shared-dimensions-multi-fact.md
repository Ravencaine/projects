---
created: 2026-08-11
updated: 2026-08-11
source: "Handling Multiple Fact Tables in Power BI.md"
note_type: atomic
tags: [data-modeling, multi-fact, star-schema]
---

# Shared Dimensions with Multiple Fact Tables

Use one set of shared dimensions across all fact tables instead of duplicating dimensions per fact table.

## Definition

When a data model contains multiple fact tables (e.g., Internet Sales and Reseller Sales), each dimension table should be created once and related to all fact tables via one-to-many relationships. A single Date/Calendar table, for example, should serve as the filter context for both fact tables simultaneously.

## Key Points

- Shared dimensions reduce model size — one Date table instead of N copies
- Shorter refresh times: fewer tables to process and store
- Consistent filtering: the same attributes apply uniformly across all fact tables
- Report authors can slice any fact table by the same dimension attributes without confusion
- Only keep fact-specific dimensions isolated (e.g., Employee for Reseller Sales only)

## Examples

```
DimDate        (shared — relates to both)
DimProduct     (shared — relates to both)
DimLocation    (shared — relates to both)
DimEmployee    (fact-specific — Reseller Sales only)
DimCustomer    (shared — relates to both)

FactInternetSales
FactResellerSales
```

## Related

- [[conformed-dimensions]] — shared dimensions enforced to the same definitions across fact tables
- [[pitfall-duplicating-dimensions]] — what goes wrong when you duplicate dimensions per fact
- [[star-schema-fact-table-dimension-tables-in-powerpivot]] — foundational star schema pattern
