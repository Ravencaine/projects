---
created: 2026-08-09
updated: 2026-08-09
source: "Do You Really Need Medallion Architecture.md"
note_type: pattern
tags: [data-modeling, materialized-views, data-quality, lakehouse, microsoft-fabric, curated-layer, pattern]
---

# Materialized Views for Data Quality — Curated Layer Pattern

> **Type:** pattern
> **Routed to:** Data Modeling
> **Primary source:** Boniface Muchendu, Data Bear — 2026-03-24

## Problem

Teams add a Silver layer purely to handle data quality and validation — applying cleaning, casting, trimming before data reaches Silver. But in Fabric Lakehouses, materialized views can enforce data quality directly in the Curated layer, eliminating the need for a separate Silver layer.

## Materialized View Approach

Instead of Bronze → Silver → Gold:

```
Landing → Curated (with materialized views) → Analytics (optional)
```

The Curated layer uses materialized views to:
- Enforce data quality constraints directly
- Create a clean star schema (facts + dimensions)
- Apply validation rules as the data is materialized

## Data Validation Constraints (Examples)

These constraints are applied at the materialized view level in Fabric Lakehouses:

| Constraint | Rule |
|------------|------|
| NOT NULL | Product must not be NULL |
| NOT NULL | Category must not be NULL |
| Required field | Store must have a region |
| Positive values | Quantity must be greater than zero |
| Value range | Sales amount must be positive |

## Result

Clean data flows into the analytics layer without separate Silver transformation steps. The materialized view IS the transformation + quality enforcement.

## Benefits

- **Fewer layers:** eliminates separate Silver layer overhead
- **Quality at query time:** constraints enforced during materialization
- **Single source of truth:** one curated dataset with built-in quality
- **Faster pipelines:** fewer transformation steps

## When to Still Use Silver

- Data sources have complex, frequent schema changes requiring intermediate raw storage
- Multiple teams need a certified intermediate dataset
- Data quality rules are complex enough to warrant a separate transformation stage

## See Also

- [[Source-Do-You-Really-Need-Medallion-Architecture]] — source article
- [[Medallion-Architecture-Layer-Selection-Pattern]] — when to use medallion vs simplified
- [[Layers-Equal-Responsibility-Boundaries]] — the principle behind layer decisions
