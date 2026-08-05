---
created: 2026-07-27
updated: 2026-08-02
source: "Advanced Dimensional Modeling for Retail Product Variants Pt 3"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-pt-3-d02abbc97319"
note_type: error
tags: [performance, degradation, slow-query, statistics, azure-synapse]
---

# Performance Degradation Over Time

Symptom: a dimension view that took 30 seconds last month now takes 2 minutes. The logic hasn't changed, but query performance has worsened steadily.

## Error / Symptom

```
Month 1:  DIM_AllItems query → 28 seconds
Month 3:  DIM_AllItems query → 75 seconds
Month 6:  DIM_AllItems query → 130 seconds
```

No code changes — only data volume growth.

## Cause

Three compounding factors:

1. **Product catalog growth**: more variants added to InventDimCombination over time
2. **Price history accumulation**: PriceDiscTable grows with each new price agreement; more rows to filter in the ROW_NUMBER CTE
3. **Stale statistics**: the query optimizer makes execution plans based on table statistics; as data grows, statistics become stale and the plan becomes suboptimal

## Solution

```sql
-- 1. Materialize CTEs as temp tables (reduce repeated work)
SELECT * INTO #pricediscpurch FROM pricediscpurch;
SELECT * INTO #ProductVariants FROM ProductVariants;

-- 2. Filter by dataareaid early (reduces data volume dramatically)
WHERE t1.dataareaid IN ('USMF', 'USSI')

-- 3. Use CETAS for overnight refresh (pre-compute, don't recompute)
CREATE EXTERNAL TABLE [Delta].[DIM_AllItems]
WITH (LOCATION = '/dimensions/dim_allitems_' + FORMAT(GETDATE(), 'yyyyMMdd') + '/')
AS SELECT ...;

-- 4. Rebuild statistics
UPDATE STATISTICS DIM_AllItems;
```

## Prevention

- Schedule nightly CETAS rebuilds rather than relying on on-demand view execution
- Monitor row counts and query duration monthly; trigger a rebuild when growth exceeds 20%
- Use `AUTO_UPDATE_STATISTICS` on dedicated SQL Pool

## Related Errors

- [[materialized-views-vs-regular-views-cetas]] — the production solution
- [[replicated-table-distribution]] — the distribution solution
