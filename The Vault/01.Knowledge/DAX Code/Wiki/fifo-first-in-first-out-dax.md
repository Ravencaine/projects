---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, inventory, fifo, costing, accounting]
---

# FIFO Inventory Costing in DAX

First In, First Out inventory valuation — consuming the oldest inventory first.

## Concept

FIFO assigns costs based on purchase order sequence: the first items received are the first consumed. When inventory layers are partially consumed, the cost is prorated.

## Key Pattern

```dax
FIFO Cost =
    VAR __RequiredQty = [RequiredQty]
    VAR __Layers =
        FILTER(
            'PurchaseOrders',
            'PurchaseOrders'[Item] = [Item]
            && 'PurchaseOrders'[RemainingQty] > 0
        )
        ORDERBY( 'PurchaseOrders'[ReceivedDate], ASC )
    VAR __Result =
        SUMX(
            __Layers,
            VAR __FromThisLayer = MIN( __RequiredQty, [RemainingQty] )
            VAR __Cost = __FromThisLayer * [UnitCost]
            VAR __RequiredQty = __RequiredQty - __FromThisLayer
            RETURN __Cost
        )
    RETURN __Result
```

This iterates through purchase layers in date order, consuming each layer until the required quantity is satisfied.

## Related

- [[days-of-supply-dos-dax]] — inventory level metric
- [[order-cycle-time-oct-dax]] — supply chain timing metric
- [[order-fulfillment-dax]] — order processing patterns
