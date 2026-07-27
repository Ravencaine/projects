---
created: 2026-07-26
source: system
note_type: reference
tags: [index, data-modeling]
---

# Data Modeling — Index

> Last updated: 2026-07-27

## Authors

| Note | Description |
|------|-------------|
| [[Jesse Ruiz]] | D365 F&O and retail dimensional modeling specialist |

## Source Notes

| Note | Description |
|------|-------------|
| [[3-easy-data-architecture-interview-questions-source]] | Source — data lake, medallion, batch vs stream |
| [[advanced-dimensional-modeling-retail-product-variants-source]] | Source — D365 product dimension (3-part series) |
| [[stop-building-slow-power-bi-reports-source]] | Source — Bill Donofrio; 10-point Power BI performance checklist |
| [[data-modeling-bi-trustworthy-analytics]] | Lagu — star schema, facts, dimensions, grain |
| [[data-warehousing-bi]] | Lagu — ETL/ELT, warehouse architecture, modern stack |
| [[data-warehouse-architectures-inmon-kimball-datavault]] | Ahmed Abdulwahid — Inmon vs Kimball vs Data Vault 2.0 |
| [[is-data-cleaning-more-painful-than-building-models]] | Gulab Chand Tejwani — data cleaning vs modeling effort |

## Conceptual Atomics

| Note | Description |
|------|-------------|
| [[data-lake-vs-data-warehouse]] | Schema-on-read vs schema-on-write; when to use each |
| [[medallion-architecture]] | Bronze/Silver/Gold layers in Delta Lake |
| [[batch-processing-vs-stream-processing]] | Batch vs stream; when to hybridise |
| [[lambda-kappa-architecture]] | Lambda and Kappa hybrid processing patterns |
| [[variant-complexity-problem-d365-fo]] | The 12+ table challenge in D365 F&O product data |
| [[simple-vs-variant-products]] | Simple (no variants) vs variant (Colour/Style/Size/Config) products |
| [[dimension-groups-color-style-size-config]] | Dimension group concept in D365 F&O |

## Patterns

| Note | Description |
|------|-------------|
| [[composite-key-strategy-itemkey]] | CONCAT-based ItemKey for simple + variant products |
| [[pricing-cte-with-row-number-deduplication]] | ROW_NUMBER for price deduplication in PriceDiscTable |
| [[conditional-joins-case-concat-matching]] | CASE/CONCAT dynamic join for dimension groups |
| [[union-all-pattern-simple-variant-products]] | UNION ALL for combining simple and variant product branches |
| [[materialized-views-vs-regular-views-cetas]] | CETAS and Materialized View performance patterns |
| [[index-strategy-filtered-index-barcode]] | Filtered index on Barcode column |
| [[replicated-table-distribution]] | Azure Synapse Replicated distribution |
| [[scd-type-1-price-changes]] | SCD Type 1 for pricing attributes |
| [[surrogate-keys-vs-composite-keys]] | Integer surrogate keys vs string composite keys |
| [[power-bi-correct-granularity-and-scd]] | Wrong SCD granularity causes full fact recalculation |
| [[many-to-many-bridge-table-pattern]] | Bridge tables for survey many-to-many |
| [[import-vs-directquery-performance]] | Import vs DirectQuery trade-offs |
| [[incremental-refresh-pattern]] | Append-only incremental refresh for large tables |
| [[column-pruning-bravo]] | Pruning unused columns with Bravo for Power BI |
| [[degenerate-dimension-barcode-in-fact]] | Barcode stored in fact table for scan speed |
| [[role-playing-dimension]] | Same dimension used multiple times |
| [[dim-date-dax-calendar]] | dim_date DAX using CALENDAR + ADDCOLUMNS |

## Atomic Conceptual Notes

| Note | Description |
|------|-------------|
| [[power-bi-visual-performance]] | Visual-level performance tips |

## Comparisons

| Note | Description |
|------|-------------|
| [[star-schema-vs-snowflake-schema]] | Performance trade-offs; when to use each |

## Errors

| Note | Description |
|------|-------------|
| [[missing-prices-debug-root-cause]] | RetailPrice = 0 / NULL; debug + root causes |
| [[duplicate-barcodes-retailshowforitem-filter]] | Multiple rows per barcode; retailshowforitem fix |
| [[performance-degradation-over-time]] | Slow queries as data grows; fixes |

## Open Questions

*(Use this space to track gaps, contradictions, and threads to explore.)*
