---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: contradicts
tags: [Data Modeling, implicit-edge, contradicts]
source_node: "[[consolidated-fact-tables]]"
target_node: "[[duplicated-dimensions]]"
weight: 1
---

# Consolidated Fact Tables Anti-Pattern contradicts Duplicated Dimensions Per Fact Table Anti-Pattern

<!-- Consolidated fact tables contradict the approach of keeping fact tables separate with shared dimensions, while both are anti-patterns for multi-fact scenarios. -->

## Edge

`[[consolidated-fact-tables]]` -- **contradicts** -> `[[duplicated-dimensions]]`

## Evidence

Consolidated fact tables contradict the approach of keeping fact tables separate with shared dimensions, while both are anti-patterns for multi-fact scenarios.


## Related

- [[consolidated-fact-tables]]
- [[duplicated-dimensions]]
