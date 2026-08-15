---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: contradicts
tags: [Data Modeling, implicit-edge, contradicts]
source_node: "[[column-pruning-bravo]]"
target_node: "[[composite-key-strategy-itemkey]]"
weight: 1
---

# Column Pruning with Bravo for Power BI contradicts Composite Key Strategy (CONCAT-based ItemKey)

<!-- Bravo flags surrogate/composite keys as unused candidates for removal, but the composite ItemKey pattern depends on those columns staying in the model for joins. -->

## Edge

`[[column-pruning-bravo]]` -- **contradicts** -> `[[composite-key-strategy-itemkey]]`

## Evidence

Bravo flags surrogate/composite keys as unused candidates for removal, but the composite ItemKey pattern depends on those columns staying in the model for joins.


## Related

- [[column-pruning-bravo]]
- [[composite-key-strategy-itemkey]]
