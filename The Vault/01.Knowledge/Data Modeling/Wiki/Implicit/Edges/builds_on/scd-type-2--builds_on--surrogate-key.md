---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[scd-type-2]]"
target_node: "[[surrogate-key]]"
weight: 1
---

# SCD Type 2 builds_on Surrogate Key

<!-- SCD Type 2 requires a surrogate key on every dimension row (active and inactive versions) so that fact rows can join to the correct historical version at transaction time. -->

## Edge

`[[scd-type-2]]` -- **builds_on** -> `[[surrogate-key]]`

## Evidence

SCD Type 2 requires a surrogate key on every dimension row (active and inactive versions) so that fact rows can join to the correct historical version at transaction time.


## Related

- [[scd-type-2]]
- [[surrogate-key]]
