---
created: 2026-07-27
updated: 2026-08-02
source: "Advanced Power BI DAX Measures for Retail Analytics Pt 1"
source_url: "https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-1-297936931171"
note_type: pattern
tags: [dax, pattern, variance, display, conditional]
---

# Conditional Variance Display (−100% Hide)

A DAX pattern that suppresses alarming -100% variance visuals by returning BLANK when variance is at or below -100% — used when budget data is incomplete or absent.

## Purpose

When a store has no budget assigned, the sales-to-budget variance formula returns -100% (zero sales divided by zero budget = blank → treated as -1). This creates a misleading visual — the dashboard shows deep red for a store that simply has no budget data. This pattern hides values at or below -100% to eliminate false alarms.

## Components

- `DIVIDE()` — safe division
- `ISBLANK()` — outer guard for missing budget
- `IF()` with `<= -1` threshold — inner guard to hide extreme negatives
- VAR/RETURN — two-step variable pattern for clarity

## Structure

```dax
MEASURE _Metrics[_CONDITIONAL_VAR %_] =
VAR sales_to_budget_percent =
    IF(
        ISBLANK([Budget_DateRange]),
        BLANK(),
        DIVIDE([Total Sales], [Budget_DateRange]) - 1
    )
VAR display_sales_to_budget_percent =
    IF(
        sales_to_budget_percent <= -1,   -- If variance is -100% or worse
        BLANK(),                          -- Hide value (avoid alarming visuals)
        sales_to_budget_percent
    )
RETURN display_sales_to_budget_percent

-- Same pattern applied at day-level and MTD-level
MEASURE _Metrics[_CONDITIONAL_MTD %_] =
VAR month_to_date_percent =
    IF(ISBLANK([MTD Budget]), BLANK(),
       DIVIDE([MTD Sales], [MTD Budget]) - 1)
VAR display =
    IF(month_to_date_percent <= -1, BLANK(), month_to_date_percent)
RETURN display

MEASURE _Metrics[_CONDITIONAL_YOY %_] =
VAR year_over_year_percent =
    IF(ISBLANK([YOY Sales]), BLANK(),
       CALCULATE(DIVIDE([Total Sales], [YOY Sales]) - 1))
VAR display =
    IF(year_over_year_percent <= -1, BLANK(), year_over_year_percent)
RETURN display
```

## Why Two IF Statements?

The outer `IF(ISBLANK(...))` handles the case where no budget exists at all. The inner `IF(<= -1, BLANK(), ...)` handles the case where a budget exists but performance is so poor the variance reaches -100%. Both guards are needed.

## Related

- [[sales-to-budget-variance-percent]] — base variance formula this extends
- [[blank-vs-zero-in-averages]] — related BLANK() behaviour gotcha
