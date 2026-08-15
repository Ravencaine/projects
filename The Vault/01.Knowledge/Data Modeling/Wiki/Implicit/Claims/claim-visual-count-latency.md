---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, performance, Data Modeling]
---

# Visual Count Per Page Causes Latency

<!-- Every visual fires its own DAX query on filter change; 20 visuals with 2-second queries can cause 40 seconds of per-interaction latency. -->

## Claim

Every visual fires its own DAX query on filter change; 20 visuals with 2-second queries can cause 40 seconds of per-interaction latency.
