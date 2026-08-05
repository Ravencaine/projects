---
created: 2026-07-27
updated: 2026-08-02
source: "Advanced Dimensional Modeling for Retail Product Variants Pt 3"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-pt-3-d02abbc97319"
note_type: pattern
tags: [index, filtered-index, barcode, performance, azure-synapse]
---

# Index Strategy (Filtered Index on Barcode)

Index design pattern for product dimensions: standard indexes on join keys, plus a filtered (conditional) index on Barcode that excludes empty strings.

## Purpose

Fact-to-dimension joins on ItemKey and itemid/dataareaid happen on every query. Barcode lookups (from POS scan → dimension) are also common but only for rows with an actual barcode. A filtered index on non-empty barcodes reduces index size and improves scan performance for barcode-based joins.

## Structure

```sql
-- Primary join key index
CREATE INDEX idx_itemkey ON DIM_AllItems(ItemKey);

-- item lookup index (covers dataareaid + itemid for direct item lookups)
CREATE INDEX idx_itemid ON DIM_AllItems(itemid, dataareaid);

-- Filtered barcode index (excludes empty strings)
CREATE INDEX idx_barcode
  ON DIM_AllItems(Barcode)
  WHERE Barcode != '';
```

## Why Filter on Barcode?

A barcode column on a product dimension will have many empty-string values (simple products, discontinued variants). Indexing empty strings wastes space and degrades the seek for real barcode lookups. The filtered index excludes these rows entirely, keeping the index compact and the seek fast.

## Related

- [[materialized-views-vs-regular-views-cetas]] — pre-computation strategy that pairs with indexing
- [[missing-prices-debug-root-cause]] — related debugging pattern
