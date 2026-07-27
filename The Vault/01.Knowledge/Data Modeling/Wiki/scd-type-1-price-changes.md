---
created: 2026-07-27
source: "Advanced Dimensional Modeling for Retail Product Variants Pt 3"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-pt-3-d02abbc97319"
note_type: pattern
tags: [scd, type-1, slowly-changing-dimension, price-history]
---

# SCD Type 1 (Price Changes Overwrite)

A slowly changing dimension pattern where price changes overwrite the previous value — the ItemKey remains stable but the price attribute updates in place.

## Purpose

In SCD Type 1, when an attribute changes (e.g., RetailPrice changes from $19.99 to $24.99), the new value overwrites the old one. There is no history preserved. This is appropriate for pricing data in a product dimension: you want the current price, not the historical price trail (historical prices live in PriceDiscTable, not the dimension).

## Structure

```
ItemKey="USMF_T00123_RED"
2024-01-01: RetailPrice = 19.99
2024-02-01: RetailPrice = 24.99   ← overwrites (no historical row added)
```

The dimension row for `USMF_T00123_RED` is updated in place. Any fact rows pointing to that ItemKey now "see" the new price when joined.

## When to Use SCD Type 1

- Pricing and cost
- Product descriptions and names
- Any attribute where only the current value is relevant for analysis
- Appropriate for: dimension tables where history is stored in type-2 rows or source systems, not in the dimension itself

## When NOT to Use SCD Type 1

- Attributes where historical assignment matters (e.g., which sales rep served a customer at time of sale)
- Regulatory or audit requirements

## Related

- [[role-playing-dimension]] — same dimension used in different roles
- [[degenerate-dimension-barcode-in-fact]] — barcode stored redundantly for performance
