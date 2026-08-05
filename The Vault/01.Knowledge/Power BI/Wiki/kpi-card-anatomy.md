---
created: 2026-08-02
updated: 2026-08-05
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: pattern
tags: [powerbi, pattern, kpi, card, visual]
---

# KPI Card Anatomy

The structural composition of a multi-part KPI card visual built from Power BI core visuals, driven entirely by DAX measures for dynamic behaviour.

## Purpose

Executive KPI cards need to communicate three things simultaneously: the current value, its trend relative to a prior period, and a narrative about what is driving the change. This anatomy decomposes the card into five discrete layers, each mapped to a specific visual or DAX pattern.

## Layers

### Layer 1 — Container
A rectangle shape serves as the card background. A small thematic icon image and a text label (title) are placed on top of it.

### Layer 2 — Context Filter
A native slicer (e.g., on `Scheduling Data[Role]`) filters the entire card. Because the DAX measures use `CALCULATE` with direct filters, they respond to slicer context automatically.

### Layer 3 — Main Metric
A **Card visual** bound to `OT Hours per FTE This Week` (renamed "Since Last Week" in the data field). This is a rolling 7-day measure that self-updates on every data refresh.

### Layer 4 — Trend
A **line chart with small KPI card** showing the week-over-week variance percentage. Conditional formatting applies green for decreases in OT hours and red for increases.

### Layer 5 — Key Observations
A **button slicer** (vertical list layout) with the header set to "Key Observations". The callout value label is bound to `Highlight Headers`, which SWITCHes between four formatted text strings based on `SELECTEDVALUE(Highlights[Order])`.

## DAX Dependency Map

```
Max Date = MAX('Scheduling Data'[Date])              ← foundation
Max Date - 7 = [Max Date] - 7                       ← window start
OT Hours per FTE = DIVIDE([OT Hours], [Employee Count])
OT Hours per FTE This Week = CALCULATE([OT Hours per FTE], date range filter)
OT Hours per FTE Variance % = DIVIDE([This Week] - [Last Week], [Last Week])
Highlight Headers = SWITCH(SELECTEDVALUE(Highlights[Order]), ...)
```

## Related

- [[Dynamic-KPI-Card-Layout]]
- [[Advanced-KPI-Cards]]
- [[Button-Slicer]]
