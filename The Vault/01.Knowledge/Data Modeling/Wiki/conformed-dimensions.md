---
created: 2026-08-11
updated: 2026-08-11
source: "Handling Multiple Fact Tables in Power BI.md"
note_type: pattern
tags: [data-modeling, multi-fact, conformed-dimensions]
---

# Conformed Dimensions

Dimensions shared across fact tables with identical definitions — same attributes, same keys, same business meaning — enabling cross-fact aggregation and consistent filtering.

## Purpose

Conformed dimensions allow measures from different fact tables to be aggregated in the same report using the same row/column filters. Without conformance, each fact table becomes an isolated silo and cross-fact reporting requires complex measures or duplicated logic.

## Components

- **Shared key:** the same surrogate key links the dimension to each fact table
- **Identical attribute set:** column names, data types, and business definitions are identical across all fact contexts
- **Single source of truth:** the dimension table lives once; no copies

## Structure

```
DimProduct (single shared table)
  └── ProductKey  PK
      └── ProductName, Category, Subcategory, Brand, Color

FactInternetSales
  └── ProductKey  FK ──→ DimProduct[ProductKey]

FactResellerSales
  └── ProductKey  FK ──→ DimProduct[ProductKey]

Same filter = same result across both fact tables
```

## Example

A "Total Revenue" card visual can use `SUM(FactInternetSales[SalesAmount]) + SUM(FactResellerSales[SalesAmount])` and filter by `DimProduct[Category]` — one dimension handles both fact tables.

## Variations

- **Identical conformance:** dimension is byte-for-byte identical across all fact contexts
- **Shrunken/conformed:** a subset of a master dimension is conformed for a specific fact (e.g., a product category rollup table used by one fact but not another)

## Related

- [[shared-dimensions-multi-fact]] — the broader principle of sharing dimensions across fact tables
- [[pitfall-duplicating-dimensions]] — consequence of not using conformed dimensions
- [[implementing-star-schema-multi-fact]] — workflow for building this pattern
