---
created: 2026-08-11
updated: 2026-08-11
source: "Handling Multiple Fact Tables in Power BI.md"
note_type: workflow
tags: [data-modeling, workflow, star-schema, multi-fact]
---

# Implementing Star Schema with Multiple Fact Tables

Build a clean multi-fact star schema in Power BI using shared dimensions and conformed relationships.

## Prerequisites

- Multiple fact tables loaded into Power BI (e.g., via Power Query)
- Access to source dimension tables
- Understanding of which dimensions are shared vs fact-specific

## Steps

1. **Identify shared dimensions.** Scan all fact tables for common entities: Date/Calendar, Product, Customer, Location. These become the shared dimensions — one table each.

2. **Import shared dimensions once.** Load only one Date table, one Product table, one Customer table, one Location table into the model.

3. **Create one-to-many relationships.** For each shared dimension, drag from its primary key to the matching foreign key in each fact table. Repeat for all shared dimensions across all fact tables.

4. **Keep fact-specific dimensions isolated.** Dimensions that apply to only one fact table (e.g., Employee for Reseller Sales) remain linked only to that fact table. Do not duplicate them.

5. **Add table descriptions.** In Power BI model view, right-click each table → Properties → Description. Write a short note indicating which fact tables the dimension serves. Example: "Used by: FactInternetSales, FactResellerSales."

6. **Test cross-fact reporting.** Create a visual that aggregates across multiple fact tables using a shared dimension filter. Verify correct totals with no blanks from unrelated fact-specific dimensions.

## Variations

- **Mixed granularity facts:** if one fact is daily and another is monthly, use the daily date table as the shared dimension and filter the monthly fact appropriately (the monthly fact will have blanks on day-level granularity — expected and correct)
- **Conformed dimension subset:** create a shrunken conformed dimension (e.g., product category rollup) shared across facts that need only that level

## Related

- [[shared-dimensions-multi-fact]] — the principle behind step 1-3
- [[conformed-dimensions]] — identical dimension definitions across facts
- [[pitfall-duplicating-dimensions]] — what step 2 avoids
- [[pitfall-consolidated-fact-tables]] — what keeping facts separate avoids
- [[star-schema-fact-table-dimension-tables-in-powerpivot]] — foundational star schema
