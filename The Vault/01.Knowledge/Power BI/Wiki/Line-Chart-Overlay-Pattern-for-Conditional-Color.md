---
created: 2026-08-06
updated: 2026-08-06
source: Conditionally Color-Coding Line Charts in Power BI 📈
note_type: pattern
tags: [line-chart, conditional-color, overlay-series, dax, power-bi, visualization]
---

# Line Chart Overlay Pattern for Conditional Color

DAX pattern for making a Power BI line chart change color dynamically based on a metric — using two overlay measure series and static Format pane colors.

## Pattern Overview

```
Y-axis: Series A (green) + Series B (red)
Each series returns [Price for Graph] only when its condition is met, BLANK() otherwise.
```

## Step 1 — Prerequisite Measures

These are built first to drive the color condition:

```dax
Price = SUM(Bitcoin[Price])

Max Date = MAX(Dates[Date])
Min Date = MIN(Dates[Date])

Current Price =
VAR _MaxDate = [Max Date]
RETURN
    CALCULATE(
        [Price],
        FILTER(Bitcoin, Bitcoin[Date] = _MaxDate)
    )

Last Price =
VAR _MinDate = [Min Date]
RETURN
    CALCULATE(
        [Price],
        FILTER(Bitcoin, Bitcoin[Date] = _MinDate)
    )

Price Variation = [Current Price] - [Last Price]
```

## Step 2 — Calendar Table (Disconnected)

Create a single-column `Calendar` table in Power Query — NOT connected to the model. Drives the X-axis.

```m
let
    GetMinDate = Date.StartOfMonth(List.Min(Bitcoin[Date])),
    GetMaxDate = Date.EndOfMonth(List.Max(Bitcoin[Date])),
    Source     = #table({"MinDate", "MaxDate"}, {{GetMinDate, GetMaxDate}}),
    AddDateColumn = Table.AddColumn(Source, "Date",
        each {Number.From([MinDate])..Number.From([MaxDate])}),
    ExpandDates   = Table.ExpandListColumn(AddDateColumn, "Date"),
    ChangedType   = Table.TransformColumnTypes(ExpandDates,{{"Date", type date}}),
    RemovedCols   = Table.RemoveColumns(ChangedType,{"MinDate", "MaxDate"})
in
    RemovedCols
```

## Step 3 — Price for Graph Measure

```dax
Price for Graph =
VAR _SelectedDate = SELECTEDVALUE('Calendar'[Date])
RETURN
    CALCULATE(
        [Price],
        FILTER(Bitcoin, Bitcoin[Date] = _SelectedDate)
    )
```

## Step 4 — Color Series Measures

**Stage 1 — both return the same value (so both are visible for color-setting):**

```dax
Price - Green Line =
    IF(
        [Price Variation] >= 0,
        [Price for Graph],
        [Price for Graph]
    )

Price - Red Line =
    IF(
        [Price Variation] < 0,
        [Price for Graph],
        [Price for Graph]
    )
```

Set Format pane colors while both series are visible:
- **Price — Green Line** → green
- **Price — Red Line** → red

**Stage 2 — adjust to show/hide by returning BLANK():**

```dax
Price - Green Line =
    IF(
        [Price Variation] >= 0,
        [Price for Graph]
    )

Price - Red Line =
    IF(
        [Price Variation] < 0,
        [Price for Graph]
    )
```

> ⚠️ Return BLANK(), not 0 — returning 0 creates a flat zero line across the chart.

## Step 5 — Visual Configuration

- X-axis: `Calendar[Date]`, set to **Continuous**
- X-axis Minimum Range: set to `[Min Date]` from the DateSelection table
- Y-axis: both color series measures
- **Legend: OFF**
- Rename Y-axis field labels to "Price" to keep tooltips clean

## DAX Building Blocks

| Element | Purpose |
|---------|---------|
| `SELECTEDVALUE()` | Gets the single selected date from the disconnected Calendar table |
| `CALCULATE(..., FILTER(...))` | Recalculates Price at a specific date in filter context |
| `IF(condition, value, BLANK())` | Shows value only when condition is met; hides series otherwise |
| `BLANK()` | Returns empty — the series does not render at this point |
| Disconnected Calendar table | Provides continuous X-axis dates without creating a relationship |

## Notes

- The disconnected Calendar table is key — it prevents the slicer selection from filtering the X-axis, giving the visual its date range independently of the measure context
- If you have a different threshold (e.g., budget variance, growth %), replace `[Price Variation] >= 0` with your own measure
- Works for Area charts too — same pattern, same color configuration
- See [[Color-Coding-4-Techniques]] for Technique 4 (overlay charts) in context with the other three approaches
- See [[Dynamic-Line-Area-Chart-Color]] if that note exists for further variants

## Related

- [[Conditional-Color-Coding-Line-Charts-in-Power-BI]] — concept overview
- [[Build-a-Conditionally-Color-Coded-Line-Chart]] — step-by-step workflow
- [[Color-Coding-4-Techniques]] — 4-technique reference (Technique 4 = this overlay pattern)
- [[conditional-formatting-via-dax]] — DAX-based conditional formatting for visuals with fx support
