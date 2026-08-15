---
created: 2026-08-08
updated: 2026-08-08
source: ABC Analysis in Power BI The Chart That Shows Your 8020 Instantly
note_type: atomic
tags: [power-bi, visual-calculations, running-sum, pareto]
---

# RUNNINGSUM with ORDER BY in Visual Calculations

`RUNNINGSUM` accumulates values across the visual axis in a specified sort order. The `ORDER BY` argument is critical — it determines the sequence in which values accumulate.

## Definition

```
RUNNINGSUM(
  <expression>,
  ORDER BY <expression> [ASC|DESC],
  <axis>
)
```

## Common Use

Pareto / cumulative analysis:

```
Running Sum =
  RUNNINGSUM(
    [% of Total],
    ORDER BY [Total Sales] DESC,
    ROWS
  )
```

- Sorts items by Total Sales descending before accumulating
- `ROWS` means the running sum respects the visual row ordering
- `DESC` ensures largest contributors appear first and accumulate first (true Pareto shape)

## ORDER BY Gotcha

> **Do not** use `ORDER BY [Measure]` directly — use the `ORDER BY` function inside `RUNNINGSUM`:

```
// Wrong — hard to control sort:
RUNNINGSUM([% of Total], ORDER BY SUM(Sales[SalesAmount]) DESC, ROWS)

// Correct — use ORDER BY function:
RUNNINGSUM(
  [% of Total],
  ORDER BY [Total Sales] DESC,
  ROWS
)
```

The `ORDER BY` function (not the DAX `ORDER BY` clause) is a visual calculation construct that specifies the sort key and direction for the running accumulation.

## Related

- [[ABC-Classification-Chart-Visual-Calculations]] — Pareto line in ABC chart
- [[Visual-Calculations-COLLAPSESUM]] — % of total input to RUNNINGSUM
- [[Visual-Calculations-NEXT]] — NEXT pairs with ORDER BY for bucket boundary detection
