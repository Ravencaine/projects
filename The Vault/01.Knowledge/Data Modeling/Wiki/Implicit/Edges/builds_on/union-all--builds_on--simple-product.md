---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[union-all]]"
target_node: "[[simple-product]]"
weight: 1
---

# UNION ALL builds_on Simple Product

<!-- The UNION ALL pattern combines simple product rows from InventTable with variant product rows from InventDimCombination into a unified dimension. -->

## Edge

`[[union-all]]` -- **builds_on** -> `[[simple-product]]`

## Evidence

The UNION ALL pattern combines simple product rows from InventTable with variant product rows from InventDimCombination into a unified dimension.


## Related

- [[union-all]]
- [[simple-product]]
