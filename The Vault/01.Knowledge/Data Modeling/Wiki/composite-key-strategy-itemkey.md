---
created: 2026-07-27
source: "Advanced Dimensional Modeling for Retail Product Variants"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-b4e6c1743382"
note_type: pattern
tags: [product-dimension, composite-key, itemkey, star-schema]
---

# Composite Key Strategy (CONCAT-based ItemKey)

A key design pattern that generates a single, unique ItemKey for every row in a product dimension — handling both simple products and variant products in one unified string.

## Purpose

Fact tables in a star schema join to dimension tables on a single key. But a retail dimension must serve both simple products (no variants) and variant products (with Colour/Style/Size/Config). The ItemKey pattern resolves this by encoding variant attributes directly into the key string, making it deterministic and unique across both product types.

## Components

- `InventTable` — source for simple products
- `InventDimCombination` — source for variant products
- `InventDim` — source for dimensional attribute values
- CONCAT / ISNULL — build the key string with NULL → empty string handling

## Structure

```sql
-- Variant product key (includes all dimensions)
CONCAT(dataareaid, '_', itemid, inventcolorid, inventstyleid, inventsizeid, configid)
-- Example: "USMF_T00123_RED_CLASSIC_M_"

-- Simple product key (no variants)
CONCAT(dataareaid, '_', itemid)
-- Example: "USMF_D00456"
```

**Key principles:**
- ISNULL(attribute, '') is used throughout — NULL variant attributes become empty strings, maintaining key structure
- The trailing underscore pattern helps visually separate itemid from variant attributes in the key

## Example

```sql
SELECT
  CONCAT(
    id.dataareaid, '_',
    idc.itemid,
    id.inventcolorid,
    id.inventstyleid,
    id.inventsizeid,
    id.configid
  ) AS ItemKey,
  idc.itemid,
  ISNULL(producttrans.name, '') AS ItemName,
  ISNULL(id.inventcolorid, '') AS Color,
  ISNULL(id.inventstyleid, '') AS Style,
  ISNULL(id.inventsizeid, '') AS Size,
  ISNULL(id.configid, '') AS Config
FROM [dbo].inventdimcombination idc
LEFT JOIN [dbo].inventdim id ON id.inventdimid = idc.inventdimid
...
```

## Variations

- **Fixed-width padding**: Some implementations zero-pad or space-pad attribute columns to fixed lengths for deterministic substring extraction
- **Hash surrogate key**: Some teams use a hash of the CONCAT string as the surrogate key, storing the readable key as a business key column

## Related

- [[simple-vs-variant-products]] — the two product types this key unifies
- [[conditional-joins-case-concat-matching]] — how this key is used to join to pricing
