---
created: 2026-08-08
updated: 2026-08-08
source: Choosing the Right Charts in Power BI - A Beginners Guide
note_type: atomic
tags: [power-bi, line-chart, time-series, trend, data-visualization]
---

# Line Chart — Tracking Changes Over Time

Use a **line chart** when the goal is to show how data moves across a time period — trends, growth, decline, seasonality.

## When to Use

- Data spans a specific period (days, months, quarters, years)
- You want to show direction of movement at a glance
- Tracking KPIs over time (revenue, sessions, sales)

## Best Practices

- **Keep the timeline clean:** avoid crowding multiple lines into one chart; tangled lines are hard to read
- Connect data points to show a clear start-to-finish path
- Use consistent time intervals on the X-axis
- Let the line colour be the primary encoding — no 3D effects or distracting fills

## Anti-Patterns

- **Too many lines**: More than 4–5 lines on one chart creates visual noise. If you have many categories, use a slicer to filter rather than overlaying everything
- **Irregular time intervals**: Gaps on the X-axis can mislead — ensure consistent granularity
- **3D effects**: Distort the relative positions of data points

## Related

- [[Bar-Column-Chart-Comparing-Groups]] — comparison chart when time is not the axis
- [[Chart-Selection-Decision-Flow]] — decision tree for choosing chart type
