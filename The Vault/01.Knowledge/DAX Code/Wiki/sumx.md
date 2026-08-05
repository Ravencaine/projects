---
created: 2026-07-27
updated: 2026-08-02
source: "Iterators in DAX: SUMX, AVERAGEX, RANKX"
note_type: function
tags: [dax, sumx, iterator, function]
---

# SUMX Function

Iterates over a table row-by-row, evaluates an expression for each row, then sums the results. The most common DAX iterator.

## Signature

```dax
SUMX ( <Table>, <Expression> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `<Table>` | table | Table or table expression to iterate |
| `<Expression>` | scalar | Expression evaluated per row — must return a scalar value |

## Returns

A single scalar value (the sum of the per-row expression results).

## Examples

```dax
-- Row-by-row: Quantity x Price, then sum
Total Revenue =
SUMX (
    Sales,
    Sales[Quantity] * Sales[Price]
)

-- Profit: Revenue - Cost per row, then sum
Total Profit =
SUMX (
    Sales,
    Sales[Revenue] - Sales[Cost]
)
```

## Notes

- SUMX creates **row context**: Expression can reference columns of Table directly
- If Expression contains CALCULATE, context transition occurs
- **Common anti-pattern:** SUMX(Sales, Sales[Amount]) — replace with SUM(Sales[Amount]) for 27x faster
- **Performance rule:** If the expression is just a single column reference, use SUM instead

## Related

- [[sum]]
- [[averagex]]
- [[rankx]]
- [[iterator-vs-aggregator-comparison]]
- [[sumx-vs-sum-gotcha]] — anti-pattern gotcha
