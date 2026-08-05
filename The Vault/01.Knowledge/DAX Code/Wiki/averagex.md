---
created: 2026-07-27
updated: 2026-08-02
source: "Iterators in DAX: SUMX, AVERAGEX, RANKX"
note_type: function
tags: [dax, averagex, iterator, function]
---

# AVERAGEX Function

Iterates over a table row-by-row, evaluates an expression per row, then returns the average of those values. Used for weighted averages where simple AVERAGE gives the wrong result.

## Signature

```dax
AVERAGEX ( <Table>, <Expression> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `<Table>` | table | Table or table expression to iterate |
| `<Expression>` | scalar | Expression evaluated per row |

## Returns

The arithmetic mean of the per-row expression results.

## Examples

```dax
-- Weighted average price: Revenue / Quantity per row, then average
Weighted Avg Price =
AVERAGEX (
    Sales,
    Sales[Revenue] / Sales[Quantity]
)

-- Average days to ship per order
Avg Days to Ship =
AVERAGEX (
    Sales,
    Sales[DaysToShip]
)
-- Note: AVERAGE(Sales[DaysToShip]) is faster for simple column average
```

## Notes

- AVERAGEX ignores BLANK rows but includes 0 values in the average
- **Common anti-pattern:** AVERAGEX(Sales, Sales[DaysToShip]) — replace with AVERAGE(Sales[DaysToShip]) for 34x faster
- Use AVERAGEX when the per-row expression computes a derived value (ratio, compound calculation)

## Related

- [[sumx]]
- [[average]]
- [[rankx]]
- [[iterator-vs-aggregator-comparison]]
