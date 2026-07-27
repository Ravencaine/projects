---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, window]
---

# Window Functions Overview

Window functions operate over a set of rows defined by an **ORDERBY** clause. They require ORDERBY and return rows based on their position relative to the current row.

## Companion Functions (used to define the window)

| Function | Purpose |
|----------|---------|
| `ORDERBY` | Defines the sort order within each partition |
| `PARTITIONBY` | Restarts the window for each group (like SQL PARTITION BY) |
| `MATCHBY` | Defines equality groups without projecting output columns |

## Window Functions

| Function | Purpose |
|----------|---------|
| `INDEX` | Returns a row at an absolute position (1-based) within a partition |
| `OFFSET` | Returns a row at a relative position (delta) from the current row |
| `WINDOW` | Returns a range of rows between two positions |
| `RANKX` | Ranks values within a partition (dense/skip/race variants) |
| `ROWNUMBER` | Assigns sequential numbers within a partition |

## Key Concepts

### ORDERBY

```dax
-- ORDERBY is required by all window functions
OFFSET(1, ORDERBY('Sales'[Date], ASC))
```

- Must appear inside a window function call
- Can sort by multiple columns
- Default sort direction is ASC
- When omitted inside a window function, the result depends on the function

### PARTITIONBY

```dax
-- Restart window for each color
OFFSET(1,
    ORDERBY('Sales'[Date], ASC),
    PARTITIONBY('Product'[Color])
)
```

- Like SQL `OVER (PARTITION BY ... ORDER BY ...)`
- Resets the ordering sequence for each partition
- Multiple partition columns supported

### MATCHBY

```dax
-- Match by OrderID even if outputting OrderLine
ROWNUMBER(
    ORDERBY('Sales'[OrderLine], ASC),
    MATCHBY('Sales'[OrderID])
)
```

- Defines how rows are grouped without affecting the output columns
- Useful when the grouping key differs from the output columns

## Common Patterns

```dax
-- Previous row (lag)
Sales[Prior Day] := OFFSET(-1,
    ORDERBY('Sales'[Date], ASC),
    PARTITIONBY('Product'[ProductKey])
)

-- Running total (cumulative sum)
Sales[Running Total] :=
SUMX(
    WINDOW(-INF, 0,
        ORDERBY('Sales'[Date], ASC),
        PARTITIONBY('Product'[ProductKey])
    ),
    [Sales Amount]
)

-- Rank within group
Sales[Rank] := RANKX(
    ORDERBY([Sales Amount], DESC),
    PARTITIONBY('Product'[Category])
)
```

## Notes

- All window functions require ORDERBY — no default ordering
- PARTITIONBY is optional but strongly recommended when working at row level
- Window functions are **not supported in DirectQuery mode** for calculated columns or RLS rules
- Negative positions in INDEX count from the end: `-1` is the last row

## Related

- [[window-functions-overview]]
- [[offset]]
- [[window]]
- [[rankx]]
- [[rownumber]]
- [[window-functions-orderby-partitionby-matchby]] — pattern
