---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into Power BI reporting with the new date picker slicer option (Preview).md"
note_type: workflow
tags: [power-bi, date-picker, slicer, relative-dates, last-full-month, workflow]
---

# Last Full Month — Date Picker Slicer Relative Range Workflow

> **Type:** workflow
> **Routed to:** Power BI
> **Primary source:** Microsoft Fabric / DataZoe — 2026-07-16

## Problem

Reports showing current month display a sharp decline because the month is incomplete. Comparing current month to prior year months is misleading — the current month hasn't finished yet.

## Solution

Configure a Date Picker Slicer to show the last N complete (full) calendar months, anchored to the last available date in the data.

## Configuration Steps

1. Select the **calendar button** (left side of slicer)
2. Select **Relative**
3. Set: "Date is in the **Last** **24 Months (Calendar)** from **Last** **date** offset by **0** Months (Calendar)"
4. Select **Apply**

## Key Settings

| Setting | Value | Purpose |
|---------|-------|---------|
| Direction | Last | Past-facing |
| Period | N Months (Calendar) | Whole months only |
| Anchor | Last date | Auto-adjusts to latest data |
| Offset | 0 Months | No backshift |

## Result

- Slicer shows the last 24 complete calendar months
- Range moves forward automatically when a new full month ends
- Year-over-year comparisons always use complete months
- Pinned to dashboard → relative range continues to roll forward

## Variations

| Scenario | Config |
|----------|--------|
| Last 12 complete months | Last 12 Months (Calendar) from Last date |
| Last 3 complete quarters | Last 3 Quarters (Calendar) from Last date |
| Last 30 days | Last 30 Days from Last date |
| Start 5 days back, span 30 days | Last 30 Days from Last date offset by 5 Days |

## See Also

- [[Source-Date-Picker-Slicer-Preview]] — source article
- [[Date-Range-Beyond-Available-Data]] — handling date tables that extend beyond actual data
