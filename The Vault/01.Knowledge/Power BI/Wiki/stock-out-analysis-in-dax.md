---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, operations, stock-out, inventory]
note_type: pattern

---

# Stock-out Analysis in DAX

Identifying products and periods where inventory was exhausted.

## Definition

A stock-out occurs when demand cannot be fulfilled from available inventory.

## DAX Pattern

```dax
Is Stock-out :=
IF(
    SUM( 'Demand'[Qty] ) > SUM( 'Inventory'[Qty] ),
    1, 0
)

Lost Sales :=
SUMX(
    FILTER(
        'Demand',
        'Demand'[Qty] > LOOKUPVALUE( 'Inventory'[Qty], 'Inventory'[ProductID], 'Demand'[ProductID] )
    ),
    'Demand'[Qty] - LOOKUPVALUE( 'Inventory'[Qty], 'Inventory'[ProductID], 'Demand'[ProductID] )
)
```

## Notes

- Stock-out cost = Lost Sales + Lost Customer Goodwill
- Use for safety stock calculations
- Segment by product category and supplier for procurement insights

## Related

- [[inventory-turnover-in-dax]]
- [[days-on-hand-inventory-in-dax]]
- [[on-time-in-full-otif-dax]]
