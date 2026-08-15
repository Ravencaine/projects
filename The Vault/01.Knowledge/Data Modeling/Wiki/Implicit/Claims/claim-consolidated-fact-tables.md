---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, data-modeling, Data Modeling]
---

# Consolidated Fact Tables Anti-Pattern

<!-- Stacking multiple fact tables into one via append/union creates null keys wherever fact-specific dimensions do not apply, causing ambiguous grain, unexpected blanks in visuals, slow refresh, and complex measure logic. -->

## Claim

Stacking multiple fact tables into one via append/union creates null keys wherever fact-specific dimensions do not apply, causing ambiguous grain, unexpected blanks in visuals, slow refresh, and complex measure logic.
