---
created: 2026-07-27
source: "Advanced Dimensional Modeling for Retail Product Variants Pt 2"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-pt-2-efd14c680c3c"
note_type: pattern
tags: [pricing, row-number, deduplication, cte, d365, pricedisctable]
---

# Pricing CTE with ROW_NUMBER Deduplication

A CTE pattern that isolates PriceDiscTable rows per item and picks a deterministic single price using ROW_NUMBER — required because PriceDiscTable accumulates price history (effective date ranges) and overlapping agreements.

## Purpose

PriceDiscTable can have multiple active price records per item/variant simultaneously: a current price, a future price, and historical prices. Without deduplication, a variant could return multiple price rows, breaking the dimension. The CTE pattern partitions by item, orders by fromdate, and picks the latest applicable price.

## Components

- `PriceDiscTable` — source of pricing data
- `InventDim` — source of dimension attributes on the price record
- `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)` — deduplication window function
- `module` filter (1 = Sales/Retail, 2 = Purchase/Cost)
- Date validity: `(todate = '1900-01-01' OR todate > GETDATE()) AND fromdate <= GETDATE()`

## Structure

```sql
pricediscpurch AS (
  SELECT
    pricediscpurch.*,
    ROW_NUMBER() OVER (
      PARTITION BY CONCAT(pricediscpurch.dataareaid, pricediscpurch.itemrelation)
      ORDER BY pricediscpurch.fromdate
    ) AS seqnum,
    ISNULL(id.inventcolorid, '') AS inventcolorid,
    ISNULL(id.inventstyleid, '') AS inventstyleid,
    ISNULL(id.inventsizeid, '')  AS inventsizeid,
    ISNULL(id.configid, '')      AS configid
  FROM [dbo].pricedisctable pricediscpurch
  LEFT JOIN [dbo].inventdim id
    ON id.inventdimid = pricediscpurch.inventdimid
    AND id.dataareaid = pricediscpurch.dataareaid
  WHERE
    module = 2                                        -- Purchase prices (cost)
    AND (todate = '1900-01-01' OR todate > GETDATE()) -- Active prices only
    AND fromdate <= GETDATE()
)
```

Then in the final query: `WHERE seqnum = 1` to get one price per item.

## Why ISNULL?

The `inventdimid` on PriceDiscTable may be NULL (item-level price, not variant-level). LEFT JOIN + ISNULL converts NULL dimensions to empty strings, keeping the CONCAT-based match key consistent and preventing NULL propagation.

## Related

- [[conditional-joins-case-concat-matching]] — how the deduplicated prices are then joined to variants
- [[composite-key-strategy-itemkey]] — the CONCAT key pattern shared across both patterns
