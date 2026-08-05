---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: pattern
tags: [powerbi, pattern, chart, switch, button-slicer, dynamic]
---

# Dynamic Chart — SWITCH on Button Slicer

A clustered column chart whose axis values, colors, title, and subtitle all change dynamically based on the selected button in a button slicer. All four properties are bound to SWITCH-based DAX measures that read `SELECTEDVALUE(Highlights[Order])`.

## Purpose

When a KPI card has multiple highlights (e.g., High OT Flag, Biggest Rise, Top Unit, Lowest Fill Rate), each one requires a different metric, color logic, and descriptive title in the supporting chart. Rather than build separate charts for each scenario, one chart is controlled by four measures that swap based on the button selection.

## Components

| Property | Bound to | Formula |
|----------|----------|---------|
| Values | `Column Value` measure | SWITCH on `SELECTEDVALUE(Highlights[Order])` |
| Conditional formatting (Data Colors) | `Column Color` measure | SWITCH on TRUE + highlight order + threshold comparison |
| Title | `Graph Title` measure | SWITCH returning static strings |
| Subtitle | `Graph Subtitle` measure | SWITCH returning formatted detail strings |

## Structure

```
Button Slicer (Highlights[Order])
    ↓ SELECTEDVALUE(Highlights[Order])
    ├→ Column Value  → metric to display
    ├→ Column Color  → conditional red/green/blue
    ├→ Graph Title   → static title string
    └→ Graph Subtitle → detail string
```

## Example

```dax
Column Value =
    SWITCH(
        SELECTEDVALUE(Highlights[Order]),
        1, [High OT Employees (Last 7 Days)],
        2, [OT Hours per FTE Variance %],
        3, [OT Hours This Week],
        4, [Filled Rate % This Week]
    )

Column Color =
    SWITCH(
        TRUE(),
        SELECTEDVALUE(Highlights[Order]) = 1
            && [High OT Employees (Last 7 Days)] = [Most Employees Flagged for High OT per Unit],
            [_Color Red],
        SELECTEDVALUE(Highlights[Order]) = 2
            && [OT Hours per FTE Variance %] <= 0,
            [_Color Green],
        SELECTEDVALUE(Highlights[Order]) = 2
            && [OT Hours per FTE Variance %],
            [_Color Red],
        SELECTEDVALUE(Highlights[Order]) = 3
            && [OT Hours This Week] = [Highest OT Hours per Unit],
            [_Color Red],
        SELECTEDVALUE(Highlights[Order]) = 4
            && [Filled Rate % This Week] = [Lowest Fill Rate],
            [_Color Red],
        [_Color Medium Blue]
    )

Graph Title =
    SWITCH(
        SELECTEDVALUE(Highlights[Order]),
        1, "Employees with >10h of OT This Week",
        2, "Variation of OT Hours per FTE Since Last Week",
        3, "OT Hours This Week",
        4, "Shift Fill Rate by Department"
    )
```

## Variations

- Swap the conditional color logic for a dedicated `Color Measure` folder in the model with named constants (`_Color Red`, `_Color Green`, `_Color Medium Blue`)
- Extend the subtitle measure to include shift-level attribution — add per-highlight detail DAX measures stored under `Graph/Subtitles`
- Use `KEEPFILTERS` inside the color SWITCH to correctly handle multi-selection on other slicers

## Related

- [[Button-Slicer]]
- [[Highlights-Table-Unconnected-Helper-Table]]
- [[Dynamic-KPI-Card-Layout]]
- [[dynamic-measure-selection-in-dax]]
