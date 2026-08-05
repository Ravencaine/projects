---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: atomic
tags: [chart-selection, data-story, visual-encoding, comparison, trend, distribution]
related: [Double-Diamond-Design, Visual-Information-Seeking-Mantira]
---

# Chart Selection Principle

Match the chart type to the *story* you want to tell, not to the data type or the tool's default suggestion.

## The Principle

> **Ask: what decision does this visual support? Then pick the chart that answers that question most clearly.**

## Story → Chart Mapping

| Story Question | Best Chart(s) | Avoid |
|--------------|--------------|-------|
| **How much?** (single value) | KPI Card, Gauge | Pie, Line |
| **How much?** (comparison) | Bar, Column | Area, Pie |
| **Over time?** (trend) | Line, Area | Bar (if too many periods) |
| **Parts of a whole?** | Donut, Treemap, Stacked Bar | Pie (>5 segments) |
| **Relationship?** (two metrics) | Scatter | Bar |
| **Distribution?** | Histogram, Box plot | Line |
| **Where?** (geographic) | Map | Bar (if many regions) |
| **Ranking?** | Bar sorted descending | Pie |
| **Process flow?** | Custom shapes (see [[Process-Tracker-Complete]]) | Standard chart |

## Data Density vs. Visual Complexity

| Chart | Data Density | Visual Complexity | Best For |
|-------|-------------|-----------------|---------|
| KPI Card | Low | Low | 3-second overview |
| Line Chart | Medium | Low | Trends, time series |
| Bar Chart | Medium | Low | Comparisons, rankings |
| Scatter | High | High | Correlations, segments |
| Table | High | Medium | Detail, analysis |

## Bittar's Rule of Thumb

> If the audience needs to look at the chart for more than 30 seconds to understand it, the chart type is wrong for the story.

## Common Mistakes

- **Pie chart with >5 segments**: use a bar chart instead.
- **Line chart with unsorted categories**: use a bar chart.
- **Stacked area chart with >3 series**: use a line chart with a legend.
- **Map with too many regions**: use a bar chart or highlight only the top/bottom regions.

## Notes

- [[Double-Diamond-Design]] provides the framework for deciding which stories to tell on which pages.
- [[Visual-Information-Seeking-Mantira]] determines which charts appear at which depth level (overview vs. detail).
- [[The-3-30-300-Rule]] allocates the appropriate chart complexity to each tier.

## Related

- [[Double-Diamond-Design]] — decide which stories to tell
- [[Visual-Information-Seeking-Mantira]] — which chart for overview vs. detail
- [[The-3-30-300-Rule]] — complexity budget per report page
