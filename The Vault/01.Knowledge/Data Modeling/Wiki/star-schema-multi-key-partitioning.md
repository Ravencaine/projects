---
created: 2026-08-02
updated: 2026-08-02
source: Why Star Schema FACT Tables Are More Powerful Than You Think (And How to Master Them).md
note_type: pattern
tags: [data-modeling, pattern, fact-table, partitioning, cloud-data-warehouse, performance]
---

# Multi-Key Partitioning (Time AND Geography)

Partition a large fact table by two keys — time and a geographic or business dimension — rather than by date alone. Most teams stop at date partitioning and scan too much irrelevant data on every query.

## The Pattern

```sql
CREATE TABLE fact_sales_clustered (
    sales_quarter VARCHAR(10) NOT NULL,
    region_id     INT NOT NULL,
    -- ...
)
PARTITION BY (sales_quarter, region_id)
ORDER BY (customer_id, transaction_id);
```

Two-partition key: `sales_quarter` (time) + `region_id` (geography). Query predicates on either partition column trigger partition pruning.

## Performance Impact

| Partition Strategy | Query Performance |
|---|---|
| Date only | Full partition scan for regional queries |
| Quarter + Region | Partition pruning on both dimensions; ~60% compute cost reduction |
| Quarter + Region + Customer clustering | 40% faster BI queries via sorting |

## When to Apply

- Table exceeds 100GB (partitioning overhead not worth it below this)
- Common query patterns filter by both time and a geographic/business dimension
- Cloud data warehouse with per-partition pricing (Snowflake, BigQuery, Redshift Spectrum)

## Related

- [[star-schema-zstd-encoding-clustering]] — `pattern`
- [[star-schema-fact-table-principles]] — `atomic`
