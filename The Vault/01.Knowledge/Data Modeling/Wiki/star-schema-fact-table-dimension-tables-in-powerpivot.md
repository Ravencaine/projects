---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: pattern
tags: [data-modeling, star-schema, fact-table, dimension-table, powerpivot]
---

# Star Schema: Fact Table + Dimension Tables in PowerPivot

A star schema organizes data in a central fact table surrounded by denormalized dimension tables — the foundational data modeling pattern used by PowerPivot and all modern analytical databases.

## Purpose

The star schema separates the measures to be aggregated (fact table) from the attributes used to slice and filter (dimension tables), enabling fast aggregation across multiple dimensions without join complexity.

Dunlop (Ch4 + Ch7) uses the Contoso database as the canonical example: `dbo_FactSales` is the fact table, surrounded by `dbo_DimProduct`, `dbo_DimDate`, `dbo_DimChannel`, and `dbo_DimStore` as dimension tables.

## Components

- **Fact table:** Contains numeric measures (e.g., `TotalSales`, `TotalCost`, `SalesQuantity`, `UnitPrice`) and foreign keys linking to dimensions. Every analytical query aggregates this table.
- **Dimension tables:** One per logical entity (Product, Date, Channel, Store, Customer). Contains descriptive attributes (product name, category, color, size) used in row/column grouping.
- **Foreign key:** A field in the fact table (e.g., `ChannelKey`) that references the primary key of a dimension table (e.g., `DimChannel[ChannelKey]`).
- **Primary key:** A unique identifier in a dimension table (e.g., `DimChannel[ChannelKey]`).

## Structure

```
dbo_DimProduct (SK)
  ^                        ^
  | ChannelKey             | ProductKey
dbo_DimChannel (SK)  dbo_FactSales  dbo_DimDate (SK)
  ^                        | DateKey
  | StoreKey
dbo_DimStore (SK)
```

## Example

In the Contoso PowerPivot model:
- `dbo_FactSales[TotalSales]` — the measure (fact)
- `dbo_DimProduct[ProductCategoryName]` — used to group sales by category
- `dbo_DimChannel[ChannelName]` — used to filter by channel ("Store")
- PowerPivot auto-creates relationships when importing tables that have matching key fields

## Notes

- Dimension tables should be denormalized (wide, with descriptive text columns) for easier filtering
- Fact tables should be narrow (only keys + measures) for performance
- PowerPivot automatically detects relationships during import if foreign keys are present in the source database
- The fact table typically has a composite key (all foreign keys together) or a single surrogate key

## Related

- [[powerpivot-data-model-load-access-diagram-view-relationships]] — loading and viewing the schema in PowerPivot
- [[dax-calculate-function]] — CALCULATE filtering over fact/dimension relationships
- [[dax-year-over-year]] — year-over-year calculated fields using dimension date filters
