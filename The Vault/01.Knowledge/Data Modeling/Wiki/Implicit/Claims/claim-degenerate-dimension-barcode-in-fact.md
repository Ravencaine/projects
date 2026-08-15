---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, barcode, Data Modeling]
---

# Degenerate Dimension (Barcode in Fact)

<!-- A dimensional modelling pattern where a low-cardinality attribute (Barcode) is stored directly in the fact table rather than in a separate dimension - trading some denormalisation for faster scan-path queries in POS scenarios. -->

## Claim

A dimensional modelling pattern where a low-cardinality attribute (Barcode) is stored directly in the fact table rather than in a separate dimension - trading some denormalisation for faster scan-path queries in POS scenarios.
