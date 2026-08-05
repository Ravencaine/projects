---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, supply-chain, delivery, accuracy, promise]
---

# Delivery Date Accuracy in DAX

Measuring how accurately promised delivery dates match actual delivery dates.

## Formula

```
Delivery Accuracy = Orders Delivered On or Before Promised Date / Total Delivered Orders × 100
```

## DAX Pattern

```dax
Delivery Date Accuracy =
    VAR __OnTime =
        COUNTROWS(
            FILTER(
                'Deliveries',
                'Deliveries'[ActualDate] <= 'Deliveries'[PromisedDate]
            )
        )
    VAR __Total = COUNTROWS( 'Deliveries' )
    RETURN DIVIDE( __OnTime, __Total, 0 ) * 100
```

## Early vs Late Analysis

```dax
Delivery Variance (Days) =
    DATEDIFF( 'Deliveries'[PromisedDate], 'Deliveries'[ActualDate], DAY )
```

Positive = late, negative = early.

## Related

- [[on-time-in-full-otif-dax]] — OTIF metric
- [[order-cycle-time-oct-dax]] — OCT timing metric
- [[order-fulfillment-dax]] — fulfillment patterns
