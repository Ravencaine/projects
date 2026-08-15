---
created: 2026-08-06
updated: 2026-08-06
source: Building a Data Warehouse from Scratch A Case Study in Kimball Modeling.md
note_type: reference
tags: [data-warehouse, performance, indexing, schema, dimensional-modeling]
---

# Indexing Strategy — Defer Until Schema Complete

Index too early and you add either speculative overhead or missed coverage. Index too late and existing reports may already be tuned to suboptimal paths. The right moment is after schema stabilization but before BI reporting begins.

## When to Add Indexes

**Wrong:** During initial dimensional modeling, before all fact and dimension tables are designed.

**Right:** After all fact and dimension table designs are finalized, but before real reports are written on the BI tool.

At this point you can clearly see:

- Which columns serve as dimension foreign keys
- Which columns are used for date-based filtering
- Which columns bridge fact tables together
- Which columns in bridge tables are used for joins

## Decision Criteria

> Tie every indexing decision to the question: "Is there a concrete join or filter scenario for this column?"

If the only justification is "it will probably be useful someday" — don't add it.

## Index by Table Write Frequency

| Table type | Load pattern | Index impact |
|-----------|-------------|-------------|
| Fact table | Daily batch | ~10 indexes have negligible cost |
| Streaming fact | Thousands of rows/second | Each index degrades write performance |

Always factor the table's actual loading pattern into the indexing decision.

## Anti-patterns

- **Speculative indexes** — "maybe someone will filter on this" — go unused but cost every write
- **Early indexes before full schema** — miss critical join paths not yet visible

## Related

- [[kimball-dimensional-modeling-case-study-baylas-2026]] — `source`
- [[medallion-architecture-raw-cleansed-dimensional]] — dimensional layer where indexes are applied
