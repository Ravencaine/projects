---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, performance, Data Modeling]
---

# Replicated Tables Eliminate Data Movement

<!-- When a fact table is hash-distributed, joining a dimension requires moving rows to fact nodes; replicated tables remove this shuffle by being present on all nodes. -->

## Claim

When a fact table is hash-distributed, joining a dimension requires moving rows to fact nodes; replicated tables remove this shuffle by being present on all nodes.
