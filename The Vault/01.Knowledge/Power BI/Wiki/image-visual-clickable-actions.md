---
created: 2026-08-02
source: The New Image Visual in Power BI Is a Quiet Game Changer
note_type: pattern
tags: [power-bi, image-visual, actions, navigation, bookmarks, drillthrough, ux]
---

# Image Visual Clickable Actions — Navigation, Tooltips, Pop-ups

The Image visual supports binding actions directly to images — replacing buttons, shapes, and invisible overlays.

## Supported Actions

| Action | Description |
|--------|-------------|
| **Navigate to page** | Jump to another report page |
| **Open tooltip** | Trigger a tooltip/popover |
| **Bookmark** | Activate a saved bookmark state |
| **Show/hide help** | Toggle help panel visibility |
| **Pop-up overlay** | Display overlay content |
| **Drill through** | Navigate to a drill-through page |

## Use Cases

### Navigation bar (SVG icons)
```dax
Nav Icon :=
    UDF_EncodeSVG(
        IF(
            SELECTEDVALUE('Nav'[Page]) = "Home",
            "<svg><!-- home active icon --></svg>",
            "<svg><!-- home inactive icon --></svg>"
        )
    )
```
Bind `Nav Icon` → Image visual → action: Navigate to page (Home).

### Help button with nudge
- Tiny "?" SVG icon
- Action: Show bookmark (help panel)
- Subtle pulsing nudge animation draws attention

### Insight callout
- "Show analysis" SVG badge
- Action: Activate bookmark revealing analysis pane
- Lights up only when insights are available (measure-driven)

## Related

- [[image-visual-dynamic-binding]] — measure-driven image state
- [[svg-pill-pattern-udf-based]] — SVG icons via UDF
