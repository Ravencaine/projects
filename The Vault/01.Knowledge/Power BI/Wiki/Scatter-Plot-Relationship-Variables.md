---
created: 2026-08-08
updated: 2026-08-08
source: Choosing the Right Charts in Power BI - A Beginners Guide
note_type: atomic
tags: [power-bi, scatter-plot, correlation, relationship, data-visualization]
---

# Scatter Plot — Finding Links Between Variables

Use a **scatter plot** when the goal is to explore or communicate the relationship between two numeric variables.

## When to Use

- You have two continuous numeric measures (e.g., marketing spend vs. revenue, price vs. quantity sold)
- You want to identify correlation, clusters, or outliers
- Testing hypotheses about cause-and-effect relationships

## Power BI Scatter Plot Requirements

The Power BI scatter chart requires:
- **Two numeric axes** (X and Y) — both must be numeric
- A **unique key** field to identify each dot (prevents over-plotting)
- Optionally, a size encoding (bubble chart) or colour encoding (categorical grouping)

## When NOT to Use

> **Do not use a scatter plot for single-variable analysis or category comparisons.**

If you are only looking at one variable, or comparing categories rather than numeric relationships, a scatter plot will mislead. Always match the chart to the specific business question you are trying to answer.

## Related

- [[Line-Chart-Trend-Over-Time]] — time-series analysis (not two-variable correlation)
- [[Chart-Selection-Decision-Flow]] — decision tree for chart type
