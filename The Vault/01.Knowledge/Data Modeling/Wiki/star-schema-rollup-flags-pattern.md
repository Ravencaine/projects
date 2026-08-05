---
created: 2026-08-02
updated: 2026-08-02
source: Why Star Schema FACT Tables Are More Powerful Than You Think (And How to Master Them).md
note_type: pattern
tags: [data-modeling, pattern, fact-table, pre-aggregation, rollup, materialized-view, dashboard-performance]
---

# Rollup Flags Pattern — Replaces 20 Materialized Views

Pre-aggregate fact table rows at multiple granularities and use boolean flags to indicate which aggregation level each row represents. Dashboards query the flag instead of scanning millions of raw rows. **Result: 2-minute dashboards reduced to 3 seconds.**

## The Pattern

```sql
CREATE TABLE fact_sales_clustered (
    is_monthly_summary   BOOLEAN DEFAULT FALSE,
    is_regional_summary  BOOLEAN DEFAULT FALSE,
    -- ...
    gross_revenue        DECIMAL(18,4) ENCODE ZSTD,
    net_profit           DECIMAL(18,4) ENCODE ZSTD
)
```

Three scenarios for the same underlying data — raw transactions, monthly rollups, regional rollups — stored in one table with flags distinguishing which type each row is.

## Dashboard Query

```sql
SELECT
    region_id,
    SUM(net_profit) AS total_regional_profit
FROM fact_sales_clustered
WHERE sales_quarter = '2023-Q4'
  AND is_regional_summary = TRUE
GROUP BY region_id;
```

Instead of scanning millions of raw rows for a quarterly regional dashboard, the query hits only the pre-aggregated regional summary rows.

## When to Use

- Dashboard queries always aggregate to the same levels (monthly, regional)
- Materialized views are slow to maintain or expensive on the cloud platform
- The same metrics are queried at multiple granularities repeatedly

## Related

- [[star-schema-fact-table-principles]] — `atomic`
- [[star-schema-zstd-encoding-clustering]] — `pattern`
- [[star-schema-multi-key-partitioning]] — `pattern`
