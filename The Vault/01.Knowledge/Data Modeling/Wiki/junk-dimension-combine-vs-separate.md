---
created: 2026-08-06
updated: 2026-08-06
source: Building a Data Warehouse from Scratch A Case Study in Kimball Modeling.md
note_type: pattern
tags: [data-warehouse, dimensional-modeling, junk-dimension, dimension-table, kimball]
---

# Junk Dimension — Combine vs Separate Decision

A junk dimension combines multiple low-cardinality, related attributes into a single dimension table instead of separate tables. Use it when attributes are queried together and none will be used independently across fact tables.

## Decision Criteria

| Combine into junk dimension | Keep as separate dimension |
|---|---|
| Attributes always filtered together | Any attribute will be filtered independently |
| None reused across multiple fact tables | Attribute is a conformed dimension (e.g., date, location) |
| Single join improves query performance | Attribute needs to join to different fact tables |

## Gut-Check Question

> "Is there any reporting scenario where someone would want to filter on one of these attributes without the others?"

If no — combine. If yes — keep separate.

## Examples

**Combine:** `event_type + category + sub_category + infrastructure + work_qualification` — analysts almost always filter on all of these together ("critical-category fiber events"). Four separate tables means four joins per query; one junk dimension means one.

**Keep separate:** Date dimension, location dimension, customer dimension — these are universal and reused across every fact table. Never bury conformed dimensions in a junk dimension.

## Related

- [[bridge-tables-many-to-many-list-unpivoting]] — another dimensional modeling pattern
- [[kimball-dimensional-modeling-case-study-baylas-2026]] — `source`
