---
created: 2026-08-08
updated: 2026-08-08
source: Choosing the Right Charts in Power BI - A Beginners Guide
note_type: atomic
tags: [power-bi, pie-chart, donut-chart, composition, data-visualization]
---

# Pie and Donut Charts — Parts of a Whole

Use **pie** or **donut charts** when the goal is to show how individual parts contribute to a total — composition analysis.

## When to Use

- A small number of categories (≤ 4–5 slices)
- Parts add up to 100% or a meaningful whole
- Showing market share, budget allocation, or category breakdown

## Donut Chart Preference

Donut charts are generally preferred over pie charts because:
- The hollow centre can display a key metric or total
- Easier to compare arc lengths than slice angles
- Less visually dominant than full pie

## Hard Rule: Slice Limit

> **Never use a pie or donut chart with more than 4–5 slices.**

Beyond 5 slices, labels become unreadable and the eye cannot accurately compare slice sizes. If you have many categories, switch to a **horizontal bar chart:** sorted by value, it is almost always easier to read.

## Anti-Patterns

- **Too many slices:** split into "Other" category, or use a bar chart
- **3D effects:** distort slice proportions
- **Exploded slices:** only use for a single slice you want to highlight; multiple exploded slices confuse the composition

## Related

- [[Bar-Column-Chart-Comparing-Groups]] — alternative when pie/donut has too many slices
- [[Chart-Selection-Decision-Flow]] — decision tree for chart type
