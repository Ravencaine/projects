---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, etl, Data Modeling]
---

# Unverified keys cause silent upsert overwrites

<!-- Using a column as an upsert key without verifying uniqueness results in silently overwriting the wrong source rows when duplicates exist. -->

## Claim

Using a column as an upsert key without verifying uniqueness results in silently overwriting the wrong source rows when duplicates exist.
