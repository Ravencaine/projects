---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, bridge-table, Data Modeling]
---

# List Columns in Same Row Are Not Index-Parallel

<!-- When a source row contains multiple comma-separated list columns, they are often independent and not aligned by index; matching by index silently produces wrong results. -->

## Claim

When a source row contains multiple comma-separated list columns, they are often independent and not aligned by index; matching by index silently produces wrong results.
