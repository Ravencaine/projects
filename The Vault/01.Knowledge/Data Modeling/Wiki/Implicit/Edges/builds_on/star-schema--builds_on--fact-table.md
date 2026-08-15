---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[star-schema]]"
target_node: "[[fact-table]]"
weight: 1
---

# Star Schema builds_on Fact Table

<!-- Star Schema organises one or more fact tables at the centre with dimension tables radiating outward via single-hop foreign key joins. -->

## Edge

`[[star-schema]]` -- **builds_on** -> `[[fact-table]]`

## Evidence

Star Schema organises one or more fact tables at the centre with dimension tables radiating outward via single-hop foreign key joins.


## Related

- [[star-schema]]
- [[fact-table]]
