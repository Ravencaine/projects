---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, performance, Data Modeling]
---

# Pre-Denormalize Metrics at Load Time

<!-- Denormalize metric components that change per transaction and are used in over 80% of queries directly into the fact table at load time, not at query time. -->

## Claim

Denormalize metric components that change per transaction and are used in over 80% of queries directly into the fact table at load time, not at query time.
