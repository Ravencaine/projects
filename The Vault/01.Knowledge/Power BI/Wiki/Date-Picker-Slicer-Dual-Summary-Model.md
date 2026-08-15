---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into Power BI reporting with the new date picker slicer option (Preview).md"
note_type: atomic
tags: [power-bi, date-picker, slicer, dual-summary, filter-range, selected-range]
---

# Date Picker Slicer — Dual Summary Model

> **Type:** atomic
> **Routed to:** Power BI
> **Primary source:** Microsoft Fabric / DataZoe — 2026-07-16

## Mental Model

The Date Picker Slicer maintains two independent summaries simultaneously:

| Summary | What it shows | Tells the user |
|---------|--------------|----------------|
| **Top** (Filtered Range) | The actual dates the data column is filtered to | "What am I actually seeing?" |
| **Bottom** (Selected Range) | The relative or manual range selected | "What did I pick?" |

## Why Two Summaries?

They can diverge — and both pieces of information matter:

- **Top summary diverges from bottom** when the relative range extends beyond available data
- **Top summary shows incompleteness** when the data has gaps or the date table has future dates
- The tooltip on the top summary explains why the filtered range is incomplete

## Key Design Principle

> The slicer always knows two things: **what it filtered to** (data reality) and **what the user picked** (selection intent).

Both are displayed so users can diagnose why a chart looks unexpected:
- Chart short? → Top summary shows filtered range is incomplete
- Top and bottom differ? → Relative range extended beyond available data

## Configuration

- Top summary: always visible by default
- Bottom summary: toggle off via Format pane → Text → Summary = Off (for compact layout)

## See Also

- [[Source-Date-Picker-Slicer-Preview]] — source article
- [[Date-Range-Beyond-Available-Data]] — scenario where top and bottom summaries diverge
