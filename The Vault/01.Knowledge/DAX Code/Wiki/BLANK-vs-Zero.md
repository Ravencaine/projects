---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 1
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-1-297936931171
note_type: function
tags: [dax, blank, missing-data, aggregation, semantics]
---

# BLANK() vs 0 — Behaviour in Aggregations

`BLANK()` and `0` are semantically different in DAX. `BLANK()` represents missing or unknown data and is excluded from most aggregations. `0` is an actual zero value and is included. Confusing them produces incorrect averages, totals, and measure results.

## Definition

- **`BLANK()`:** DAX's representation of missing, unknown, or not-applicable data. Not the same as an empty string or null in SQL.
- **`0`:** An explicit numeric zero. A valid value that participates in calculations.

## Key Difference: Excluded vs Included

| Function | BLANK() behaviour | 0 behaviour |
|----------|------------------|-------------|
| `SUM()` | Ignored | Included (adds 0) |
| `AVERAGE()` | Excluded from numerator AND denominator | Included in both |
| `COUNTROWS()` | Ignored | Included |
| `MIN()` / `MAX()` | Excluded | Included |
| Division (`/`, `DIVIDE`) | Treated as 0 (division by 0 → BLANK) | Normal division |

## Concrete Example: AVERAGE()

Given three stores with sales:

| Store | Sales |
|-------|-------|
| Store A | 100 |
| Store B | 0 |
| Store C | BLANK() |

```
SUM   = 100 + 0 + (nothing) = 100
COUNT = 2   (Store C's BLANK is not counted)
AVERAGE = 100 / 2 = 50
```

Store C's BLANK is **excluded from both the sum and the count**. The result is the average of the two non-blank stores. If Store C had `0` instead of `BLANK()`, the average would be `100 / 3 = 33.3`.

## Practical Impact

### Where this matters

- **Average sales per store:** stores with no sales should be BLANK, not 0, if "no sales" means "no data" rather than "explicitly zero"
- **KPIs with missing budget:** `ISBLANK([Budget]) → BLANK()` returns nothing, not 0, so measures downstream don't treat it as zero
- **Division by blank:** `100 / BLANK` = `BLANK` (not an error); `100 / 0` = `BLANK` (or error with `/`)
- **Counting rows:** `COUNTROWS(Table)` counts rows with BLANK values in columns as 1 row; only BLANK in all columns of a scalar context produces BLANK

## Returning BLANK vs 0 from Measures

```dax
-- Return BLANK when there's no budget (cleaner downstream behaviour)
MEASURE [% Variance] =
IF(
    ISBLANK([Budget]),
    BLANK(),                    -- not 0
    DIVIDE([Total Sales], [Budget]) - 1
)

-- Return 0 when there were genuinely zero sales (different semantic)
MEASURE [Total Sales] =
IF(
    [Units Sold] = 0,
    0,                          -- explicit zero — no sales recorded
    [NetAmount] / [Units Sold]
)
```

## Related

- [[DIVIDE-Safe-Division]] — DIVIDE treats denominator BLANK → BLANK result
- [[Conditional-Variance-Display-Hide-Minus-100]] — ISBLANK(Budget) → BLANK() pattern
