---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into Power BI reporting with the new date picker slicer option (Preview).md"
note_type: gotcha
tags: [power-bi, date-picker, slicer, future-dates, date-table, gotcha]
---

# Future Dates in Date Table — Misleading Relative Range Gotcha

> **Type:** gotcha
> **Routed to:** Power BI
> **Primary source:** Microsoft Fabric / DataZoe — 2026-07-16

## Problem

Date tables often extend into the future (for forecast periods, future planning, capacity models). When a Date Picker Slicer uses a relative range anchored to the date table's max date, it includes future dates with no actual data — causing a sharp, misleading decline at the end of the chart.

## Why It Happens

The Date Picker Slicer's relative range is calculated against the **date table's max date**, not the **max date with actual data**. If the date table runs to July 15 but sales end April 14, the relative range includes April 15 through July 15 — dates with zero transactions.

## How It Looks

A line chart that ends with a steep drop-off in mid-April — not because sales collapsed, but because the date table has future dates with no data after April 14.

## The Trap

The date table max (July 15) ≠ the data's max (April 14). The Date Picker Slicer's relative range anchor uses the date table max, so it extends into the future.

## Solution

Constrain the slicer with a Filter pane override — add a "is not blank" filter on the fact column directly in the slicer's filter area. This pins the relative range to the last date with actual data, regardless of what the date table contains.

See: [[Date-Range-Beyond-Available-Data]]

## Key Insight

A date table prepared for the future is correct design — but the Date Picker Slicer needs to be told to stop at real data, not at the date table boundary.

## See Also

- [[Source-Date-Picker-Slicer-Preview]] — source article
- [[Date-Range-Beyond-Available-Data]] — filter pane override workflow
