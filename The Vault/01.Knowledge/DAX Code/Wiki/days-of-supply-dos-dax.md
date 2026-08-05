---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, inventory, supply-chain, days, metric]
---

# Days of Supply (DOS) in DAX

Inventory KPI measuring how many days of inventory remain at the current consumption rate.

## Formula

```
DOS = On-Hand Inventory / Average Daily Usage
```

Where Average Daily Usage = Total Usage over Period / Number of Days in Period.

## Pattern

```dax
Days of Supply =
    VAR __OnHand = SUM( 'Inventory'[OnHandQty] )
    VAR __Usage = SUM( 'Inventory'[UsageQty] )
    VAR __Days = COUNTROWS( DISTINCT( 'Inventory'[Date] ] )
    VAR __AvgDailyUsage = DIVIDE( __Usage, __Days, 0 )
    VAR __DOS = DIVIDE( __OnHand, __AvgDailyUsage, BLANK() )
    RETURN __DOS
```

## Interpretation

- **High DOS**: Excess inventory, potential write-offs, working capital tied up
- **Low DOS**: Risk of stockouts, lost sales
- **Optimal DOS**: Depends on industry and supply chain characteristics

## Related

- [[on-time-in-full-otif-dax]] — OTIF supply chain KPI
- [[order-cycle-time-oct-dax]] — OCT metric
- [[fifo-first-in-first-out-dax]] — FIFO inventory costing
