---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: contradicts
tags: [Data Modeling, implicit-edge, contradicts]
source_node: "[[cetas]]"
target_node: "[[performance-degradation-over-time]]"
weight: 1
---

# CETAS (Create External Table As Select) contradicts Performance Degradation From Growth and Stale Statistics

<!-- CETAS materialization contradicts on-demand view execution by pre-computing dimensions to prevent degradation. -->

## Edge

`[[cetas]]` -- **contradicts** -> `[[performance-degradation-over-time]]`

## Evidence

CETAS materialization contradicts on-demand view execution by pre-computing dimensions to prevent degradation.


## Related

- [[cetas]]
- [[performance-degradation-over-time]]
