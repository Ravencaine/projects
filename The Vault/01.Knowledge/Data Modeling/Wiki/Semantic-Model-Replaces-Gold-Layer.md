---
created: 2026-08-09
updated: 2026-08-09
source: "Do You Really Need Medallion Architecture.md"
note_type: pattern
tags: [data-modeling, semantic-model, gold-layer, aggregations, power-bi, pattern]
---

# Semantic Model Replaces Gold Layer — Pattern

> **Type:** pattern
> **Routed to:** Data Modeling
> **Primary source:** Boniface Muchendu, Data Bear — 2026-03-24

## Problem

Teams automatically build aggregated tables in the Gold layer, assuming pre-aggregation is always necessary for performance. But with Power BI semantic models, this may be redundant.

## Power BI Semantic Model Capabilities

Power BI can:
- **Calculate measures dynamically:** aggregations computed at query time
- **Handle large datasets efficiently:** VertiPaq engine compression and in-memory optimization
- **Generate aggregations on demand:** no pre-materialization required

## When Gold Layer Aggregates Are Unnecessary

If Power BI performance is acceptable without pre-aggregated tables, the Gold layer adds:
- Storage cost for duplicate data
- Pipeline complexity for maintaining aggregate tables
- Staleness risk (aggregates may fall out of sync)

## When Gold Layer Aggregates Are Still Needed

| Scenario | Why Gold Layer Needed |
|----------|----------------------|
| External reporting tools can't access the semantic model | Other tools need flat, pre-aggregated datasets |
| Large datasets require performance optimization | Query time aggregations too slow even with VertiPaq |
| Cross-platform analytics needs flattened datasets | Power BI not the only reporting tool |

## Decision Rule

```
Can Power BI semantic model handle the query performance?
├── YES → Gold layer aggregates are optional
└── NO → Consider Gold layer only after measuring actual performance
```

## Key Insight

> Don't add the Gold layer for pre-aggregation unless you've measured Power BI performance and found it insufficient. Measure first; add layers based on evidence, not habit.

## See Also

- [[Source-Do-You-Really-Need-Medallion-Architecture]] — source article
- [[Medallion-Architecture-Layer-Selection-Pattern]] — full layer selection decision
- [[Layers-Equal-Responsibility-Boundaries]] — correct basis for architecture decisions
