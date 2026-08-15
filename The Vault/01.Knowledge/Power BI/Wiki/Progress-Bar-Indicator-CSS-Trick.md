---
created: 2026-08-10
updated: 2026-08-10
source: 10 CSS Tricks Used in This Modern HTML KPI Card in Power BI
source_url: https://medium.com/microsoft-power-bi/10-css-tricks-used-in-this-modern-html-kpi-card-in-power-bi-3c71bd836012
note_type: pattern
tags: [powerbi, html-content, css, progress-bar, kpi]
---

# Progress Bar via CSS `::after` Fill

Render a dynamic-width progress bar inside a Power BI HTML KPI card using a parent `overflow: hidden` clip technique.

## Purpose

Visualises a KPI metric (e.g., % change, target attainment) as a filled bar inside an HTML card. The fill width is set inline via DAX `FORMAT()` and dynamically reflects the measure value.

## Components

1. Parent `.bar` div — defines the track, sets height and background
2. `overflow: hidden` — clips any content that overflows the bar boundaries
3. Child `.fill` div — positioned inside the track, width set inline by DAX
4. Gradient fill — `linear-gradient` for a polished colour transition
5. `border-radius` — rounds the ends of both track and fill

## Structure

**HTML (inside DAX measure):**
```html
<div class='bar'>
  <div class='fill' style='width: 40%'></div>
</div>
```

**CSS:**
```css
.bar {
  height: 6px;
  background: rgba(255,255,255,0.15);
  border-radius: 10px;
  overflow: hidden;
}

.fill {
  height: 100%;
  background: linear-gradient(90deg, #22c55e, #4ade80);
}
```

**DAX (dynamic width):**
```dax
<div class='fill' style='width:" & FORMAT(ABS([Orders Change %]), "0%") & "'></div>
```

`ABS()` is used so the bar always fills forward regardless of positive or negative change direction. `FORMAT(...,"0%")` outputs values like `0%`, `40%`, `100%`.

## Variations

- **Colour by direction:** add conditional CSS classes `.positive` / `.negative` to the fill div:
  ```css
  .positive .fill { background: linear-gradient(90deg, #22c55e, #4ade80); }
  .negative .fill { background: linear-gradient(90deg, #ef4444, #f87171); }
  ```
- **Thinner bar:** reduce `height` to `4px` for a more subtle indicator
- **Multi-segment bar:** stack multiple `.fill` divs inside the same `.bar` for comparing two metrics side by side

## Related

- [[HTML-KPI-Card-CSS-Composition-Pattern]]
- [[KPI-Card-Pulse-Glow-Animation]]
