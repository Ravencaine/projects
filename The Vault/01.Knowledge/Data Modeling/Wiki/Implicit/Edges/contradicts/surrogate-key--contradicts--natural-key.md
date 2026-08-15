---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: contradicts
tags: [Data Modeling, implicit-edge, contradicts]
source_node: "[[surrogate-key]]"
target_node: "[[natural-key]]"
weight: 1
---

# Surrogate Key contradicts Natural Key

<!-- For high-volume fact tables, natural keys are preferred over surrogate keys to avoid join overhead -->

## Edge

`[[surrogate-key]]` -- **contradicts** -> `[[natural-key]]`

## Evidence

For high-volume fact tables, natural keys are preferred over surrogate keys to avoid join overhead


## Related

- [[surrogate-key]]
- [[natural-key]]
