---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, data-modeling, Data Modeling]
---

# SCD at Wrong Granularity Causes Full In-Memory Recalculation

<!-- Joining fact tables to type-2 SCD dimension tables at the wrong granularity causes Power BI to recalculate the entire model in memory; the fix is using a surrogate key on every record so inactive SCD rows are never in the fact table. -->

## Claim

Joining fact tables to type-2 SCD dimension tables at the wrong granularity causes Power BI to recalculate the entire model in memory; the fix is using a surrogate key on every record so inactive SCD rows are never in the fact table.
