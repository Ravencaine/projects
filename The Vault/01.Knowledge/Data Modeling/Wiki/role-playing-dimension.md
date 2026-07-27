---
created: 2026-07-27
source: "Advanced Dimensional Modeling for Retail Product Variants Pt 3"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-pt-3-d02abbc97319"
note_type: pattern
tags: [role-playing-dimension, date-dimension, product-dimension, conformed-dimension]
---

# Role-Playing Dimension

A dimensional modelling pattern where the same dimension table is joined to a fact table multiple times, each join giving the dimension a different role (meaning) in the query.

## Purpose

A single fact table may need the same dimension in different temporal or relational contexts. Rather than creating duplicate dimension tables, the same dimension is joined multiple times with different aliases. Date dimensions are the canonical example, but product dimensions can also be role-playing (e.g., Sold Product vs. Returned Product in a retail returns fact).

## Structure

```sql
-- Same DimProducts used twice with different meanings
SELECT
  f.SoldItemKey,
  f.ReturnedItemKey,
  sold.ItemName   AS SoldItemName,
  returned.ItemName AS ReturnedItemName,
  sold.RetailPrice AS SoldRetailPrice,
  returned.RetailPrice AS ReturnedRetailPrice
FROM FactSales f
LEFT JOIN DimProducts sold    ON sold.ItemKey   = f.SoldItemKey
LEFT JOIN DimProducts returned ON returned.ItemKey = f.ReturnedItemKey;
```

## Examples in Retail

| Role | Meaning |
|------|---------|
| Sold Product | The item in the original sale |
| Returned Product | The item being returned |
| Gift Item | A gift-with-purchase item |

## Related

- [[scd-type-1-price-changes]] — the SCD approach used within the shared dimension
- [[degenerate-dimension-barcode-in-fact]] — another dimension modelling pattern
