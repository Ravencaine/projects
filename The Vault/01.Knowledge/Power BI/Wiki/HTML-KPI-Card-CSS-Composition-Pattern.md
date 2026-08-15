---
created: 2026-08-10
updated: 2026-08-10
source: 10 CSS Tricks Used in This Modern HTML KPI Card in Power BI
source_url: https://medium.com/microsoft-power-bi/10-css-tricks-used-in-this-modern-html-kpi-card-in-power-bi-3c71bd836012
note_type: pattern
tags: [powerbi, html-content, css, kpi, visualization]
---

# HTML KPI Card — CSS Composition Pattern

Combine 10 CSS techniques inside a single Power BI DAX measure returning HTML to build a polished, modern KPI card.

## Purpose

Deliver a self-contained KPI card (value + change + progress bar + footer) in Power BI without a custom visual. The card uses flexbox layout, gradient backgrounds, soft shadows, and subtle animations — all via inline CSS inside a DAX measure.

## Components

1. Flexbox column layout (`display: flex; flex-direction: column; justify-content: space-between`)
2. Gradient background (`linear-gradient`)
3. Soft box-shadow
4. Visual hierarchy (large value → small label → subtle footer)
5. Accent color for positive/negative change
6. Progress bar via CSS `::after` pseudo-element
7. Subtle divider line
8. Minimal icon usage
9. Consistent padding
10. Hover lift effect with `transform` + shadow transition

## Structure

```dax
KPI Orders Pro =
VAR Orders = [Total Orders]
VAR Change = [Orders Change %]
VAR Class = IF(Change > 0, "positive", "negative")
VAR Arrow = IF(Change > 0, "▲", "▼")
VAR AbsChange = ABS(Change)

RETURN
"
<div class='card orders'>

  <div class='header'>
    <div class='title'>Orders</div>
    <div class='icon'>📦</div>
  </div>

  <div class='value'>" & FORMAT(Orders, "#,##0") & "</div>

  <div class='change " & Class & "'>
    " & Arrow & " " & FORMAT(Change, "0.00%") & "
  </div>

  <div class='bar'>
    <div class='fill' style='width:" & FORMAT(AbsChange, "0%") & "'></div>
  </div>

  <div class='footer'>
    Monthly performance
  </div>

</div>

<style>
.card {
  padding: 28px;
  border-radius: 20px;
  color: white;
  font-family: Segoe UI;
  min-height: 260px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.6);
}

.orders {
  background: linear-gradient(135deg, #1e3a8a, #2563eb);
}

/* glow */
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

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.title {
  font-size: 15px;
  opacity: 0.8;
}

.icon {
  font-size: 22px;
}

.value {
  font-size: 44px;
  font-weight: bold;
}

.change {
  font-size: 18px;
}

.positive { color: #86efac; }
.negative { color: #fecaca; }

/* progress bar */
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

.footer {
  font-size: 13px;
  opacity: 0.6;
}
</style>
"
```

## Key Technique: `::before` Glow + `::after` Progress Fill

The glow effect uses absolute positioning with a large circular `::before` pseudo-element and a `@keyframes pulse` animation. The progress bar uses `overflow: hidden` on the parent bar div to clip the `::after`-like fill div.

## Variations

- Swap gradient colors per KPI type: blue for orders, green for revenue, orange for costs
- Use emoji or SVG inline icons
- Adjust `border-radius` (16px–24px) for softer/sharper card feel
- Replace pulse animation with a static glow for performance on lower-end hardware

## Related

- [[KPI-Card-Pulse-Glow-Animation]]
- [[Progress-Bar-Indicator-CSS-Trick]]
- [[Advanced-KPI-Cards]]
