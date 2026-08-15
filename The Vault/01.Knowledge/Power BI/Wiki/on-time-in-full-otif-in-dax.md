---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, operations, otif, supply-chain, fulfillment]
note_type: pattern

---

# On Time In Full (OTIF) in DAX

Measuring whether orders were fulfilled with the full quantities at the expected times.

## Formula

```
OTIF = ( Orders On Time AND In Full / Total Orders ) * 100
```

## DAX Pattern

```dax
Total Orders := COUNTROWS( 'Orders' )

On Time AND In Full :=
COUNTROWS(
    FILTER(
        'Orders',
        'Orders'[DeliveredQty] >= 'Orders'[OrderedQty]
        && 'Orders'[DeliveryDate] <= 'Orders'[RequestedDate]
    )
)

OTIF % :=
DIVIDE( [On Time AND In Full], [Total Orders] )
```

## Notes

- OTIF is a critical supply chain KPI
- Requires: order qty, delivered qty, requested date, actual delivery date
- Segment by plant, region, or product category for root cause analysis

## Related

- [[inventory-turnover-in-dax]]
- [[order-fulfillment-in-dax]]
- [[stock-out-analysis-in-dax]]
