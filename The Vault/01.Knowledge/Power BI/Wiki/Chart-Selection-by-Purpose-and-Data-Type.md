---
created: 2026-08-10
updated: 2026-08-10
source: Data Visualisation Best Practice Tips
source_url: https://medium.com/@simon.harrison_Select_Distinct/data-visualisation-best-practice-tips-aeec7a4cd2ed
note_type: atomic
tags: [power-bi, design, charts, chart-selection, data-types, visual-purpose]
---

# Match Chart Type to Purpose and Data Type

Different chart types serve different cognitive tasks. Choosing the wrong one creates confusion even when the data is correct.

## Chart Selection Heuristics

| What you want to show | Best chart type | Avoid |
|---|---|---|
| Part-to-whole relationship | Pie, donut, treemap | Multiple pie charts side by side |
| Ranking or comparison | Bar chart (horizontal) | Pie chart for many categories |
| Trend over time | Line chart | Bar chart with too many time periods |
| Distribution | Histogram, box plot | Line chart for non-temporal distributions |
| Correlation between two variables | Scatter plot | Stacked bar for two continuous variables |
| Geographic data | Map, filled map | Table with latitude/longitude columns |

## Data Type → Chart Fit

- **Nominal data** (categories, no order): bar chart, pie chart
- **Ordinal data** (ordered categories): bar chart with ordered categories
- **Interval/ratio data** (continuous): scatter plot, line chart, histogram

## Rule of Thumb

> If the user has to work harder to read the chart than to read a table, the chart is the wrong choice.

## Related

- [[Treemap-Beats-Bar-Chart-15-Plus-Categories]] — treemap > bar chart at ~15+ categories; area comparison more intuitive
- [[KPI-Card-Context-Principle]] — KPI cards answer "what?"; charts answer "how?" and "why?"
