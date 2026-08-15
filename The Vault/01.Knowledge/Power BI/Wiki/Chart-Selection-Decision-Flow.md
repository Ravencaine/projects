---
created: 2026-08-08
updated: 2026-08-08
source: Choosing the Right Charts in Power BI - A Beginners Guide
note_type: atomic
tags: [power-bi, chart-selection, decision-tree, data-visualization]
---

# Chart Selection — Decision Flow

Use this flow to choose the right chart type based on the analytical question.

## Decision Flow

```
What is your goal?
│
├─ Show change over time?
│   └─ LINE CHART
│
├─ Compare groups or items?
│   └─ BAR / COLUMN CHART
│
├─ Show parts of a whole?
│   ├─ ≤ 4–5 categories?
│   │   └─ PIE / DONUT CHART
│   └─ > 4–5 categories?
│       └─ HORIZONTAL BAR CHART (sorted by value)
│
├─ Find relationship between two numeric variables?
│   └─ SCATTER PLOT
│
└─ None of the above?
    └─ Ask: what is the single most important question this visual must answer?
```

## Guiding Principle

> **Pick the chart that fits the goal, not the one that looks most impressive.**

The best visualisation answers a specific question clearly. If a chart type doesn't map to a clear analytical goal, reconsider whether the chart belongs in the report at all.

## Related

- [[Line-Chart-Trend-Over-Time]] — time-series
- [[Bar-Column-Chart-Comparing-Groups]] — category comparison
- [[Pie-Donut-Chart-Parts-Whole]] — composition
- [[Scatter-Plot-Relationship-Variables]] — correlation
- [[Reducing-Chart-Clutter-Power-BI]] — making any chart cleaner
