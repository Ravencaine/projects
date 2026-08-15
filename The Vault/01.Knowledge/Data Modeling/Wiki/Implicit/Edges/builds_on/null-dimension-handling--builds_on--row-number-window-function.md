---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[null-dimension-handling]]"
target_node: "[[row-number-window-function]]"
weight: 1
---

# ISNULL Converts NULL Dimensions to Empty Strings builds_on ROW_NUMBER() Window Function

<!-- ISNULL handling is a prerequisite for consistent key generation before ROW_NUMBER partitioning -->

## Edge

`[[null-dimension-handling]]` -- **builds_on** -> `[[row-number-window-function]]`

## Evidence

ISNULL handling is a prerequisite for consistent key generation before ROW_NUMBER partitioning


## Related

- [[null-dimension-handling]]
- [[row-number-window-function]]
