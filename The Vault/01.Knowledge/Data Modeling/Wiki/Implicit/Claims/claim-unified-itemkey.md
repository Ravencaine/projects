---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, key-design, Data Modeling]
---

# Unified ItemKey Handles Both Product Types

<!-- A product dimension must use one unified key pattern (CONCAT of dataareaid, itemid, and variant dimensions) so fact tables join without knowing whether the product has variants. -->

## Claim

A product dimension must use one unified key pattern (CONCAT of dataareaid, itemid, and variant dimensions) so fact tables join without knowing whether the product has variants.
