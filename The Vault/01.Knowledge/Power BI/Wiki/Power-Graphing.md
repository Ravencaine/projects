---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [table, data-bars, conditional-color, visual-title, multi-measure]
related: [SWITCH, Dynamic-Color-Coding-Bar-Charts, Context-Sensitive-Visual-Toggle]
---

# Power Graphing (Table as Chart)

Uses the native Table or Matrix visual with data bars, conditional font colors, and dynamic title/subtitle measures to create a rich data-dense display without a traditional chart visual.

## Why "Power Graphing"

Standard Power BI charts (bar, line) have fixed X/Y encoding. The Table visual allows custom column ordering, conditional styling per cell, and data bars — making it a flexible alternative for data that doesn't map cleanly to chart axes.

## Setup

1. Add a **Table** visual.
2. Add columns: Category, Metric 1, Metric 2, Trend.
3. Enable **Data bars** on numeric columns (Format → Data bars).

## Dynamic Title Measure

```dax
Chart Title =
    "Top Products by "
    & SELECTEDVALUE('KPI Selection'[KPI Name], "Revenue")
    & " | "
    & FORMAT(TODAY(), "mmm yyyy")
```

Assign to: **Format → Card → Title → Field value** → select the title measure.

## Conditional Font Color

For the Trend column, create a measure:
```dax
Trend Color =
    IF([Trend] > 0, "#76E3B4", "#EE6064")
```

In the Table visual:
- Add Trend to the Values well.
- Format → Cell elements → Font color → Conditional formatting → Field value → select `Trend Color`.

## Subtitle from Measure

```dax
Chart Subtitle =
    "Showing " & DISTINCTCOUNT('Products'[Category])
    & " categories above "
    & FORMAT([Average Target], "$#,##0")
    & " threshold"
```

## Notes

- Data bars in the Table visual replace the Y-axis encoding — the bar length shows the relative magnitude of each value.
- Dynamic title measures make the report self-documenting — the title always reflects the current filter context.
- Bittar's Power Graphing article demonstrates this technique as a replacement for standard bar charts when the data requires more context than a simple chart can provide.
- Combine with [[Context-Sensitive-Visual-Toggle]] to show a table or chart depending on the number of categories.

## Related

- [[Dynamic-Color-Coding-Bar-Charts]] — conditional color logic
- [[Context-Sensitive-Visual-Toggle]] — switch between table and chart views
- [[SWITCH]] — dynamic title based on field parameter selection
