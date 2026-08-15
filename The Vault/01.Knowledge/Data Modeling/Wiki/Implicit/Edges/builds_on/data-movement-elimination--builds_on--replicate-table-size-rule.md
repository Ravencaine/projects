---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[data-movement-elimination]]"
target_node: "[[replicate-table-size-rule]]"
weight: 1
---

# Replicated Tables Eliminate Data Movement builds_on Replicate Works for Dimensions Under 2GB Per Node

<!-- The 2GB per node rule of thumb determines when replicated distribution is appropriate -->

## Edge

`[[data-movement-elimination]]` -- **builds_on** -> `[[replicate-table-size-rule]]`

## Evidence

The 2GB per node rule of thumb determines when replicated distribution is appropriate


## Related

- [[data-movement-elimination]]
- [[replicate-table-size-rule]]
