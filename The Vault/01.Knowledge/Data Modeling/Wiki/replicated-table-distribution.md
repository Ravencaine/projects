---
created: 2026-07-27
source: "Advanced Dimensional Modeling for Retail Product Variants Pt 3"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-pt-3-d02abbc97319"
note_type: pattern
tags: [distribution, replicated, dimension-table, azure-synapse, performance]
---

# Replicated Table Distribution

A table distribution strategy for Azure Synapse dedicated SQL Pool that broadcasts a dimension table to all compute nodes — eliminating data movement during joins at the cost of additional storage.

## Purpose

When a fact table is distributed across nodes (hash distribution), joining a dimension requires moving dimension rows to the nodes where fact rows live (data movement). For small, frequently-joined dimension tables, this is expensive. Replicated tables copy the full dimension to every compute node, eliminating data movement entirely.

## Structure

```sql
CREATE TABLE DIM_AllItems
WITH (
  DISTRIBUTION = REPLICATE  -- broadcasts to all compute nodes
)
AS SELECT * FROM DIM_AllItems_Base;
```

## When to Use

**Good fit:**
- Dimension tables (small row counts, frequent joins)
- Tables under ~10M rows in dedicated SQL pool
- Tables that are read-mostly (nightly refresh, not frequent writes)

**Avoid:**
- Large fact tables (replication storage cost multiplies)
- Frequently updated tables (replication sync overhead)

Rule of thumb: if the dimension is under 2GB per node, Replicate is almost always the right choice.

## Related

- [[materialized-views-vs-regular-views-cetas]] — pre-computation pair for the dimension
- [[performance-degradation-over-time]] — what happens as dimension grows
