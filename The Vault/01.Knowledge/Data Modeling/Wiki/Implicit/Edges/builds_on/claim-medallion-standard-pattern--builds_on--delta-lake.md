---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[claim-medallion-standard-pattern]]"
target_node: "[[delta-lake]]"
weight: 1
---

# Medallion is Standard Delta Lake Pattern builds_on Delta Lake

<!-- Delta Lake provides the ACID transaction layer that enables reliable medallion architecture reprocessing. -->

## Edge

`[[claim-medallion-standard-pattern]]` -- **builds_on** -> `[[delta-lake]]`

## Evidence

Delta Lake provides the ACID transaction layer that enables reliable medallion architecture reprocessing.


## Related

- [[claim-medallion-standard-pattern]]
- [[delta-lake]]
