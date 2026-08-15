---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: contradicts
tags: [Data Modeling, implicit-edge, contradicts]
source_node: "[[duplicated-dimensions]]"
target_node: "[[consolidated-fact-tables]]"
weight: 1
---

# Duplicated Dimensions Per Fact Table Anti-Pattern contradicts Consolidated Fact Tables Anti-Pattern

<!-- Duplicating dimensions per fact table contradicts shared dimension design while stacking fact tables also represents a misdesign. -->

## Edge

`[[duplicated-dimensions]]` -- **contradicts** -> `[[consolidated-fact-tables]]`

## Evidence

Duplicating dimensions per fact table contradicts shared dimension design while stacking fact tables also represents a misdesign.


## Related

- [[duplicated-dimensions]]
- [[consolidated-fact-tables]]
