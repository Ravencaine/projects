---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[bridge-table]]"
target_node: "[[fact-table]]"
weight: 1
---

# Bridge Table builds_on Fact Table

<!-- Bridge tables maintain the fact table grain (one event = one row) while adding the dimension relationship layer without duplicating fact rows. -->

## Edge

`[[bridge-table]]` -- **builds_on** -> `[[fact-table]]`

## Evidence

Bridge tables maintain the fact table grain (one event = one row) while adding the dimension relationship layer without duplicating fact rows.


## Related

- [[bridge-table]]
- [[fact-table]]
