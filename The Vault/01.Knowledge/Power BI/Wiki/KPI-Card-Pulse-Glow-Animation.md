---
created: 2026-08-10
updated: 2026-08-10
source: 10 CSS Tricks Used in This Modern HTML KPI Card in Power BI
source_url: https://medium.com/microsoft-power-bi/10-css-tricks-used-in-this-modern-html-kpi-card-in-power-bi-3c71bd836012
note_type: pattern
tags: [powerbi, html-content, css, animation, kpi]
---

# KPI Card — Pulse Glow Animation

Add a subtle pulsing glow to an HTML KPI card in Power BI using a CSS `::before` pseudo-element with a `@keyframes` animation.

## Purpose

Creates a "living" card that breathes — a large, softly blurred circular glow in the top-right corner pulses in size and opacity. Signals a premium, modern feel without impacting the data itself.

## Components

1. `::before` pseudo-element — absolutely positioned circle
2. `border-radius: 50%` — makes the element a perfect circle
3. `position: absolute` + `overflow: hidden` on parent — clips the circle within the card
4. `@keyframes pulse` — three-state animation: scale 1 → 1.2 → 1

## Structure

```css
/* glow circle */
.orders::before {
  content: '';
  position: absolute;
  width: 240px;
  height: 240px;
  background: rgba(255,255,255,0.08);
  border-radius: 50%;
  top: -80px;
  right: -80px;
  animation: pulse 4s infinite;
}

@keyframes pulse {
  0%   { transform: scale(1);    opacity: 0.1; }
  50%  { transform: scale(1.2);  opacity: 0.2; }
  100% { transform: scale(1);   opacity: 0.1; }
}
```

Key values: `top: -80px` and `right: -80px` position the 240px circle just outside the top-right corner so only the bottom-left quarter bleeds into the card. `opacity` range 0.1–0.2 keeps it subtle.

## Variations

- **Faster pulse:** change `4s` to `2s` or `1.5s` for more energy
- **Static glow:** remove the `animation` line for a constant, non-animated glow — better performance on complex reports
- **Color glow:** replace `rgba(255,255,255,0.08)` with a tinted color to match the card's gradient (e.g., `rgba(59,130,246,0.15)`)
- **Corner position:** change `top`/`right` to `bottom`/`left` for opposite corner glow

## Related

- [[HTML-KPI-Card-CSS-Composition-Pattern]]
- [[Progress-Bar-Indicator-CSS-Trick]]
