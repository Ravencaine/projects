---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[surrogate-key]]"
target_node: "[[fact-table]]"
weight: 1
---

# Surrogate Key builds_on Fact Table

<!-- Fact tables should always use integer surrogate keys as foreign keys, never multi-column string composites, for memory efficiency and join performance. -->

## Edge

`[[surrogate-key]]` -- **builds_on** -> `[[fact-table]]`

## Evidence

Fact tables should always use integer surrogate keys as foreign keys, never multi-column string composites, for memory efficiency and join performance.


## Related

- [[surrogate-key]]
- [[fact-table]]
