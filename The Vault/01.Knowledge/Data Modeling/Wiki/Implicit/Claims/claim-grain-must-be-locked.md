---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, fact-table, Data Modeling]
---

# Grain Must Be Locked First

<!-- The fact table grain must be defined and locked with a UNIQUE constraint before any other design decisions; mixed grain causes silent double-counting. -->

## Claim

The fact table grain must be defined and locked with a UNIQUE constraint before any other design decisions; mixed grain causes silent double-counting.
