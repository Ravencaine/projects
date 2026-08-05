---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, supply-chain, fulfillment, order, shipping]
---

# Order Fulfillment Analysis in DAX

Comprehensive order fulfillment analysis: what was ordered, what shipped, what arrived, and where discrepancies occurred.

## Components

### Lines Fulfilled

```dax
Lines Fulfilled =
    COUNTROWS(
        FILTER(
            'OrderLines',
            'OrderLines'[Status] = "Shipped"
        )
    )
```

### Backorder Rate

```dax
Backorder Rate =
    DIVIDE(
        COUNTROWS( FILTER( 'OrderLines', 'OrderLines'[Status] = "Backordered" ] ),
        COUNTROWS( 'OrderLines' ),
        0
    )
```

### Fill Rate (Percentage of Order Fulfilled on First Shipment)

```dax
Fill Rate =
    DIVIDE(
        COUNTROWS( FILTER( 'OrderLines', 'OrderLines'[LinesFilledFirst] = TRUE ) ),
        COUNTROWS( 'OrderLines' ),
        0
    )
```

### Perfect Order Rate

```dax
Perfect Order Rate =
    DIVIDE(
        COUNTROWS(
            FILTER(
                'Orders',
                'Orders'[OnTime] = TRUE
                && 'Orders'[InFull] = TRUE
                && 'Orders'[ErrorFree] = TRUE
            )
        ),
        COUNTROWS( 'Orders' ),
        0
    )
```

## Related

- [[on-time-in-full-otif-dax]] — OTIF metric
- [[order-cycle-time-oct-dax]] — delivery timing
- [[delivery-date-accuracy-dax]] — promise vs actual
