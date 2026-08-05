---
created: 2026-07-27
updated: 2026-08-02
source: "Advanced Power BI DAX Measures for Retail Analytics Pt 1"
source_url: "https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-1-297936931171"
note_type: pattern
tags: [dax, pattern, variance, retail, budget]
---

# Sales-to-Budget Variance (% VAR)

A DAX pattern that calculates the percentage variance between actual sales and a budget target, with proper handling for missing budgets (blank instead of -100%).

## Purpose

Retail managers need to know: are we on track vs budget? The pattern calculates `DIVIDE(Actual, Budget) - 1` to get percentage variance, but must handle the case where no budget is assigned — returning BLANK rather than -100%, which would create misleading dashboard visuals.

## Components

- `DIVIDE()` — safe division (handles zero denominator)
- `ISBLANK()` — check if budget measure returns blank
- `IF()` — conditional return based on budget availability
- VAR/RETURN — variable pattern for readability

## Structure

```dax
-- Basic variance formula
MEASURE _Metrics[% VAR] =
IF(
    ISBLANK([Budget_range_1]),   -- Check if budget exists
    BLANK(),                      -- Return blank if no budget
    DIVIDE([Total Sales], [Budget_range_1]) - 1   -- Variance formula
)

-- The formula gives:
--  0.25 = 25% above budget
--  0    = exactly on budget
-- -0.10 = 10% below budget
-- -1    = 100% below (or no sales)
```

## Related

- [[conditional-variance-display-percent-hide]] — hiding -100% values from visuals
- sales-to-budget-variance-percent — extended version with budget MTD/YTD variants
