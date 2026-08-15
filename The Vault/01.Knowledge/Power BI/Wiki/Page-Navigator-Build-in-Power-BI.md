---
created: 2026-08-13
source: Design Meets Data: Building Engaging Power BI Report Navigation
note_type: pattern
tags: [power-bi, report-design, navigation, page-navigator, ui-pattern, visual-design]
---

# Page Navigator Build in Power BI

<!-- Native Page Navigator component: positioning, sizing, state-based styling, and accent bar configuration. -->

## Overview

Power BI's Page Navigator is a native button-type object that generates an interactive navigation menu automatically from report pages. It requires minimal setup and automatically updates when pages are added or removed — making it the lowest-maintenance navigation option.

## Adding the Page Navigator

1. Insert tab → Buttons dropdown → Navigator → **Page navigator**
2. Place on the navigation pane (typically left side of canvas)

## Navigation Pane Setup

```
Navigation pane dimensions:
  Width:  140px
  Height: full canvas height

  Logo area rectangle:
    Width:  140px
    Height: 40px
    Fill:   accent color (e.g. #6CBE4B)

  Page Navigator object:
    Width:  130px
    Height: page_count × 35px  (e.g. 3 pages → 105px)
    X position: 10
    Y position: 100
```

## Orientation

Format pane → Grid layout → **Orientation: Vertical**

## Page Display Options

| Property | Group | Effect |
|----------|-------|--------|
| Show hidden pages | Options | Includes hidden pages in navigation |
| Show tooltip pages | Options | Includes tooltip-only pages |
| Show all by default | Options | All pages visible unless toggled off |
| Per-page toggles | Show | Explicitly control which pages appear |

## Height Calculation

```
navigator_height = number_of_pages × 35px
```

Adjust height based on page count — too small and items overflow; too large and unused space appears.

## State-Based Styling

Use **Apply settings to State** dropdown to configure each state independently.

| State | Font | Font Color | Fill | Accent Bar |
|-------|------|-----------|------|-----------|
| Default | Segoe UI | Theme1 60% lighter | Theme1 dark | Off |
| Hover | Segoe UI Semibold | White | Theme1 25% darker | Off |
| Press | Segoe UI Semibold | Theme1 50% darker | White | Off |
| Selected | Segoe UI Semibold | Theme1 50% darker | White | Right, 6px, accent green |

**Selected state accent bar:** Position = Right, Color = #6CBE4B (accent green), Width = 6px — this creates the visual indicator of the active page without obscuring the label.

## Related

- [[Navigation-Approaches-Figma-vs-Native-vs-Page-Navigator]] — comparison of all three navigation approaches with performance, maintenance, and design flexibility tradeoffs
- [[Bookmark-Navigator-for-Visual-Type-Switching]] — bookmark-based navigation pattern (different approach)
