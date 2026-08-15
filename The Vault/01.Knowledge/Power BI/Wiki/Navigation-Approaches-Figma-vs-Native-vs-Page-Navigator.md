---
created: 2026-08-13
source: Design Meets Data: Building Engaging Power BI Report Navigation
note_type: comparison
tags: [power-bi, report-design, navigation, figma, page-navigator, bookmarks, comparison]
---

# Navigation Approaches: Figma vs Native vs Page Navigator

<!-- Three approaches to building report navigation in Power BI — performance, maintenance, and design flexibility tradeoffs. -->

## The Three Approaches

| Approach | Method | Maintenance Model |
|----------|--------|-----------------|
| Figma | Design in Figma → export SVG → import as images into Power BI | External design tool + Power BI |
| Native shapes + buttons | Build navigation entirely in Power BI using shapes, buttons, and bookmarks | Power BI only |
| Page Navigator | Use Power BI's built-in Page Navigator component | Native, automatic |

## Performance

| Approach | Load Behaviour |
|----------|--------------|
| Figma | Fastest — all shapes pre-rendered as image; no per-object rendering overhead |
| Native shapes + buttons | Slower — each shape and component loads independently each page view |
| Page Navigator | Fastest native — fully integrated, minimal overhead |

Figma wins on performance because the report doesn't have to render individual objects on each page load.

## Maintenance Effort

| Approach | Adding a Page | Updating Design |
|----------|-------------|---------------|
| Figma | High: redesign in Figma → re-export → re-import → re-integrate | High: full round-trip through external tool |
| Native shapes + buttons | Manual: add new shape/button, update bookmarks | Manual: adjust each object individually |
| Page Navigator | Easiest: page added to report → navigator updates automatically | Only size adjustment needed |

**Page Navigator is the clear winner on maintenance** — pages are picked up automatically. Only the object's height needs manual adjustment based on page count.

## Design Flexibility

| Approach | Customisation |
|----------|--------------|
| Figma | Highest — any design concept possible; limited only by Figma's capability |
| Native shapes + buttons | High — more flexibility than Page Navigator; constrained by Power BI's shape/button options |
| Page Navigator | Limited — prioritises ease and maintenance over design control |

Page Navigator trades design control for simplicity. Native shapes + buttons offer a middle ground.

## When to Use Each

```
Use Page Navigator when:
  - Navigation is functional (not a brand/design showcase)
  - Report has many pages that change frequently
  - Low maintenance burden is the priority
  - Standard Power BI aesthetics are acceptable

Use Native shapes + buttons when:
  - Design needs exceed Page Navigator's options
  - Report pages are relatively stable
  - Team has Power BI expertise but no Figma access

Use Figma when:
  - Navigation is a key design element (executive/brand-forward reports)
  - Design consistency across multiple reports matters
  - Team has both Figma and Power BI skills
  - Can absorb the higher maintenance cost
```

## Related

- [[Page-Navigator-Build-in-Power-BI]] — detailed build steps for the Page Navigator approach
- [[Bookmark-Navigator-for-Visual-Type-Switching]] — bookmark-based navigation pattern (native shapes + buttons category)
