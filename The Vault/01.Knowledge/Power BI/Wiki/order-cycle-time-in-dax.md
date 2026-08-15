---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, operations, order-cycle, lead-time, supply-chain]
note_type: pattern

---

# Order Cycle Time in DAX

Measuring the time from order placement to order fulfillment.

## Formula

```
Order Cycle Time = Order Fulfillment Date - Order Placement Date
```

## DAX Pattern

```dax
Order Cycle Time (Days) :=
DATEDIFF(
    MIN( 'Orders'[OrderDate] ),
    MIN( 'Orders'[FulfillmentDate] ),
    DAY
)
```

## Notes

- Lower cycle time = faster fulfillment
- Segment by product category, customer region, or order size

## Related

- [[on-time-in-full-otif-dax]]
- [[order-fulfillment-in-dax]]
