---
created: 2026-07-27
updated: 2026-08-02
source: "Advanced Dimensional Modeling for Retail Product Variants Pt 3"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-pt-3-d02abbc97319"
note_type: error
tags: [duplicate-barcode, retailshowforitem, inventitembarcode, d365]
---

# Duplicate Barcodes (retailshowforitem Filter)

Symptom: a barcode scan returns multiple rows in the dimension — a barcode that should be unique is returning duplicates.

## Error / Symptom

```
Barcode: 001234567890
→ Row 1: USMF_T00123_RED_CLASSIC_S_  (2024-01-01, historical)
→ Row 2: USMF_T00123_RED_CLASSIC_S_  (2024-06-01, current)
→ Row 3: USMF_T00123_RED_CLASSIC_S_  (2024-09-01, current)
```

Multiple rows returned per barcode scan in POS — violates the one-SKU-per-barcode expectation.

## Cause

InventItemBarcode contains barcode history and secondary barcode assignments per variant — not just the current primary barcode. Without filtering, all historical and secondary records are returned, causing duplicates.

## Solution

```sql
LEFT JOIN inventitembarcode bar
  ON bar.retailvariantid = idc.retailvariantid
  AND bar.retailshowforitem = 1  -- Primary barcode only
```

The `retailshowforitem = 1` filter ensures only the display barcode is returned, not historical or secondary barcodes.

## Prevention

Always filter on `retailshowforitem = 1` when joining InventItemBarcode. Add a UNIQUE constraint on (Barcode) in the dimension table if the data platform supports it — the constraint will surface duplicates during ETL rather than at query time.

## Related Errors

- [[missing-prices-debug-root-cause]] — another PriceDiscTable join correctness issue
- [[composite-key-strategy-itemkey]] — the key that links barcodes to variants
