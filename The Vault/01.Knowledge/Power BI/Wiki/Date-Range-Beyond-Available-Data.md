---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into Power BI reporting with the new date picker slicer option (Preview).md"
note_type: workflow
tags: [power-bi, date-picker, slicer, filter-pane, is-not-blank, workflow]
---

# Date Range Beyond Available Data — Filter Pane Override Workflow

> **Type:** workflow
> **Routed to:** Power BI
> **Primary source:** Microsoft Fabric / DataZoe — 2026-07-16

## Problem

Date table extends into the future (for forecasts, future planning). When the date picker slicer uses a relative range, it includes future dates with no actual data — causing a misleading sharp decline at the boundary.

Example: Sales data ends April 14, date table extends to mid-July → relative range includes empty future dates → chart drops off misleadingly.

## Root Cause

Relative range is calculated against the date table's max date, not the max date with actual data.

## Solution

Use the Filter pane to constrain the slicer to only dates where data exists (is not blank).

## Steps

1. Select the **date picker slicer**
2. Open the **Filter pane** (right panel)
3. Drag the **fact column** (e.g., Units Sold) or its **measure** into the slicer's filter area
4. Set filter type to **Advanced filter**
5. Set condition: show items when the value **is not blank**
6. Select **Apply filter**

## Result

- Relative range now anchored to the **last date with actual data**, not the date table max
- Date picker continues to use the full date table for selection flexibility
- Year-over-year comparisons always use complete data periods

## Key Insight

The date picker slicer and the filter pane constraint work together:
- Slicer: drives user selection and display format
- Filter pane: constrains the actual data range

## See Also

- [[Source-Date-Picker-Slicer-Preview]] — source article
- [[Last-Full-Month-Date-Picker-Workflow]] — relative range configuration
- [[Partial-Month-Decline-Gotcha]] — related gotcha: incomplete current month
