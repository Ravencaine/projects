---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[countrows-vs-distinctcount]]"
target_node: "[[primary-key]]"
weight: 1
---

# COUNTROWS vs DISTINCTCOUNT QA builds_on Primary Key

<!-- COUNTROWS vs DISTINCTCOUNT requires a unique primary key column to accurately detect duplicate rows. -->

## Edge

`[[countrows-vs-distinctcount]]` -- **builds_on** -> `[[primary-key]]`

## Evidence

COUNTROWS vs DISTINCTCOUNT requires a unique primary key column to accurately detect duplicate rows.


## Related

- [[countrows-vs-distinctcount]]
- [[primary-key]]
