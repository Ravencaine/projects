---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: entity
tags: [entity, performance, Data Modeling]
---

# Deferred Indexing Strategy

<!-- The practice of deferring index creation until after the schema is fully stabilized but before BI reporting begins, when all join paths and filter scenarios are visible. Speculative indexes before schema completion miss critical paths; indexes after reporting is tuned to suboptimal paths. -->

## Definition

The practice of deferring index creation until after the schema is fully stabilized but before BI reporting begins, when all join paths and filter scenarios are visible. Speculative indexes before schema completion miss critical paths; indexes after reporting is tuned to suboptimal paths.
