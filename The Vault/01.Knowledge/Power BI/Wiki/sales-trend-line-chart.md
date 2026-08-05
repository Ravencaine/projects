---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: pattern
tags: [power-bi, pattern, line-chart, sales-trend, time-intelligence]
---

# Sales Trend Line Chart

A line chart showing Total Sales (and optionally Total Profit) over time — typically by month, quarter, or year — to reveal growth patterns and seasonal fluctuations.

## Purpose

Transforms raw time-series data into an interpretable narrative of business performance. Enables executives to spot growth trajectories, seasonal dips, and the impact of campaigns or market events at a glance.

## Components

- **X-axis**: Calendar dimension (Year, Quarter, Month, or Week)
- **Y-axis**: Total Sales (primary) and Total Profit (secondary, optional)
- **Line per measure**: Sales (solid), Profit (dashed or secondary axis)
- **Optional**: comparison line from same period last year (SAMEPERIODLASTYEAR)

## Structure

```dax
-- Base measure:
Total Sales := SUM ( Sales[Sales] )

-- Monthly trend measure (for axis):
Total Sales Monthly :=
    SUM ( Sales[Sales] )
    -- Use on a visual grouped by Calendar[Month] or [Month Name]
```

## Example

```
Month
 Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec
 120  135  142  158  145  162  189  195  178  201  234  256
```

A steady upward trend from January to December suggests seasonal peak demand during holiday period.

## Variations

- **Dual-axis line chart**: Sales on primary axis, Order Count on secondary axis
- **Area chart**: filled area below the line for stronger visual emphasis
- **Line + column**: columns for Quantity Sold, line for Average Order Value

## Related

- [[retail-kpi-framework]] — `atomic`
- [[calendar-table-time-intelligence]] — `pattern`
- [[executive-kpi-card-row]] — `pattern`
