---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 2
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-2-7b00a1662317
note_type: function
tags: [dax, filter-context, all, allselected, slicer]
---

# ALL vs ALLSELECTED — Filter Context Scope

`ALL` ignores all filters. `ALLSELECTED` respects the current user slicer context. Choosing the wrong one causes measures to return either the grand total or the wrong filtered value.

## Definitions

| Function | Behaviour |
|---------|-----------|
| `ALL(table)` or `ALL(column)` | Removes ALL filters on the specified table or column — ignores slicers, ignores report filters, ignores everything |
| `ALLSELECTED()` or `ALLSELECTED(column)` | Removes filters ONLY on the visual level — respects user slicer selections that are currently active |

## Side-by-Side Comparison

```dax
-- ALL: ignores slicer, returns grand total
MINX(ALL(dateTable), dateTable[Date])
-- Result: minimum date in the entire date table

-- ALLSELECTED: respects slicer, returns minimum date in current selection
MINX(ALLSELECTED(dateTable), dateTable[Date])
-- Result: minimum date the user has selected via slicer
```

## When to Use Each

| Situation | Use |
|-----------|-----|
| Want the earliest/latest date in the user's current slicer selection | `ALLSELECTED` |
| Want to remove a filter but keep other context (e.g., remove date filter for YoY) | `ALL` |
| Want to ignore all filters for a grand total | `ALL` |
| Building a date range from slicer boundaries for DATESBETWEEN | `ALLSELECTED` |
| Inside SAMEPERIODLASTYEAR — remove date filter before applying prior-year filter | `ALL` |

## Concrete Example: Budget by Slicer Date

Budget rows stored at month level. User selects a date range via slicer. You need the budget for the latest date in the slicer:

```dax
MEASURE [YTD Budget] =
CALCULATE(
    SUM('StoreBudgets'[YTDBudget]),
    'StoreBudgets'[Date] = MAXX(
        ALLSELECTED(dateTable),    -- use slicer context, not full table
        dateTable[Date]            -- latest date currently selected
    )
)
```

Using `ALL` here would return the budget for the absolute last date in the table, ignoring the user's slicer entirely.

## Inside Inventory Aging: DATESBETWEEN

```dax
DATESBETWEEN(
    'dateTable'[Date],
    MINX(ALLSELECTED(dateTable), dateTable[Date]),  -- dynamic start from slicer
    MAXX(ALLSELECTED(dateTable), dateTable[Date])   -- dynamic end from slicer
)
```

`ALLSELECTED` makes the date range dynamic — it adapts to whatever the user has selected. Using `ALL` would always use the full table range.

## Related

- [[SAMEPERIODLASTYEAR-YoY-Pattern]] — uses `ALL` to strip date filter before applying prior-year dates
- [[Inventory-Aging-Buckets-Pattern]] — uses `ALLSELECTED` in DATESBETWEEN
- [[DATESBETWEEN-Dynamic-Date-Ranges]] — dynamic date range built from ALLSELECTED boundaries
