---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[star-schema]]"
target_node: "[[date-table]]"
weight: 1
---

# Star Schema builds_on Date Dimension Table

<!-- Star schema includes a dedicated date dimension table to support time intelligence across all fact tables. -->

## Edge

`[[star-schema]]` -- **builds_on** -> `[[date-table]]`

## Evidence

Star schema includes a dedicated date dimension table to support time intelligence across all fact tables.


## Related

- [[star-schema]]
- [[date-table]]
