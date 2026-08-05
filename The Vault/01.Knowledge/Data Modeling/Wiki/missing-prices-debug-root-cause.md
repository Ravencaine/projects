---
created: 2026-07-27
updated: 2026-08-02
source: "Advanced Dimensional Modeling for Retail Product Variants Pt 3"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-pt-3-d02abbc97319"
note_type: error
tags: [missing-price, debug, d365, pricedisctable, dimension-group]
---

# Missing Prices (Debug + Root Cause)

Symptom: a variant row exists in the dimension but RetailPrice = 0 or NULL. The variant is valid but has no matching price record.

## Error / Symptom

```
ItemKey: USMF_T00123_RED_MODERN_M_
ItemID:  T00123
Color:   Red
Style:   Modern
Size:    M
DimensionGroup: Donated
RetailPrice: 0   ← should be 19.99
```

## Cause

The price record in PriceDiscTable does not match the variant's dimensional attributes exactly. Common causes:

1. **Price set at item level, not variant level**: PriceDiscTable.inventdimid is NULL; the price covers the item but the dimension join requires a variant-level price
2. **Price dimensions don't match the dimension group**: e.g., a DonatedNS product has a price keyed on Colour+Style+Size, but only Colour+Style should be matched
3. **Price has expired**: todate is in the past; the active date filter excludes it
4. **Wrong module**: price record is module=2 (Purchase) but you're joining for Sales/Retail

## Solution

```sql
-- Debug query: find variants without prices
SELECT
  v.ItemKey,
  v.ItemID,
  v.Color,
  v.Style,
  v.Size,
  pg.name AS DimensionGroup
FROM ProductVariants v
LEFT JOIN EcoResProductDimensionGroup pg ON ...
LEFT JOIN PriceDiscSales p
  ON v.ItemID = p.itemrelation
  AND v.Color = p.inventcolorid
  AND v.Style = p.inventstyleid
  AND v.Size = p.inventsizeid
WHERE v.RetailPrice = 0 OR v.RetailPrice IS NULL;
```

**Fix steps:**
1. Confirm the dimension group in D365 F&O for the affected item
2. Check PriceDiscTable for the item: does a price record exist at item level or variant level?
3. Verify the todate is either '1900-01-01' (permanent) or future-dated
4. Confirm module = 1 for retail/sales prices

## Prevention

- Build price validation into the ETL pipeline: count variants vs matched prices, alert if match rate drops below threshold
- Log the dimension group name alongside the item in the dimension for easier debugging

## Related Errors

- [[duplicate-barcodes-retailshowforitem-filter]] — another PriceDiscTable join issue
- [[performance-degradation-over-time]] — price history accumulation can mask missing prices
