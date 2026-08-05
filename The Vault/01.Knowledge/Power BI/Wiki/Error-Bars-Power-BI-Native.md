---
created: 2026-08-05
updated: 2026-08-05
source: Arrow Charts in Power BI Enhancing Data Visualization (Boniface Muchendu)
note_type: reference
tags: [power-bi, error-bars, line-chart, arrows, native-feature, formatting]
---

# Error Bars in Power BI Charts (Native Feature)

Power BI's native error bar feature on line charts — enables upper/lower bounds, automatic direction detection, and arrow styling. Used in Arrow Charts to draw the connecting arrows between data points.

## Availability

Error bars are available on **Line charts**, **Area charts**, and **Scatter charts** in Power BI Desktop and Power BI Service (not on column or bar charts).

## Enabling Error Bars

1. Select a line chart → **Format pane**
2. Expand **Error bars**
3. Toggle **Error bars** to **On**

## Configuration Options

### Bounds (Upper and Lower)

| Bound type | Description |
|-----------|-------------|
| **Constant** | Fixed numeric value for all points |
| **Custom** | Use a measure/column to set bounds per data point |

For Arrow Charts, the custom bounds are the positive/negative split measures:
- **Upper bound**: `Sales Positive` (current > previous)
- **Lower bound**: `Sales Negative` (current < previous)

### Direction

| Setting | Behaviour |
|---------|-----------|
| **Both** | Show arrows in both directions (up and down) |
| **Up** | Show only upward arrows |
| **Down** | Show only downward arrows |

Power BI auto-detects direction from the relative position of upper vs lower bound — but can be overridden.

### Arrow Options

| Option | Description |
|--------|-------------|
| **Style** | Straight or curved arrows |
| **Width** | Thickness of the arrow line |
| **Colour** | Arrow line colour |
| **Arrow size** | Size of the arrowhead |
| **Transparency** | Arrow line transparency |

### Markers

Error bars include marker formatting for the bound endpoints — the marker colour set on each series (green/red from the conditional formatting step) propagates to the error bar endpoints.

## Relationship to Arrow Charts

Error bars are what turn a standard line chart into an Arrow Chart:
- The **bounds** define where the arrow starts and ends (previous period → current period)
- The **direction** defines whether it's an up or down arrow
- The **style** and **arrow size** define the visual weight of the arrow

## Related

- [[Arrow-Chart-Build-Line-Marker-ErrorBar]]
- [[Dual-Measure-Conditional-Formatting-Positive-Negative]]
