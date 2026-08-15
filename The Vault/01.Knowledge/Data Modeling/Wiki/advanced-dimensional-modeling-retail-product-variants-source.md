---
created: 2026-07-27
updated: 2026-08-14
source: "Advanced Dimensional Modeling for Retail Product Variants"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-b4e6c1743382"
download_file: 99.System/Attachments/Code/sqlqueries_optimized_Retail_New_DeltaLake.sql
note_type: source
tags: [d365, retail, product-dimension, dimensional-modeling]
---

# Advanced Dimensional Modeling for Retail Product Variants (Parts 1–3)

Three-part Medium series by Jesse Ruiz covering the full lifecycle of a D365 F&O retail product dimension — from table relationships and composite key design, through conditional pricing joins and ROW_NUMBER deduplication, to production optimisation with CETAS and Azure Synapse distribution strategies.

> **Type:** article
> **Author:** Jesse Ruiz (she/they)
> **Published:** Part 1: 2026-04-27, Part 2: 2026-05-11, Part 3: 2026-05-25
> **URL:** https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-b4e6c1743382
> **Routed to:** Data Modeling

## Summary

The series tackles the most complex dimension in a retail star schema: the product dimension for D365 F&O, where a single master product can generate 48 SKUs across Colour/Style/Size/Config combinations. Each part builds on the previous: Part 1 establishes the data model and key strategy, Part 2 builds the pricing CTEs and conditional joins, and Part 3 addresses performance and common errors in production.

## Key Claims

- D365 F&O product data spans 12+ interconnected tables; no single Products table exists
- A unified ItemKey must handle both simple products and variant products using CONCAT-based composite key
- Conditional joins via CASE/CONCAT are required because dimension groups determine which attributes must be matched for pricing
- PriceDiscTable deduplication via ROW_NUMBER is essential because price history accumulates
- CETAS or Materialized Views are required for production; on-demand view execution is too slow for DirectQuery
- Three common errors: missing prices, duplicate barcodes (fix: retailshowforitem=1), and performance degradation

## Notable Details

- Download: [[99.System/Attachments/Code/sqlqueries_optimized_Retail_New_DeltaLake.sql]] — SQL source file for this series (DIM_AllItems view + optimised CTEs)
- Dimension groups observed: 'Donated' (Colour+Style+Size), 'DonatedNS' (Colour+Style), 'DonatedS' (Style), 'Retail Kit' (Config)
- The 1900-01-01 sentinel date in todate = permanent/future price (no end date)
- UNION ALL over UNION for combining simple and variant product branches

## Extracted Notes

Links to notes derived from this source:

- [[Jesse Ruiz]] — `author` — D365 F&O and retail dimensional modeling specialist
- [[variant-complexity-problem-d365-fo]] — `atomic` — the 12+ table challenge
- [[simple-vs-variant-products]] — `atomic` — two product types in one dimension
- [[dimension-groups-color-style-size-config]] — `atomic` — dimension group concept
- [[composite-key-strategy-itemkey]] — `pattern` — CONCAT-based ItemKey
- [[pricing-cte-with-row-number-deduplication]] — `pattern` — ROW_NUMBER for price deduplication
- [[conditional-joins-case-concat-matching]] — `pattern` — CASE/CONCAT dynamic join
- [[union-all-pattern-simple-variant-products]] — `pattern` — combining both product types
- [[materialized-views-vs-regular-views-cetas]] — `pattern` — pre-computation for DirectQuery
- [[index-strategy-filtered-index-barcode]] — `pattern` — filtered index design
- [[replicated-table-distribution]] — `pattern` — Azure Synapse distribution
- [[scd-type-1-price-changes]] — `pattern` — SCD Type 1 for pricing
- [[degenerate-dimension-barcode-in-fact]] — `pattern` — barcode in fact table
- [[role-playing-dimension]] — `pattern` — same dimension multiple times
- [[missing-prices-debug-root-cause]] — `error` — missing RetailPrice debug
- [[duplicate-barcodes-retailshowforitem-filter]] — `error` — retailshowforitem fix
- [[performance-degradation-over-time]] — `error` — slow queries as data grows

## Metadata

| Field | Value |
|-------|-------|
| Source file | Advanced Dimensional Modeling for Retail Product Variants.md (+ Pt 2 + Pt 3) |
| Archived at | [[99.System/InboxArchive/2026-07/Advanced Dimensional Modeling for Retail Product Variants.md]] |
| Download | [[99.System/Attachments/Code/sqlqueries_optimized_Retail_New_DeltaLake.sql]] |
| Ingestion date | 2026-07-27 |
| Word count | ~2,400 (parts combined) |
