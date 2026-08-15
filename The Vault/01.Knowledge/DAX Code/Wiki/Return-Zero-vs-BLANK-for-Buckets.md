---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 2
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-2-7b00a1662317
note_type: atomic
tags: [dax, blank, zero, aggregation, bucket, design-rule]
---

# Return 0 for Buckets, BLANK for Single Values

When a measure represents an individual bucket or category that may legitimately have zero sales, return `0`. When a measure represents a total or KPI for a specific entity, return `BLANK()` if there is no data. Mixing these up breaks either bucket summation or KPI displays.

## The Rule

| Context | Return | Reason |
|---------|--------|--------|
| Age bucket with no sales (0–1 wk, 1–2 wk, etc.) | `0` | Buckets must sum to 100%; BLANK breaks the total |
| Single KPI with no data (total sales for store with no transactions) | `BLANK()` | `BLANK` communicates "no data" cleanly; shows as blank visual |

## Why It Matters: Bucket Summation

When summing bucket percentages, `BLANK` propagates upward:

```
[0–1 wk %] = 25%
[1–2 wk %] = BLANK   (no sales in that age range)
[2–3 wk %] = 50%
[3–4 wk %] = 25%

Total = 25% + BLANK + 50% + 25% = BLANK  ← broken
```

Fix: return `0` for each empty bucket:

```
Total = 25% + 0% + 50% + 25% = 100%  ← correct
```

## Pattern

```dax
-- Bucket: empty = 0
MEASURE [_1_2_Week_$] =
VAR sales =
    CALCULATE(
        [Total Sales],
        RetailSalesTransactions[AgeInWeeks] = 1,
        DATESBETWEEN(...)
    )
RETURN IF(ISBLANK(sales), 0, sales)

-- Single KPI: empty = BLANK
MEASURE [% Variance] =
IF(
    ISBLANK([Budget]),
    BLANK(),
    DIVIDE([Total Sales], [Budget]) - 1
)
```

## When to Return BLANK Instead

- Individual store total with no transactions → BLANK (no data, not zero)
- Budget variance when no budget exists → BLANK (don't show anything)
- Variance comparison (YoY, MTD) when prior period had no data → BLANK

## Related

- [[Inventory-Aging-Buckets-Pattern]] — uses 0 for empty age buckets
- [[BLANK-vs-Zero]] — deeper treatment of BLANK() vs 0 semantics
