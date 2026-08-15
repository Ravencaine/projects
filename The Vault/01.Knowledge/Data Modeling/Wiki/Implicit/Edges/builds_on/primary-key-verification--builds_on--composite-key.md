---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[primary-key-verification]]"
target_node: "[[composite-key]]"
weight: 1
---

# Primary Key Verification builds_on Composite Key

<!-- If single-column key fails uniqueness test, composite key should be tested -->

## Edge

`[[primary-key-verification]]` -- **builds_on** -> `[[composite-key]]`

## Evidence

If single-column key fails uniqueness test, composite key should be tested


## Related

- [[primary-key-verification]]
- [[composite-key]]
