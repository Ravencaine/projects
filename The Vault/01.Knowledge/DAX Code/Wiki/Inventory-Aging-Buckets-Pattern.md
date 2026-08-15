---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 2
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-2-7b00a1662317
note_type: pattern
tags: [dax, retail, inventory, aging, bucketing, calculation]
---

# Inventory Aging Buckets Pattern

Segment inventory sales into weekly age buckets (0–1 week, 1–2 weeks, 2–3 weeks, etc.) to understand whether inventory is moving at healthy rates or aging. Aged inventory (5+ weeks) signals product problems.

## Prerequisites

A `RetailSalesTransactions` table with an `AgeInWeeks` column (integer, 0, 1, 2, ...) computed in Power Query at load time.

## Bucket Measures

```dax
-- 0–1 Week (fresh inventory)
MEASURE [_0_1_Week_$] =
CALCULATE(
    [Total Sales],
    RetailSalesTransactions[AgeInWeeks] = 0,
    DATESBETWEEN(
        'dateTable'[Date],
        MINX(ALLSELECTED('dateTable'), 'dateTable'[Date]),
        MAXX(ALLSELECTED('dateTable'), 'dateTable'[Date])
    )
)

-- 1–2 Weeks
MEASURE [_1_2_Week_$] =
VAR _1weekold =
    CALCULATE(
        [Total Sales],
        RetailSalesTransactions[AgeInWeeks] = 1,
        DATESBETWEEN(...)
    )
RETURN IF(ISBLANK(_1weekold), 0, _1weekold)

-- 5+ Weeks (aged inventory)
MEASURE [_5_Week_$] =
VAR _weeksold =
    CALCULATE(
        [Total Sales],
        RetailSalesTransactions[AgeInWeeks] > 4,
        DATESBETWEEN(...)
    )
RETURN IF(ISBLANK(_weeksold), 0, _weeksold)
```

## Why Return 0, Not BLANK, for Buckets

When summing bucket percentages, returning `BLANK` from any bucket makes the total `BLANK` (undefined):

```
25% + 0% + 50% + BLANK = ?
```

Returning `0` keeps the sum clean:

```
25% + 0% + 50% + 25% = 100%
```

**Rule:** Individual buckets that may have no sales → return `0` so percentages sum correctly. Single-value KPIs (e.g., total sales for a store with no transactions) → return `BLANK`.

## Percentage Measures

```dax
MEASURE [_0_1_Week_%] = DIVIDE([_0_1_Week_$], [_Total_SumOfWeeksAge])
MEASURE [_5_Week_%]   = DIVIDE([_5_Week_$],   [_Total_SumOfWeeksAge])
```

## Total (Sum of All Buckets)

```dax
MEASURE [_Total_SumOfWeeksAge] =
CALCULATE(
    [_0_1_Week_$] + [_1_2_Week_$] + [_2_3_Week_$] +
    [_3_4_Week_$] + [_4_5_Week_$] + [_5_Week_$],
    DATESBETWEEN(
        'dateTable'[Date],
        MIN('dateTable'[Date]),
        MAX('dateTable'[Date])
    )
)
```

## Business Interpretation

| Bucket | Meaning | Signal |
|--------|---------|--------|
| 0–1 week | Fresh inventory selling quickly | Healthy |
| 1–2 weeks | Normal inventory flow | Acceptable |
| 3–4 weeks | Slowing | Monitor |
| 5+ weeks | Aged inventory | Problem — investigate cause |

## Related

- [[DATESBETWEEN-Dynamic-Date-Ranges]] — dynamic date filtering that adapts to user slicer
- [[Return-Zero-vs-BLANK-for-Buckets]] — why buckets return 0; single values return BLANK
