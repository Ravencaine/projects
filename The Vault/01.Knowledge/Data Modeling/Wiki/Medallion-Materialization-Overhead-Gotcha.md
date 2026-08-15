---
created: 2026-08-09
updated: 2026-08-09
source: "Do You Really Need Medallion Architecture.md"
note_type: gotcha
tags: [data-modeling, medallion-architecture, materialization, overhead, ownership, storage, gotcha]
---

# Medallion Materialization Overhead — Gotcha

> **Type:** gotcha
> **Routed to:** Data Modeling
> **Primary source:** Boniface Muchendu, Data Bear — 2026-03-24

## Problem

Every time a medallion layer is materialized (physical table created), it introduces a **boundary in the data pipeline:** each boundary requires:

- **Ownership:** who is responsible for this table
- **Maintenance:** keeping it up to date, schema changes
- **Storage:** paying for the physical storage
- **Monitoring:** ensuring data quality, freshness, pipeline health

## The Accumulation Effect

The full medallion pipeline:
```
Landing → Bronze → Silver → Gold
```

...costs:
- More storage (data duplicated at each layer)
- More orchestration (each layer needs scheduling)
- More complexity (more pipeline stages to maintain)
- More operational overhead (more things that can break)

## Why It Sneaks Up on Teams

Medallion architecture is the industry default. Teams implement it because "that's what you're supposed to do" — without asking whether each layer actually solves a specific problem for their specific situation.

## The Test

For each medallion layer, ask:

> **What specific problem does this layer solve?**

If the answer is vague or generic ("it stores cleaned data", "it provides a staging area"), the layer may be adding overhead without proportional value.

## When the Overhead Is Justified

The overhead is worth it when:
- Multiple teams depend on intermediate layers
- External consumers need certified intermediate datasets
- Data volumes require physical separation for performance

## When the Overhead Is Waste

The overhead is wasteful when:
- Single team, single consumer
- Stable, simple source data
- Each layer is nearly identical (Bronze ≈ Silver ≈ Gold)

## See Also

- [[Source-Do-You-Really-Need-Medallion-Architecture]] — source article
- [[Medallion-Architecture-Layer-Selection-Pattern]] — when to use medallion vs simplified
- [[Layers-Equal-Responsibility-Boundaries]] — the correct basis for adding layers
