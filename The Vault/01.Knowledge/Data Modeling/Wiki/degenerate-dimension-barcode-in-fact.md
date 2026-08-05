---
created: 2026-07-27
updated: 2026-08-02
source: "Advanced Dimensional Modeling for Retail Product Variants Pt 3"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-pt-3-d02abbc97319"
note_type: pattern
tags: [degenerate-dimension, barcode, fact-table, performance, star-schema]
---

# Degenerate Dimension (Barcode in Fact)

A dimensional modelling pattern where a low-cardinality attribute (Barcode) is stored directly in the fact table rather than in a separate dimension — for scan-speed performance at the cost of some denormalisation.

## Purpose

Barcode is technically a product attribute — it belongs in the product dimension. But POS systems scan barcodes directly at transaction time. Storing the barcode in the fact table enables:
- Single-table barcode lookup (no join needed for real-time scan)
- Simplified ETL from POS source systems (barcode already in the transaction feed)

This is a deliberate trade-off: slightly larger fact table storage, but faster scan-path queries.

## Structure

```sql
-- Fact table has Barcode as a degenerate dimension
SELECT
  f.Barcode,          -- degenerate (in fact for quick lookup)
  dim.ItemName,       -- dimension attribute
  dim.RetailPrice
FROM FactSales f
LEFT JOIN DimProducts dim ON dim.Barcode = f.Barcode;
```

The Barcode is both a fact table column and a dimension attribute — hence "degenerate" dimension.

## When to Use

- Barcode or transaction reference numbers used in both source feeds and dimension lookups
- High-frequency, latency-sensitive scan paths where join cost is unacceptable
- Appropriate when the attribute doesn't change frequently (no SCD concerns)

## Related

- [[scd-type-1-price-changes]] — SCD pattern for the product dimension
- [[role-playing-dimension]] — same dimension table used in multiple roles
