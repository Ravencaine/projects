---
created: 2026-08-02
updated: 2026-08-05
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: pattern
tags: [powerbi, pattern, kpi, dashboard, layout]
---

# Dynamic KPI Card Layout

A composite Power BI visual built from core visuals (shape, card, line chart, button slicer) that displays a headline metric, a week-over-week trend, and a set of interactive highlights that drive a detail chart below.

## Purpose

Executive dashboards need KPI cards that communicate at a glance while allowing drill-down into the underlying drivers. This layout packages all four into a single compact visual: the current metric, trend direction, and interactive highlights that pivot a supporting chart to the most relevant detail.

## Components

| Component | Visual | Purpose |
|-----------|--------|---------|
| Background | Rectangle shape | Container + title |
| Theme icon | Image | Visual branding |
| Role slicer | Slicer (native) | Filter by staff role |
| Main metric | Card visual | OT Hours per FTE for last 7 days |
| Trend | Line + KPI card | Week-over-week variance % |
| Highlights | Button slicer | Navigate 4 key observations |
| Detail chart | Clustered column chart | Shows metric relevant to selected highlight |

## Structure

```
┌─────────────────────────────────┐
│ [Icon] KPI Title    [Role ▾]   │  ← Rectangle + Image + Slicer
├─────────────────────────────────┤
│    OT Hours per FTE             │  ← Card
│    Since Last Week  +12.3%     │  ← Line chart + KPI
├─────────────────────────────────┤
│ Key Observations                │
│  ▸ Highlight 1 (selected)       │  ← Button slicer
│    Highlight 2                  │
│    Highlight 3                  │
│    Highlight 4                  │
├─────────────────────────────────┤
│ [Dynamic Column Chart]          │  ← Driven by selected highlight
└─────────────────────────────────┘
```

## Example

The card always shows the most recent 7-day window:
- Max Date = latest date in dataset (dynamic on refresh)
- Min Date = Max Date − 7
- CALCULATE applies the date filter to the base OT Hours per FTE measure

The button slicer changes which highlight is active — the chart below updates automatically because its `Values` field is bound to `Column Value`, a SWITCH measure that returns the correct metric per highlight.

## Variations

- Swap the clustered column chart for a line chart or matrix depending on the metric type
- Add a custom tooltip visual to the chart for shift-level drill-down
- Replace the role slicer with a date range or department filter
- Use emoji prefixes in DAX string concatenation for compact highlight text (e.g. `"👥 5 employees >10h OT"`)

## Related

- [[Button-Slicer]]
- [[Highlights-Table-Unconnected-Helper-Table]]
- [[Dynamic-Chart-SWITCH-on-Button-Slicer]]
- [[Advanced-KPI-Cards]]
