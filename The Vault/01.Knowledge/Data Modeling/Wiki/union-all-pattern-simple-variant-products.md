---
created: 2026-07-27
source: "Advanced Dimensional Modeling for Retail Product Variants Pt 2"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-pt-2-efd14c680c3c"
note_type: pattern
tags: [union-all, simple-product, variant-product, product-dimension, sql]
---

# UNION ALL Pattern (Simple + Variant Products)

A SQL pattern that combines rows from simple products and variant products into a single unified dimension result set — using UNION ALL (not UNION) for performance.

## Purpose

Simple products and variant products have different source tables and different join logic. The UNION ALL pattern brings both result sets into one dimension table with a consistent schema: one ItemKey column, one ItemName, one RetailPrice, and variant attribute columns that are populated for variants and empty for simple products.

## Components

- `InventDimCombination` → variant products (via ProductVariants CTE)
- `InventTable` → simple products
- `UNION ALL` — combines both result sets without deduplication overhead
- Subquery filter: `WHEN t1.itemid IN (SELECT itemid FROM ProductVariants) THEN 0` — marks simple products that have variants with RetailPrice = 0 (price is at variant level, not item level)

## Structure

```sql
SELECT DISTINCT
  t1.*,
  GETDATE() AS RefreshDate
FROM (
  -- Branch 1: Variant Products
  SELECT
    ItemKey, itemid, dataareaid, ItemName,
    RetailPrice, CostPerPiece,
    [Type], SubType,
    Color, Style, Size, Config,
    Multiples, Stopped, Barcode
  FROM ProductVariants

  UNION ALL

  -- Branch 2: Simple Products
  SELECT
    CONCAT(t1.dataareaid, '_', t1.itemid) AS ItemKey,
    t1.itemid,
    t1.dataareaid,
    ISNULL(producttrans.name, '') AS ItemName,
    CASE
      WHEN t1.itemid IN (SELECT itemid FROM ProductVariants) THEN 0
      ELSE (SELECT TOP 1 amount FROM [dbo].pricedisctable
            WHERE itemrelation = t1.itemid AND module = 1
            AND (todate = '1900-01-01' OR todate > GETDATE()))
    END AS RetailPrice,
    '' AS Color, '' AS Style, '' AS Size, '' AS Config,
    ...
  FROM [dbo].inventtable t1
) t1;
```

## UNION ALL vs UNION

- **UNION ALL**: Faster — no deduplication sort; we already guarantee no overlap via the subquery filter
- **UNION**: Removes duplicates (expensive sort) — unnecessary here

## Related

- [[composite-key-strategy-itemkey]] — the key generated in both branches
- [[simple-vs-variant-products]] — the two product types this pattern combines
