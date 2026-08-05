---
created: 2026-07-30
updated: 2026-08-02
source: "dax4humans_ch7_better_together.txt"
note_type: pattern
tags: [market-basket, association, cross-sell, combinatorics]
---

# Better Together — Market Basket Analysis

Identifies pairs of items that are purchased together in the same order, enabling cross-sell recommendations and association analysis.

## Purpose

Given a transaction table of orders and items, this pattern finds all unique item pairs that appear together in at least one order. Useful for market basket analysis, recommendation engines, and bundle strategy.

## Components

- `DISTINCT` — extract unique item names
- `GENERATE` — Cartesian product of item pairs
- `SELECTCOLUMNS` — rename columns to avoid name collisions in GENERATE
- `FILTER` — remove pairs where item1 = item2 and deduplicate reversed pairs
- `SUMMARIZE` — group by Order_ID to count co-occurrences
- `ADDCOLUMNS` — add a "Bought Together" count column per pair
- `COUNTROWS` — count orders where both items appear

## Structure

```dax
Better Together =
  VAR __Items = DISTINCT( 'Orders'[Item_Name] )
  VAR __Table =
    FILTER(
      GENERATE(
        SELECTCOLUMNS( __Items, "__Item1", [Item_Name] ),
        SELECTCOLUMNS( __Items, "__Item2", [Item_Name] )
      ),
      [__Item1] < [__Item2]       -- deduplicate reversed pairs + remove self-pairs
    )
  VAR __Result =
    ADDCOLUMNS(
      __Table,
      "Bought Together",
      VAR __Table2 =
        SUMMARIZE(
          FILTER(
            'Orders',
            [Item_Name] = [__Item1] | [Item_Name] = [__Item2]
          ),
          [Order_ID],
          "__Count", COUNTROWS( 'Orders' )
        )
      VAR __Count = COUNTROWS( FILTER( __Table2, [__Count] > 1 ) ) + 0
      RETURN __Count
    )
  RETURN __Result
```

## Example

Given orders:

| Order_ID | Item_Name |
|----------|-----------|
| 1 | Kettle |
| 2 | Kettle, Iron |
| 3 | Tomatoes, Cucumber |
| 4 | Kettle, Iron, Cucumber |
| 5 | Cucumber, Kettle, Tomatoes |

Result pairs (non-reversed, non-self):

| __Item1 | __Item2 | Bought Together |
|---------|---------|---------------|
| Kettle | Iron | 2 (Orders 2 and 4) |
| Kettle | Cucumber | 2 (Orders 4 and 5) |
| Cucumber | Tomatoes | 2 (Orders 3 and 5) |
| Iron | Cucumber | 1 |

The count `> 1` filter excludes pairs that only appear in single-item orders.

## Variations

**Show all pair combinations (including count = 1):**
Remove `> 1` from the final COUNTROWS filter.

**Exclude pairs ordered only once:**
```dax
VAR __Count = COUNTROWS( FILTER( __Table2, [__Count] > 1 ) ) + 0
```

**Triplet analysis:** Extend by adding a third `SELECTCOLUMNS` to GENERATE — requires adjusting the deduplication filter logic accordingly.

## Notes

- The `GENERATE` with two `SELECTCOLUMNS` creates a full Cartesian product of items, then `__Item1 < __Item2` deduplicates both self-pairs and reversed duplicates simultaneously.
- The combination count formula counts orders where ≥ 2 items from the pair appear, not strictly "only those two items."
- Number of possible pairs from `n` items = C(n, 2) = n! / (r!(n-r)!)

## Related

- [[customer-churn-rate-dax]] — related customer analytics patterns
- [[customer-lifetime-value-ltv-dax]] — related customer value metrics
- [[dax-variables-var-return]] — VAR/RETURN usage in complex measures
