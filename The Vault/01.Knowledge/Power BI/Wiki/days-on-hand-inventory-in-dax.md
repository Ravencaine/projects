---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "operations", "inventory", "days-on-hand"]
note_type: pattern

---

# Days on Hand Inventory in DAX

Measuring how many days of inventory are available at current consumption rates.

## Formula

```
Days on Hand = Current Inventory / ( COGS / 365 )
```

## DAX Pattern

```dax
Days on Hand :=
DIVIDE(
    SUM( 'Inventory'[CurrentStock] ),
    DIVIDE( SUM( 'Inventory'[COGS] ), 365 )
)
```

## By Product Category

```dax
Days on Hand by Category :=
SUMMARIZECOLUMNS(
    'Product'[Category],
    "DaysOnHand",
    DIVIDE( SUM( 'Inventory'[CurrentStock] ), DIVIDE( SUM( 'Inventory'[COGS] ), 365 ) )
)
```

## Notes

- Target days on hand varies by product type (perishables vs. durable goods)
- Days on Hand above target = overstocking
- Days on Hand below target = risk of stock-outs

## Related

- [[inventory-turnover-in-dax]]
- [[stock-out-analysis-in-dax]]
