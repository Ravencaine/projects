---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, supply-chain, order-cycle, lead-time, metric]
---

# Order Cycle Time (OCT) in DAX

The elapsed time from order placement to order receipt/fulfillment.

## Formula

```
OCT = Date Received - Date Ordered
```

## DAX Pattern

```dax
Order Cycle Time (Days) =
    AVERAGEX(
        'Orders',
        DATEDIFF( 'Orders'[OrderDate], 'Orders'[ReceivedDate], DAY )
    )
```

## Variations

| OCT Type | Definition |
|----------|------------|
| Order to Ship | Days from order to shipment |
| Order to Delivery | Days from order to customer receipt |
| Order to Promise | Actual vs promised delivery |
| Manufacturing Cycle | Days from production start to finish |

## Related

- [[on-time-in-full-otif-dax]] — OTIF delivery metric
- [[delivery-date-accuracy-dax]] — on-time delivery vs promise
- [[order-fulfillment-dax]] — full fulfillment analysis
