---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 1
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-1-297936931171
note_type: pattern
tags: [dax, variance, conditional-display, retail, budget]
---

# Conditional Variance Display — Hide -100% When No Budget

When a store has no budget assigned, a naive `Actual / Budget - 1` variance formula returns -100% — making missing data look like catastrophic underperformance. The fix: return `BLANK()` when the variance is ≤ -100%, and when the budget itself is blank.

## Problem

`DIVIDE([Total Sales], [Budget]) - 1` with no budget returns `-1` (= -100%), which:
- Creates alarming visuals for non-issues
- Misleads users into thinking a store is catastrophically underperforming
- Obscures the real story: there is no data, not a performance problem

## Pattern

```dax
MEASURE _Metrics[% Variance] =
VAR raw_variance =
    IF(
        ISBLANK([Budget]),       -- no budget assigned
        BLANK(),                 -- don't show anything
        DIVIDE([Total Sales], [Budget]) - 1
    )
VAR display_variance =
    IF(
        raw_variance <= -1,      -- variance is -100% or worse
        BLANK(),                 -- hide it
        raw_variance
    )
RETURN
    display_variance
```

## When to Use

Use when:
- Budget data may be missing for some entities (stores, products, regions)
- You want clean dashboards that don't show alarming false negatives
- The variance metric is exposed to business users who need reliable signals

## Layered IF Structure

The pattern has two layers:
1. **Outer layer:** `ISBLANK([Budget])`: budget exists at all
2. **Inner layer:** `raw_variance <= -1`: even with budget, variance is effectively zero or worse

Both layers return `BLANK()`, preventing misleading -100% displays.

## Variations by Granularity

The same pattern applies at different time levels by swapping the budget measure:

| Granularity | Budget Measure | Sales Measure |
|------------|----------------|---------------|
| Day | `[Budget_Day]` | `[Total Sales]` |
| Month-to-Date | `[MTD Budget]` | `[MTD Sales]` |
| Year | `[Budget_range_1]` | `[Total Sales]` |
| Year-over-Year | `[YOY Budget]` | `[YOY Sales]` |

## Related

- [[DAX-VAR-RETURN-Pattern]] — variable pattern used inside this measure
- [[DIVIDE-Safe-Division]] — DIVIDE handles division by zero; ISBLANK handles missing budget
- [[BLANK-vs-Zero]] — BLANK is excluded from averages; 0 is included
