---
created: 2026-08-10
updated: 2026-08-10
source: 10 CSS Tricks Used in This Modern HTML KPI Card in Power BI
source_url: https://medium.com/microsoft-power-bi/10-css-tricks-used-in-this-modern-html-kpi-card-in-power-bi-3c71bd836012
note_type: source
tags: [powerbi, html-content, css, kpi, visualization]
---

# Source: Esther — 10 CSS Tricks KPI Card

> **Type:** article
> **Author:** Esther
> **Published:** 2026-03-31
> **URL:** https://medium.com/microsoft-power-bi/10-css-tricks-used-in-this-modern-html-kpi-card-in-power-bi-3c71bd836012
> **Routed to:** Power BI

## Summary

Breaks down 10 CSS techniques used inside a DAX measure to render a modern HTML KPI card via the Power BI Card visual. Techniques cover layout (flexbox), colour (gradients, accent colours), depth (shadows, glow), motion (hover lift, pulse animation), and typography hierarchy. Full DAX measure with embedded HTML/CSS provided.

## Key Claims

- CSS gradient backgrounds create depth without images
- `border-radius: 16px`–`24px` gives a modern card feel
- Soft `box-shadow` produces a floating effect
- Visual hierarchy: large number (44px) → label (15px, 0.8 opacity) → footer (13px, 0.6 opacity)
- Green accent (`#86efac`) communicates positive change; red (`#fecaca`) for negative
- CSS `::after` / child div progress bar with `overflow: hidden` clip
- Hover state with `transform: translateY(-6px)` + enhanced shadow
- Pulsing glow via `::before` pseudo-element + `@keyframes` animation
- Flexbox column layout (`display: flex; flex-direction: column; justify-content: space-between`) keeps card sections anchored
- Consistent `padding` (20px–28px) and `margin-bottom` on children maintain clean spacing

## Notable Details

- Emoji icons used inline: `📦` for orders. Work in Power BI HTML Content rendering.
- `Segoe UI` used instead of `Inter` — appropriate for Windows-native Power BI deployment.
- `min-height: 260px` on the card prevents content jumping when values change.
- `transition` on the card (`transform` and `box-shadow`) makes the hover animation smooth.
- Glow circle uses `position: absolute; top: -80px; right: -80px` on a 240px circle so only the bottom-left quarter bleeds into the card.
- `transition: 0.3s ease` is the standard transition timing for hover effects.
- Source provides no DAX pattern beyond the HTML/CSS shell — the data logic (VAR values) is minimal stub code.

## Extracted Notes

Links to notes derived from this source:

- [[HTML-KPI-Card-CSS-Composition-Pattern]] — `pattern` — Full KPI card composition: 10 CSS techniques combined in a DAX measure
- [[KPI-Card-Pulse-Glow-Animation]] — `pattern` — CSS pulse glow via `::before` + `@keyframes`
- [[Progress-Bar-Indicator-CSS-Trick]] — `pattern` — Progress bar via `overflow: hidden` + child fill div
- [[KPI-Card-DAX-Measure-Full-HTML-CSS]] — `snippet` — Copy-paste DAX measure returning complete HTML KPI card
- [[10-CSS-KPI-Card-Techniques-Reference]] — `reference` — All 10 techniques in a lookup table

## Metadata

| Field | Value |
|-------|-------|
| Source file | 10 CSS Tricks Used in This Modern HTML KPI Card in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Word count | ~310 |
