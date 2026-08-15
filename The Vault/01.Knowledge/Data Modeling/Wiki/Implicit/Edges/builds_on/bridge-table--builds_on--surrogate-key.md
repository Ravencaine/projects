---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[bridge-table]]"
target_node: "[[surrogate-key]]"
weight: 1
---

# Bridge Table builds_on Surrogate Key

<!-- Bridge tables use surrogate keys on both sides of the bridge to enable clean single-column joins instead of multi-column predicates. -->

## Edge

`[[bridge-table]]` -- **builds_on** -> `[[surrogate-key]]`

## Evidence

Bridge tables use surrogate keys on both sides of the bridge to enable clean single-column joins instead of multi-column predicates.


## Related

- [[bridge-table]]
- [[surrogate-key]]
