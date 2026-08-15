---
created: 2026-08-05
updated: 2026-08-05
source: Arrow Charts in Power BI Enhancing Data Visualization (Boniface Muchendu)
note_type: atomic
tags: [power-bi, arrow-chart, line-chart, error-bars, markers, conditional-formatting, build]
---

# Arrow Chart: Line + Marker Conditional Formatting + Error Bars

Full build recipe for an Arrow chart in Power BI: a line chart with conditionally-coloured markers (green for increase, red for decrease) and error bar arrows connecting the data points.

## Step 1: Start with a Line Chart

1. Plot your data as a **standard column chart** first to verify the data shape
2. Convert to a **Line chart:** line charts provide clearer data points for marker manipulation
3. Add your time/category axis and the values you want to track

## Step 2: Create Period Comparison Measures

Three DAX measures are required:

```dax
-- Measure 1: Current period value
Current Qtr Sales = SUM(Sales[Amount])

-- Measure 2: Previous period value
Prev Qtr Sales = CALCULATE(
    [Current Qtr Sales],
    PARALLELPERIOD(DimDate[Date], -1, QUARTER)
)
```

## Step 3: Split Into Positive and Negative Series

Power BI cannot conditionally format a single line series by value — the workaround is to split into two series using IF/BLANK:

```dax
-- Positive series: show value only when current > previous
Sales Positive =
IF(
    [Current Qtr Sales] > [Prev Qtr Sales],
    [Current Qtr Sales],
    BLANK()
)

-- Negative series: show value only when current < previous
Sales Negative =
IF(
    [Current Qtr Sales] < [Prev Qtr Sales],
    [Current Qtr Sales],
    BLANK()
)
```

Add both measures to the line chart values.

## Step 4: Conditional Formatting on Markers

1. Select the line chart → **Format pane** → **Markers** (for each series)
2. For `Sales Positive` series: set marker colour to **green**
3. For `Sales Negative` series: set marker colour to **red**
4. Enable markers, adjust shape and size

## Step 5: Add Error Bar Arrows

1. Format pane → **Error bars** → enable for the primary series
2. Set **Upper bound**: `Sales Positive` (or absolute value of change)
3. Set **Lower bound**: `Sales Negative`
4. Enable **Custom** → select the appropriate series for each bound
5. Enable **Arrow options**: direction auto-detected from bounds
6. Style: straight or curved; adjust thickness and transparency

Result: upward green arrows for increases, downward red arrows for decreases.

## Step 6: Add Labels

Format pane → **Data labels** for each series:
- **Show**: enabled
- **Display**: absolute value or percentage change
- **Background**: add background colour for readability
- **Position**: end or start of the line segment

## Visual Output

| Element | Purpose |
|---------|---------|
| Line | Shows the trajectory (journey) of the data |
| Green markers + upward arrows | Increases (positive change) |
| Red markers + downward arrows | Decreases (negative change) |
| Labels | Exact value or % change at each point |

## Key Insight

The IF/BLANK split means each series is invisible (blank) for the opposite condition — so at any given time point, only one marker and one arrow direction is visible, making the chart immediately readable.

## Related

- [[Dual-Measure-Conditional-Formatting-Positive-Negative]]
- [[Period-over-Period-DAX-Measures-Arrow-Chart]]
- [[Error-Bars-Power-BI-Native]]
