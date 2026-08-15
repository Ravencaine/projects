---
created: 2026-08-04
updated: 2026-08-05
source: "How to Build a Gantt Chart in Power BI Using Only Core Visuals.md"
source_url: "https://medium.com/the-bi-corner/%EF%B8%8F-how-to-build-a-gantt-chart-in-power-bi-using-only-core-visuals-6d27e1e56d13"
note_type: source
tags: [powerbi, visualization, gantt, native-visuals, overlay-pattern, ki-data-science]
---

# How to Build a Gantt Chart in Power BI (Using Only Core Visuals!)

Step-by-step walkthrough of building an interactive project-timeline Gantt chart in Power BI by overlaying two native visuals — a bar chart (task durations) on top of a column chart (project timeline) — with a "today" reference line, status-based color coding, and custom icon labels.

> **Type:** article
> **Author:** [[Author-Isabelle-Bittar|Isabelle Bittar]] (KI Data Science)
> **Published:** 2025-08-02
> **URL:** https://medium.com/the-bi-corner/%EF%B8%8F-how-to-build-a-gantt-chart-in-power-bi-using-only-core-visuals-6d27e1e56d13
> **Routed to:** Power BI

## Summary

Power BI has no native Gantt-chart visual, but the appearance of one can be reproduced with two native charts stacked and visually synced: a transparent column chart that owns the X-axis date scale and a transparent-fill bar chart that owns the per-task durations. The article walks through the full build — a Dates helper table, four key DAX measures for axis bounds / task starts / task duration, a 5-measure status family for color-by-status, an emoji-composed task label, and the visual formatting needed to hide every chart's "skeleton" so only the bars and the timeline grid remain visible.

## Key Claims

1. A Gantt chart can be reproduced in Power BI using **only native visuals:** no custom visual, no AppSource download — by overlaying a bar chart on a column chart and aligning their axes.
2. The column chart's job is purely to **own the X-axis date scale** (set to `Min Calendar Date` / `Max Project Date` bounds). Its own columns are made 100% transparent so the bar chart layered on top becomes the visible chart.
3. The bar chart carries the actual task durations. To align bars with the timeline, an explicit **Date Start Buffer** measure (DATEDIFF of calendar minimum to task start) is added as a second, transparent series that pushes each bar to the correct horizontal position.
4. Color-by-status is implemented as a **5-measure family:** one measure per status (Not Started, Delayed, Pending, In Progress, Completed), each gated by `IF(SELECTEDVALUE(...)=...)`. Drop the family onto the bar-chart X-axis and assign each series its own color.
5. A **today reference line** is added via the column chart's Analytics pane → X-Axis Constant Line, with a `Today = TODAY()` measure. Color, width, and shade-area-with-transparency are formatting choices that make the line legible without dominating the chart.
6. Custom Y-axis labels are built from two measures: a vertical-bar `"Task Status Bar = " | ""` character colored by status, plus a `Task Label` measure that prepends a SWITCH-driven emoji (Planning = 🗂️, Design = 🎨, Execution = ⚙️, Testing = 🔍, Deployment = 🚀) to the task name.
7. The hardest part is **alignment:** the right end of the bar chart must be flush with the right end of the column chart, and the left start of the bar chart with the first vertical gridline of the column chart's X-axis. Adding `Task Start Date` and `Task End Date` to the tooltip helps verify alignment interactively.

## Notable Details

- A `Dates` table in Power Query generates every date between min and max project dates plus the start of each week — used to drive the column chart's X-axis.
- The `Projects` table is denormalized in a `Date Type = "Start Date" | "End Date"` long form so `Task Start Date` and `Task End Date` can be extracted via `CALCULATE(MAX(...), FILTER(..., Date Type = ...))` instead of needing two columns.
- `MIN(Projects[Date])` over `ALL(Projects[Task])` is the core trick that ignores row context for axis-bound calculations.
- The article explicitly notes Power BI may someday release native project-management visuals, but until then this is the workaround.

## Extracted Notes

- [[Gantt-Chart-Native-Visuals-Overlay-Pattern]] — `atomic` — the headline technique: overlay a transparent column chart (timeline) on a transparent-fill bar chart (durations) to fake a native Gantt chart.
- [[Status-Conditioned-Measure-Family-Pattern]] — `pattern` — the 5-measure `IF(SELECTEDVALUE(...)=...)` family for color-by-status, reusable beyond Gantt charts.
- [[Chart-Alignment-Between-Stacked-Visuals-Gotcha]] — `gotcha` — two stacked visuals only "look right" when their axes are explicitly aligned; otherwise bars drift off the timeline.

## Metadata

| Field | Value |
|-------|-------|
| Source file | How to Build a Gantt Chart in Power BI Using Only Core Visuals.md |
| Archived at | — (still in Inbox) |
| Ingestion date | 2026-08-04 |
| Word count | ~750 |