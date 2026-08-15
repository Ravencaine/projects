---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[d365-fo-dimension-groups]]"
target_node: "[[conditional-joins-case-concat-matching]]"
weight: 1
---

# D365 F&O Dimension Groups builds_on Conditional Joins via CASE/CONCAT Matching

<!-- The CASE/CONCAT join pattern is required because dimension groups dictate different matching column sets per row. -->

## Edge

`[[d365-fo-dimension-groups]]` -- **builds_on** -> `[[conditional-joins-case-concat-matching]]`

## Evidence

The CASE/CONCAT join pattern is required because dimension groups dictate different matching column sets per row.


## Related

- [[d365-fo-dimension-groups]]
- [[conditional-joins-case-concat-matching]]
