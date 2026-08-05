---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: pattern
tags: [power-bi, pattern, geographic, drill-down, map]
---

# Geographic Drill-Down

A hierarchical geographic breakdown of sales — typically from Region → State → City — using map visuals and/or a matrix to reveal where the business performs strongest and weakest geographically.

## Purpose

Enables executives to identify high-performing markets for investment and underperforming markets for investigation. Supports expansion decisions and regional inventory planning.

## Components

- **Filled map** or **ArcGIS map** for region-level overview
- **Drillthrough** or **hierarchy visual** (Region → State → City)
- **Matrix table** with Region/State/City on rows, Total Sales on values
- **Optional**: Total Profit, Total Orders, Profit Margin per geography
- **Conditional formatting** on the matrix to highlight top/bottom performers

## Structure

```dax
Total Sales := SUM ( Sales[Sales] )
Total Profit := SUM ( Sales[Profit] )
Profit Margin := DIVIDE ( [Total Profit], [Total Sales] )
```

Geography hierarchy: `'Geography'[Region]` → `'Geography'[State]` → `'Geography'[City]`

## Example findings from geographic analysis

- West region contributes 40% of total sales but only 15% of total profit (high discounting)
- Texas is the top state by volume; Florida has the highest profit margin
- Chicago and New York together account for 30% of Urban sales

## Variations

- **Bubble map**: size = Total Sales, colour = Profit Margin — instantly reveals big-volume/low-margin markets
- **Decomposition tree**: auto-drills by geography without explicit hierarchy setup

## Related

- [[retail-kpi-framework]] — `atomic`
- [[category-comparison-sales-vs-profit]] — `pattern`
