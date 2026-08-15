---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[medallion-architecture]]"
target_node: "[[data-vault]]"
weight: 1
---

# Medallion Architecture builds_on Data Vault

<!-- Data Vault always requires a dimensional presentation layer on top since it is not suitable for direct business user consumption. -->

## Edge

`[[medallion-architecture]]` -- **builds_on** -> `[[data-vault]]`

## Evidence

Data Vault always requires a dimensional presentation layer on top since it is not suitable for direct business user consumption.


## Related

- [[medallion-architecture]]
- [[data-vault]]
