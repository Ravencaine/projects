---
created: 2026-08-05
updated: 2026-08-05
source: ALL, ALLSELECTED and ALLEXCEPT DAX Filter Function (Boniface Muchendu)
note_type: function
tags: [dax, allexcept, filter-context, calculate, selective-keep]
---

# `ALLEXCEPT()` DAX

Removes all context filters on a table — except filters on the columns explicitly specified as arguments. The inverse of ALLEXCEPT: you declare what to keep, not what to remove.

## Definition

> ALLEXCEPT removes all context filters in the table except filters on those columns specified in subsequent arguments.

## Syntax

```dax
ALLEXCEPT(<table>, <column>[, <column>[, …]])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `table` | **First argument** — the table over which all context filters are removed |
| `column` | Subsequent arguments — the columns whose filters must be preserved |

**Note:** Unlike ALL and ALLSELECTED, the table argument comes **first**, then the columns to keep. This is the opposite order.

## The Keep/Remove Logic

| Argument type | Effect |
|-------------|--------|
| `table` (first arg) | All filters on this table are removed |
| `column` arguments | Filters on these columns are **preserved** |

```dax
-- Remove all filters on Sales EXCEPT filters on DimDate[Year]
-- So: Year slicer works, but Category/Region slicers are ignored
Sales ALLEXCEPT =
CALCULATE(
    [Total Sales],
    ALLEXCEPT(Sales, DimDate[Year])
)
```

## Example: All Regions, Filtered by Year

```dax
Total Sales = SUM(Sales[Amount])

-- Calculate total sales across all categories and regions
-- but only for the currently selected year
Sales All Regions Selected Year =
CALCULATE(
    [Total Sales],
    ALLEXCEPT(Sales, DimDate[Year])
)
```

- Year slicer: **preserved** — total reflects selected year
- Category slicer: **removed** — total includes all categories
- Region slicer: **removed** — total includes all regions

## ALLEXCEPT vs ALL

| Scenario | ALL result | ALLEXCEPT result |
|---------|-----------|-----------------|
| `ALL(Sales)` | Removes all filters on Sales | Same (removes all on Sales) |
| `ALLEXCEPT(Sales, DimDate[Year])` | N/A | Removes all on Sales **except** Year filter |

ALLEXCEPT is more surgical: it removes everything by default and selectively keeps specified columns.

## ALLEXCEPT vs ALLSELECTED

| Aspect | ALLEXCEPT | ALLSELECTED |
|--------|----------|-------------|
| What it removes | All context filters | Query-level filters only |
| What it keeps | Explicitly listed columns | Everything outside the query |
| Use case | "Ignore everything except X" | "% of page/visual total" |

## Common Use Cases

| Use case | Expression |
|---------|-----------|
| Grand total by year (ignore category/region slicers) | `ALLEXCEPT(Sales, DimDate[Year])` |
| Total across all time, filtered by product | `ALLEXCEPT(Sales, DimProduct[Product])` |
| Ignore all slicers except date range | `ALLEXCEPT(Sales, DimDate[Date])` |

## Related

- [[ALL-Function-DAX]]
- [[ALLSELECTED-Function-DAX]]
- [[ALL-ALLSELECTED-ALLEXCEPT-Comparison]]
