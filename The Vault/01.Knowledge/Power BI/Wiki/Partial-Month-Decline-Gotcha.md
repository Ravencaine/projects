---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into Power BI reporting with the new date picker slicer option (Preview).md"
note_type: gotcha
tags: [power-bi, date-picker, slicer, partial-month, relative-dates, gotcha]
---

# Partial Month Decline — Incomplete Current Month Gotcha

> **Type:** gotcha
> **Routed to:** Power BI
> **Primary source:** Microsoft Fabric / DataZoe — 2026-07-16

## Problem

When a report includes the current (incomplete) month, the chart shows a sharp, misleading decline. This looks like poor performance when it's actually just unfinished data.

Report viewers and executives see a downward spike and ask "why is this month so low?" — the answer is simply that the month isn't finished yet.

## Why It Happens

Standard date slicers and filter panes filter to all dates up to today (or the latest date in the data). The current month has only a fraction of its data, making it look dramatically worse than prior months.

## When It Occurs

- Any report that includes the current month
- Reports with daily or weekly granularity
- Operational dashboards tracking in-progress periods
- Any KPI comparing current period to historical

## How It Looks

A bar chart where January through November are full-height bars, then December (or the current month) is a short stub — not because December is bad, but because only a few days of December have passed.

## Solution

Use the Date Picker Slicer's **relative range anchored to Last date** with **calendar months**:

- Set: "Last N Months (Calendar) from Last date"
- The calendar-month grain means the range only activates when a full month is complete
- Current incomplete month is excluded automatically
- Year-over-year comparisons always use complete, comparable periods

## Key Setting

| Setting | Value |
|---------|-------|
| Period grain | Months (Calendar), not Days |
| Anchor | Last date (not Today) |
| Direction | Last (past-facing) |

## See Also

- [[Source-Date-Picker-Slicer-Preview]] — source article
- [[Last-Full-Month-Date-Picker-Workflow]] — full configuration workflow
- [[Date-Range-Beyond-Available-Data]] — related: date tables extending beyond actual data
