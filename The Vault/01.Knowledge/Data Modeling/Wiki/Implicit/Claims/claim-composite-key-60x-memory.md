---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, surrogate-key, Data Modeling]
---

# Composite Keys Consume ~60x More Memory Than Surrogate Keys

<!-- A 6-column NVARCHAR composite key at 20 characters per column consumes approximately 240 bytes per row vs 4 bytes for an integer surrogate key. At 1 million rows this is 240 MB vs 4 MB. -->

## Claim

A 6-column NVARCHAR composite key at 20 characters per column consumes approximately 240 bytes per row vs 4 bytes for an integer surrogate key. At 1 million rows this is 240 MB vs 4 MB.
