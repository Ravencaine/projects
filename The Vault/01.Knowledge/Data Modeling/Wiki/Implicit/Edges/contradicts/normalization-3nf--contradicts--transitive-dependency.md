---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: contradicts
tags: [Data Modeling, implicit-edge, contradicts]
source_node: "[[normalization-3nf]]"
target_node: "[[transitive-dependency]]"
weight: 1
---

# Normalization and 3NF contradicts Transitive Dependency

<!-- 3NF is violated by transitive dependencies where non-key fields depend on other non-key fields. -->

## Edge

`[[normalization-3nf]]` -- **contradicts** -> `[[transitive-dependency]]`

## Evidence

3NF is violated by transitive dependencies where non-key fields depend on other non-key fields.


## Related

- [[normalization-3nf]]
- [[transitive-dependency]]
