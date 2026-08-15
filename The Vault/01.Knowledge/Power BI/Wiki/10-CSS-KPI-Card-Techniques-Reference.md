---
created: 2026-08-10
updated: 2026-08-10
source: 10 CSS Tricks Used in This Modern HTML KPI Card in Power BI
source_url: https://medium.com/microsoft-power-bi/10-css-tricks-used-in-this-modern-html-kpi-card-in-power-bi-3c71bd836012
note_type: reference
tags: [powerbi, html-content, css, kpi, reference]
---

# 10 CSS KPI Card Techniques — Quick Reference

Ten CSS techniques used to build a modern HTML KPI card in Power BI via DAX.

## Quick Reference

| # | Technique | CSS Property | Value |
|---|-----------|--------------|-------|
| 1 | Gradient background | `background` | `linear-gradient(135deg, #1e3a8a, #2563eb)` |
| 2 | Rounded corners | `border-radius` | `16px`–`24px` |
| 3 | Soft shadow | `box-shadow` | `0 10px 25px rgba(0,0,0,0.2)` |
| 4 | Visual hierarchy | `font-size` + `opacity` | large value (44px) → label (15px, 0.8) → footer (13px, 0.6) |
| 5 | Accent colour | `color` | positive: `#86efac` / negative: `#fecaca` |
| 6 | Progress bar track | `height` + `background` + `border-radius` | `6px; rgba(255,255,255,0.15); 10px` |
| 7 | Divider line | `height` + `background` + `margin` | `1px; rgba(255,255,255,0.15); 10px 0` |
| 8 | Icon sizing | `width` / `font-size` | `20px` or `22px` |
| 9 | Consistent spacing | `padding` + `margin-bottom` on children | `20px`–`28px` padding |
| 10 | Font rendering | `font-family` | `'Inter', sans-serif` or `'Segoe UI'` |

## Additional Techniques (Full Card)

| Technique | CSS | Notes |
|-----------|-----|-------|
| Hover lift | `transform: translateY(-6px)` | paired with enhanced shadow on `:hover` |
| Pulse glow | `::before` + `@keyframes pulse` | `scale(1→1.2)` + `opacity(0.1→0.2)` over 4s |
| Progress fill | `overflow: hidden` on track + child div with inline `width` | clipped by parent |
| Flexbox layout | `display: flex; flex-direction: column; justify-content: space-between` | all content in card |

## CSS Colour Palette (Blue Card)

| Role | Hex |
|------|-----|
| Card background gradient | `#1e3a8a` → `#2563eb` |
| Positive change | `#86efac` |
| Negative change | `#fecaca` |
| Progress fill gradient | `#22c55e` → `#4ade80` |
| Bar track background | `rgba(255,255,255,0.15)` |
| Glow circle | `rgba(255,255,255,0.08)` |

## Related

- [[HTML-KPI-Card-CSS-Composition-Pattern]]
- [[KPI-Card-Pulse-Glow-Animation]]
- [[Progress-Bar-Indicator-CSS-Trick]]
- [[KPI-Card-DAX-Measure-Full-HTML-CSS]]
