---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[fact-table]]"
target_node: "[[surrogate-key]]"
weight: 1
---

# Fact Table builds_on Surrogate Key

<!-- Fact tables typically use surrogate keys from dimension tables as foreign keys -->

## Edge

`[[fact-table]]` -- **builds_on** -> `[[surrogate-key]]`

## Evidence

Fact tables typically use surrogate keys from dimension tables as foreign keys


## Related

- [[fact-table]]
- [[surrogate-key]]
