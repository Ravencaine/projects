---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [histogram, bar-chart, numerical, categorical, distinction]
---

# Histogram vs Bar Chart — Which to Use

Histograms plot binned numerical data (x-axis is continuous). Bar charts plot categorical data (x-axis is discrete).

## Purpose

The chart type must match the data type. Using the wrong one misleads viewers.

## Structure

```
Histogram (numerical):
  X-axis: Binned numerical range [0-1), [1-2), [2-3)...  ← continuous scale
  Y-axis: Frequency (count of observations in each bin)
  Bars touch each other — no gaps

Bar Chart (categorical):
  X-axis: Category labels ["Q1", "Q2", "Q3", "Q4"]         ← discrete labels
  Y-axis: Value (sum, count, average, etc.)
  Bars have gaps between them
```

## When to Use Each

| Data type | Chart type | Example |
|-----------|-----------|---------|
| Numerical (binned) | Histogram | Life Ladder score distribution |
| Categorical | Bar/Column Chart | Revenue by product category |
| Date/Time (sequential) | Line Chart | Monthly tourists over time |

## Common Error

Showing binned numerical data as a bar chart with gaps between bars implies the categories are unrelated — they are not. Conversely, showing categorical data as a histogram implies an underlying continuous distribution.

## Related

- [[histogram-visual]]
- [[distribution-shapes-normal-right-skewed-left-skewed]]
- [[line-chart-visual]]
