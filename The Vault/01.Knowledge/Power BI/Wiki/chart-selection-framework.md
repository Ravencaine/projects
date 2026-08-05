---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Creating Your First Visualizations .md"
note_type: atomic
tags: [power-bi, chart-selection, visualization, beginner, dashboard-design]
---

# Chart Selection Framework

A decision tree for choosing the right chart type in Power BI based on the data relationship you need to communicate.

## Step 1: What is the Data Relationship?

| Relationship | Best chart types |
|-------------|-----------------|
| **Part-to-whole** (what proportion of the total?) | Pie, Donut, Treemap, Stacked bar |
| **Comparison** (which is bigger?) | Bar chart, Column chart |
| **Trend over time** (how is it changing?) | Line chart, Area chart |
| **Distribution** (how are values spread?) | Histogram, Scatter (with density) |
| **Correlation** (do two things move together?) | Scatter chart |
| **Single value** (what is the number?) | Card, KPI, Gauge |
| **Geographic** (where?) | Map, Filled Map |
| **Ranking** (what's top/bottom?) | Sorted bar chart |
| **Flow** (how does it move through stages?) | Funnel, Sankey, Waterfall |

## Step 2: Match to Audience and Context

| Situation | Prefer | Avoid |
|-----------|--------|-------|
| Executive summary | Cards, KPIs, single large numbers | Dense tables, multi-series line charts |
| Detailed operational report | Tables, Matrix, clustered column | Pie charts with 8+ categories |
| Time series with multiple series | Line chart | Bar chart (bar for time is a common mistake) |
| Ad-hoc exploration | Scatter, Matrix | Over-designed static charts |

## Step 3: Apply the Power BI Defaults Correctly

| Default | Common mistake | Correct use |
|---------|---------------|-------------|
| Sort by value (descending) | Leaving alphabetical sort — shows no ranking | Always sort comparison charts by magnitude |
| Stacked vs clustered | Using stacked when you need side-by-side | Clustered = comparison; Stacked = contribution |
| Time on X-axis | Putting years/months on Y-axis | Time flows left to right — always on X |

## The One-Question Rule

> Use **one chart per question.** Resist the temptation to combine multiple relationships in a single visual. A chart that tries to answer two questions communicates both poorly.

## Related

- [[visualization-right-data-clearest-way]] — the foundational principle behind this framework
- [[bar-vs-column-chart-guidance]] — specific guidance for the two most common chart types
- [[visualization-7-common-mistakes]] — what to avoid after selecting the right type
