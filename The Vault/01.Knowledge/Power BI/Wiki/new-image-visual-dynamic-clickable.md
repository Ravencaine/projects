---
created: 2026-08-02
source: The New Image Visual in Power BI Is a Quiet Game Changer
note_type: pattern
tags: [powerbi, pattern, image-visual, dynamic-image, svg, action, navigation, accessibility]
---

# New Image Visual: Dynamic Images, Clickable Actions, SVG, Accessibility

Microsoft revamped the Image visual (late 2025) into a first-class design component — replacing button/shape hacks with a native, dynamic, action-capable image container.

**What changed:**

- **Bound to fields or DAX measures:** not just static URLs; accepts calculated URLs or SVG strings
- **Dynamic image types:** KPI icons, status pills, arrow indicators, alerts, navigation icons, category logos, SVG strings
- **Fit/Fill/Cover/Crop controls:** consistent sizing without stretching or warping
- **Clickable actions:** navigate to pages, open tooltips, trigger bookmarks, show/hide panels, drill-through
- **Native Alt text:** screen reader support, semantic meaning, WCAG accessibility
- **SVG rendering:** faster, sharper, pixel-tear-free

**What it replaces:**

| Old workaround | New native solution |
|---|---|
| Table visual as image container | Image Visual bound to measure |
| Buttons with icons | Image Visual with action |
| Shape overlays | Image Visual with transparent background |
| Bookmark toggles | Image Visual with bookmark action |
| Invisible transparent shapes | Image Visual with action |

**Quick wins (under 5 minutes each):**

- Dynamic status dots (color changes by rule)
- Help button with nudge animation
- SVG navigation bar (active page = different fill)
- Category logos switching by selection
- Dynamic rating stars (surveys, HR, product feedback)

> See `dax-driven-dynamic-image-measure.md` for the DAX side — one measure, infinite visual states.
