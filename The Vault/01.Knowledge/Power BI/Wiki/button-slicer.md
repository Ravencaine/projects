---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: atomic
tags: [powerbi, slicer, button, ui]
---

# Button Slicer

A slicer visual in Power BI rendered as a list of clickable buttons instead of the default dropdown or list format.

## Definition

The Button Slicer is a slicer type (available from November 2023+) that displays its values as a set of formatted button tiles. It is used to drive DAX logic via `SELECTEDVALUE()` — the button selection changes the active filter context, which SWITCH statements read to alter measure outputs, chart axes, or text labels.

## Key Points

- Each button represents one value from a **disconnected helper table** — no relationship to the data model required
- The slicer header becomes the section title (e.g. "Key Observations")
- The Callout value label is bound to a DAX measure, so button text is fully dynamic
- Conditional formatting (fill, border, hover) is applied per-button for visual polish
- The underlying field drives `SELECTEDVALUE(HelperTable[Field])` in measures — selecting a button changes the return value of SELECTEDVALUE

## Examples

Binding a highlight measure to the Callout value label:
```
SELECTEDVALUE(Highlights[Order])  → returns 1, 2, 3, or 4
SWITCH(
    SELECTEDVALUE(Highlights[Order]),
    1, [High OT Flag Highlight],
    2, [Biggest Rise Highlight],
    3, [Top Unit Highlight],
    4, [Lowest Fill Rate Highlight]
)
```

## Related

- [[Highlights-Table-Unconnected-Helper-Table]]
- [[Dynamic-Chart-SWITCH-on-Button-Slicer]]
- [[New-Power-BI-Slicer-Features]]
