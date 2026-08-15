---
created: 2026-08-08
updated: 2026-08-08
source: ABC Analysis in Power BI The Chart That Shows Your 8020 Instantly
note_type: atomic
tags: [power-bi, visual-calculations, next, sorting]
---

# NEXT Function in Visual Calculations

`NEXT` returns the value of an expression for the next item on the visual axis. Its real power comes from the `ORDER BY` argument, which controls the logical sort order — independent of the visual display order.

## Definition

```
NEXT(
  <expression>,
  ORDER BY <expression> [ASC|DESC],
  <axis>
)
```

## Primary Use Case

Identifying the **last item in a group:** by comparing each item's value against the NEXT item's value:

```
Next Running Sum =
  NEXT(
    [Running Sum],
    ORDER BY [Total Sales] DESC,
    ROWS
  )

// Label only the last B item:
= IF([Group B] - [Next Running Sum] > 0, [Group B], BLANK())
```

- When `Group B - Next Running Sum > 0`, the current item is the last B item
- Apply a data label only on that point → label appears once per bucket

## Critical Gotcha

`NEXT` uses the sort order defined by `ORDER BY`, **not** the visual display order. If you omit `ORDER BY`, `NEXT` follows the axis field's internal ordering (e.g., alphabetical by ProductId), which is almost never what you want for Pareto analysis.

> Always pair `NEXT` with the same `ORDER BY` used in your `RUNNINGSUM`.

## Related

- [[Visual-Calculations-RUNNINGSUM-ORDER-BY]] — ORDER BY context for NEXT
- [[ABC-Classification-Chart-Visual-Calculations]] — NEXT used to place A/B/C labels
