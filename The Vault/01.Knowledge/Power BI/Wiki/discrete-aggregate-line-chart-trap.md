---
created: 2026-08-02
updated: 2026-08-05
source: When a Line Chart Misleads (And What to Use Instead)
note_type: gotcha
tags: [powerbi, gotcha, data-visualization, line-chart, bar-chart, discrete-aggregate, time-series]
---

# Discrete Aggregate Line Trap: Slope ≠ Real Run Rate; Bucket Summaries Need Bar Charts

Connecting bucketed aggregates (monthly churn, quarterly revenue, weekly active users) as a continuous line is a structural misrepresentation.

**The problem:** A line between March and April implies a smooth daily run rate — churn rose day by day. In reality, churn arrives in bursts when contracts end or systems glitch. The line makes a discrete summary feel like a physical law.

**Rule:** If the path within the period is unknown, do not imply one. The line segment between data points is often just made-up information.

**When line charts ARE appropriate for time series:**
- Truly continuous measurements (temperature, server load)
- Data captured at regular, evenly spaced chronological intervals
- Cumulative totals where the path between points is mathematically certain

**When to switch to bar charts:**
- Discrete, bucketed aggregates (monthly, quarterly, weekly)
- Period-based summaries where the within-period path is unknown
- When honest period-to-period comparison matters more than implied continuity

A bar chart's distinct visual buckets force an honest comparison between periods without inventing daily momentum.
