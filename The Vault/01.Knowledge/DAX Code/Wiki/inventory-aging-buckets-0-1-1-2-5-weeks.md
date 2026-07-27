---
created: 2026-07-27
source: "Advanced Power BI DAX Measures for Retail Analytics Pt 2"
source_url: "https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-2-7b00a1662317"
note_type: pattern
tags: [dax, pattern, retail, time-intelligence, inventory]
---

# Inventory Aging Buckets (0–1, 1–2, 5+ Weeks)

A DAX pattern that classifies sales by how old the sold inventory is at time of sale — bucketed into weekly age ranges. Used to identify freshness vs aging problems in retail inventory management.

## Purpose

Retail analysts need to know: what percentage of sales come from fresh inventory (0–1 week old) vs aged inventory (5+ weeks old)? This pattern uses a pre-computed `AgeInWeeks` column in the fact table to bucket sales into age ranges, then sums each bucket separately.

Requires a calculated column `AgeInWeeks` on the sales transactions table — computed as the number of weeks between the inventory receipt date and the sale date.

## Components

- `RetailSalesTransactions[AgeInWeeks]` — pre-computed age column
- `DATESBETWEEN` — dynamic date range respecting user slicers
- `CALCULATE` — filter context modification
- `MINX(ALLSELECTED(...))` / `MAXX(ALLSELECTED(...))` — dynamic slicer-aware date boundaries
- `IF(ISBLANK(...), 0, ...)` — return 0 instead of BLANK for percentage denominators

## Structure

```dax
-- 0–1 Week Old (fresh inventory)
MEASURE _Metrics[0–1 Week $] =
CALCULATE(
    [Total Sales],
    RetailSalesTransactions[AgeInWeeks] = 0,
    DATESBETWEEN(
        dateTable[Date],
        MINX(ALLSELECTED(dateTable), dateTable[Date]),
        MAXX(ALLSELECTED(dateTable), dateTable[Date])
    )
)

-- 1–2 Weeks Old (returns 0 instead of BLANK)
MEASURE _Metrics[1–2 Week $] =
VAR _1weekold = CALCULATE(
    [Total Sales],
    RetailSalesTransactions[AgeInWeeks] = 1,
    DATESBETWEEN(
        dateTable[Date],
        MINX(ALLSELECTED(dateTable), dateTable[Date]),
        MAXX(ALLSELECTED(dateTable), dateTable[Date])
    )
)
RETURN IF(ISBLANK(_1weekold), 0, _1weekold)

-- 5+ Weeks Old (aged inventory)
MEASURE _Metrics[5+ Week $] =
VAR _weeksold = CALCULATE(
    [Total Sales],
    RetailSalesTransactions[AgeInWeeks] > 4,
    DATESBETWEEN(...)
)
RETURN IF(ISBLANK(_weeksold), 0, _weeksold)

-- Total (sum of buckets)
MEASURE _Metrics[Total_SumOfWeeksAge] =
[0–1 Week $] + [1–2 Week $] + [2–3 Week $] +
[3–4 Week $] + [4–5 Week $] + [5+ Week $]

-- Percentage
MEASURE _Metrics[0–1 Week %] = DIVIDE([0–1 Week $], [Total_SumOfWeeksAge])
MEASURE _Metrics[5+ Week %] = DIVIDE([5+ Week $], [Total_SumOfWeeksAge])

-- Average age
MEASURE _Metrics[AVG Product Age in Weeks] =
AVERAGE(RetailSalesTransactions[AgeInWeeks])
```

## Why Return 0 Instead of BLANK?

When summing percentages across buckets, returning BLANK for a missing bucket produces undefined results. A store with no 5+ week sales would show `25% + 0% + 50% + BLANK + 25%` — the BLANK propagates and breaks the percentage total. Returning 0 instead ensures all buckets sum to 100%.

## Related

- [[conditional-variance-display-percent-hide]] — similar IF(ISBLANK) guard pattern
- [[sales-to-budget-variance-percent]] — another retail KPI pattern using CALCULATE
