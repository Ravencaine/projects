---
created: 2026-07-27
source: "Advanced Dimensional Modeling for Retail Product Variants Pt 3"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-pt-3-d02abbc97319"
note_type: pattern
tags: [materialized-view, cetas, performance, optimization, azure-synapse]
---

# Materialized Views vs Regular Views (CETAS)

Performance strategy for pre-computing complex dimension views — choosing between native Materialized Views (dedicated SQL pool) and CETAS (serverless pool / Delta Lake).

## Purpose

A regular view re-executes the full query (12+ table joins, conditional pricing logic, CTEs) every time a user queries it. For DirectQuery Power BI reports, this causes unacceptable latency. Pre-computing the result as a table eliminates the per-query compute cost.

## Components

- `CREATE VIEW` — regular view (query-time execution)
- `CREATE MATERIALIZED VIEW` — dedicated SQL pool only (pre-computed, auto-refreshed)
- `CREATE EXTERNAL TABLE ... AS SELECT` (CETAS) — serverless pool (pre-computed to Parquet/Delta in ADLS)

## Structure

```sql
-- Regular view (development)
CREATE VIEW [Delta].[DIM_AllItems] AS
SELECT ... (complex query runs every time)

-- Materialized view (dedicated SQL pool)
CREATE MATERIALIZED VIEW [Delta].[DIM_AllItems_Materialized] AS
SELECT ...

-- CETAS pattern (serverless pool)
CREATE EXTERNAL TABLE [Delta].[DIM_AllItems_External]
WITH (
  LOCATION = '/dimensions/dim_allitems/',
  DATA_SOURCE = [DeltaLake],
  FILE_FORMAT = [ParquetFormat]
)
AS SELECT * FROM [complex view];
```

## When to Use Each

| Approach | Use When |
|----------|---------|
| Regular view | Development; easy schema changes; small datasets |
| Materialized View | Dedicated SQL pool; need auto-refresh; static-ish data |
| CETAS | Serverless pool; need Delta Lake integration; nightly rebuild |
| CETAS with date partition | Daily incremental rebuild: `LOCATION = '/dimensions/dim_allitems_' + FORMAT(GETDATE(), 'yyyyMMdd')` |

## Related

- [[index-strategy-filtered-index-barcode]] — complementary indexing strategy
- [[replicated-table-distribution]] — distribution strategy for large dimensions
