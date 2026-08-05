---
created: 2026-08-01
updated: 2026-08-02
source: "Unraveling DAX Functions The Mystery Behind AVERAGE, AVERAGEA, and AVERAGEX.md"
note_type: atomic
tags: [dax, averagex, iterator, row-context, CALCULATE, intermediate]
---

# AVERAGEX Iterator Pattern

## Core Pattern

`AVERAGEX(table, expression)` = iterator: evaluate `expression` for each row, then average the results.

```c
AVERAGEX(Sales, Sales[Quantity] * Sales[Price])
```

Steps:
1. Iterates over `Sales` (row context)
2. Evaluates `Quantity * Price` per row
3. Collects all results into a temporary column
4. Computes the average of that column

## Performance Note

| Variant | Performance |
|---------|-----------|
| `AVERAGE(Sales[Price])` | ✅ Faster — direct column aggregation |
| `AVERAGEX(Sales, Sales[Price])` | ❌ Slower — unnecessary row-by-row evaluation |

**Use AVERAGEX only when the expression adds value** (multiplication, ratio, conditional logic). For a flat column, AVERAGE is preferred.

## Common Patterns

### Average Revenue per Transaction

```c
Avg Revenue :=
AVERAGEX(
    Sales,
    Sales[Quantity] * Sales[Unit Price]
)
```

### Average Margin Percentage

```c
Avg Margin % :=
AVERAGEX(
    Sales,
    DIVIDE(Sales[Revenue] - Sales[Cost], Sales[Revenue])
)
```

### Average Days to Close (with IF guard)

```c
Avg Days to Close :=
AVERAGEX(
    Issues,
    IF(Issues[Closed Date] <> BLANK(),
        Issues[Closed Date] - Issues[Opened Date]
    )
)
```

## Context Transition Inside AVERAGEX

Because AVERAGEX creates a row context, CALCULATE inside the expression triggers context transition:

```c
Avg Sales :=
AVERAGEX(
    Sales,
    CALCULATE(SUM(Sales[Amount]), Sales[Region] = "West")
)
```

The CALCULATE sees the current row context and transforms it to a filter context. Equivalent to `SUM(Sales[Amount])` with the outer row's filters applied.

## Combining with FILTER

```c
Avg Large Order :=
AVERAGEX(
    FILTER(Sales, Sales[Amount] > 1000),
    Sales[Amount]
)
```

AVERAGEX filters the table first (row context), then evaluates the expression for each remaining row.
