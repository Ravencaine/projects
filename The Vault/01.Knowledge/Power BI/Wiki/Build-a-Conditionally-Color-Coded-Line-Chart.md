---
created: 2026-08-06
updated: 2026-08-06
source: Conditionally Color-Coding Line Charts in Power BI 📈
note_type: workflow
tags: [line-chart, conditional-color, dax, power-bi, visualization, step-by-step]
---

# Build a Conditionally Color-Coded Line Chart

Step-by-step: create two overlay DAX measure series to make a Power BI line chart change color dynamically based on price/metric variation.

## Prerequisites

- Power BI Desktop with a data table containing a numeric value and a date column (e.g., Bitcoin prices)
- A DateSelection table (connected) to drive the slicer timeframe
- Basic familiarity with CALCULATE, FILTER, and IF in DAX

## Step 1 — Create Date Range Measures

Create three measures under your Dates folder:

```dax
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

## Step 2 — Create a Disconnected Calendar Table

In Power Query, create a new table:

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

> ⚠️ Do **not** create a relationship between this Calendar table and your data table. It is disconnected.

## Step 3 — Create the Price for Graph Measure

```dax
Price for Graph =
VAR _SelectedDate = SELECTEDVALUE('Calendar'[Date])
RETURN
    CALCULATE(
        [Price],
        FILTER(Bitcoin, Bitcoin[Date] = _SelectedDate)
    )
```

## Step 4 — Create the Two Color Series Measures (Stage 1)

Create both measures returning the same value first — both must be visible to set their colors:

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

## Step 5 — Add Both Series to the Line Chart

1. Select the **Line chart** visual
2. Drag `Calendar[Date]` to the **X-axis**
3. Drag **Price — Green Line** and **Price — Red Line** to the **Y-axis**
4. Set X-axis to **Continuous**
5. Set X-axis **Minimum Range** to `[Min Date]`

## Step 6 — Set Series Colors

In the Format pane:

- **Price — Green Line** → set color to **green**
- **Price — Red Line** → set color to **red**

> ⚠️ Do this before Step 7. If a series is hidden when you try to set its color, the color option will not be available.

## Step 7 — Update Measures to Hide Inactive Series

Replace both measures with these versions:

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

> ⚠️ Return nothing after the value — do not add a second argument. Omitting the third argument to IF() returns BLANK() automatically.

## Step 8 — Final Polish

- **Legend: OFF:** both series have the same label "Price" (see below)
- Rename the Y-axis fields to "Price" in the Fields pane so tooltips display cleanly
- Test by changing the date slicer — the line color should change when the price variation crosses zero

## Tips

- The disconnected Calendar table is the key to making the X-axis continuous — it prevents the slicer from filtering the axis while still allowing SELECTEDVALUE() to read the date range
- If your threshold is different (e.g., variance vs. budget), replace `[Price Variation] >= 0` with your own measure
- For Area charts: same pattern, same steps — area fill color follows the line color

## Related

- [[Conditional-Color-Coding-Line-Charts-in-Power-BI]] — concept overview
- [[Line-Chart-Overlay-Pattern-for-Conditional-Color]] — pattern reference with full DAX
- [[Color-Coding-4-Techniques]] — 4-technique reference (Technique 4 = this overlay pattern)
