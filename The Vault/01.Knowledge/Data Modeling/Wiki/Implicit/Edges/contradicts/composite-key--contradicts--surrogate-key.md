---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: contradicts
tags: [Data Modeling, implicit-edge, contradicts]
source_node: "[[composite-key]]"
target_node: "[[surrogate-key]]"
weight: 1
---

# Composite Key contradicts Surrogate Key

<!-- Surrogate keys replace composite keys for fact-dimension joins, consuming 4 bytes per row vs up to 240 bytes for multi-column string composites. -->

## Edge

`[[composite-key]]` -- **contradicts** -> `[[surrogate-key]]`

## Evidence

Surrogate keys replace composite keys for fact-dimension joins, consuming 4 bytes per row vs up to 240 bytes for multi-column string composites.


## Related

- [[composite-key]]
- [[surrogate-key]]
