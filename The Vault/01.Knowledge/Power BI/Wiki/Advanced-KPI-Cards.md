---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [KPI-card, card-visual, UNICHAR, dynamic-text, shape-compositing]
related: [UNICHAR, FORMAT, Process-Tracker-Dynamic-Fill]
---

# Advanced KPI Cards (Power BI)

Build multi-element KPI cards using the Card visual, Shape objects, and DAX measures that render dynamic text with trend arrows and formatted values.

## Components

| Component | Source | Purpose |
|-----------|--------|---------|
| Card visual | Native | Main metric value (formatted) |
| Shape (rectangle) | Insert → Shapes | Card background container |
| Text box | Insert → Text box | Labels and context |
| Card visual | Native | Secondary metric (variance) |
| Shape (rectangle) | Native | Trend indicator strip |

## DAX Measures

**Main KPI value:**
```dax
KPI Value =
    FORMAT([Total Sales], "$#,##0")
```

**Variance with UNICHAR arrow:**
```dax
KPI Variance =
    VAR _Variance = [Sales vs Target]
    VAR _Formatted =
        FORMAT(_Variance, "+0.0%;-0.0%;0.0%")
    VAR _Arrow =
        IF(_Variance > 0, UNICHAR(9650),
        IF(_Variance < 0, UNICHAR(9660),
        UNICHAR(9651)))
    RETURN
        _Arrow & " " & _Formatted
```

**Dynamic title:**
```dax
KPI Title =
    SELECTEDVALUE('KPI Selection'[KPI Name], "Revenue")
```

## Compositing Steps

1. Insert a rounded-corner rectangle (dark background).
2. Add a Card visual on top for the main value — set font to `Segoe UI Semibold`, size 28–36pt.
3. Add a second Card for the variance — use the `KPI Variance` measure, smaller font.
4. Add a thin accent-colored rectangle on the left edge as a status indicator strip.
5. Add text boxes for labels ("vs Target", "vs Prior Period").
6. Align all elements to the card's grid.
7. Repeat for each KPI.

## Notes

- Use the **Card visual's** `Callout value` formatting to control the main number's appearance separately from the label.
- Bittar's KPI card technique combines `UNICHAR` for trend arrows with `FORMAT` for percentage formatting — the variance card shows "▲ +12.3%" in green or "▼ -5.1%" in red.
- The shape-based card background allows full control over colors, rounded corners, and shadows (via border).
- For consistent sizing, set each card group to the same height and use Snap to Grid.

## Related

- [[UNICHAR]] — trend arrows
- [[FORMAT]] — format numbers and percentages
- [[Process-Tracker-Dynamic-Fill]] — shape compositing with DAX color
