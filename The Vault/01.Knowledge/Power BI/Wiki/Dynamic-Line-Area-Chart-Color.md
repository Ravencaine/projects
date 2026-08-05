---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: pattern
tags: [dynamic-color, area-chart, line-chart, overlay, font-awesome]
related: [Process-Tracker-Dynamic-Fill, Color-Coding-4-Techniques, HTML-Content-Visual]
---

# Dynamic Line/Area Chart Color (Overlay Technique)

Overlays two identical area/line charts on top of each other — one showing "positive" values in green, the other showing "negative" values in red — to simulate per-segment conditional coloring that Power BI does not natively support.

## The Problem

Power BI's native line and area charts do not support per-series conditional formatting based on value thresholds or metric performance. You cannot natively make a line turn red when it falls below a target and green when above.

## The Solution

1. Build the primary area chart with all data.
2. Duplicate the visual.
3. Apply a visual-level filter to each duplicate showing only the relevant segment.
4. Assign a single solid fill color to each duplicate (green = above target, red = below target).
5. Overlay the charts exactly on top of each other.

## Implementation

**DAX measure for the threshold indicator:**
```dax
Is Above Target =
    IF([Metric] >= [Target], 1, BLANK())
```

**DAX measure for the below-target indicator:**
```dax
Is Below Target =
    IF([Metric] < [Target], 1, BLANK())
```

**Visual 1:** Area chart — Y-axis: `Is Above Target`, fill: green (#76E3B4)
**Visual 2:** Area chart — Y-axis: `Is Below Target`, fill: red (#EE6064)
**Filter pane:**
- Visual 1 → `Is Above Target` = 1
- Visual 2 → `Is Below Target` = 1

**Transparency:** Set fill transparency to 60–70% to blend where segments overlap.

## Advanced: Dynamic Threshold via SWITCH

```dax
Color Fill =
    SWITCH(
        TRUE(),
        [Metric] >= [Target], "#76E3B4",
        [Metric] >= [Warning Threshold], "#F5A623",
        "#EE6064"
    )
```

Create three overlays for three color states.

## Notes

- Works for both line and area charts.
- Synchronize X and Y axes across all overlays — set fixed min/max via DAX measures to prevent the overlaid charts from rescaling independently.
- Use the **Selection pane** to group the overlays and control visibility from a single bookmark if needed.
- Bittar also uses the **HTML Content** custom visual as an alternative — see [[HTML-Content-Visual]] for the Font Awesome CDN approach.
- For bar charts, Power BI natively supports conditional formatting via field values, so the overlay is unnecessary.

## Related

- [[Dynamic-Color-Coding-Bar-Charts]] — native conditional formatting for bar charts
- [[Color-Coding-4-Techniques]] — full reference of four conditional color techniques
- [[HTML-Content-Visual]] — Font Awesome icon rendering via DAX + HTML Content visual
