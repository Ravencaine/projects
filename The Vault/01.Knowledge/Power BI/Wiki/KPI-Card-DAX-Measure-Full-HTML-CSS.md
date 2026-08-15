---
created: 2026-08-10
updated: 2026-08-10
source: 10 CSS Tricks Used in This Modern HTML KPI Card in Power BI
source_url: https://medium.com/microsoft-power-bi/10-css-tricks-used-in-this-modern-html-kpi-card-in-power-bi-3c71bd836012
note_type: snippet
tags: [powerbi, dax, html-content, kpi]
---

# KPI Card DAX Measure — Full HTML/CSS Boilerplate

Copy-paste DAX measure returning a complete HTML KPI card with gradient background, glow pulse animation, progress bar, and hover lift effect.

## Code

```dax
KPI Card =
VAR Value = [Total Sales]
VAR Change = [Sales Change %]
VAR Label = "Total Sales"
VAR Icon = "📊"
VAR Footer = "vs last period"

VAR Class = IF(Change > 0, "positive", "negative")
VAR Arrow = IF(Change > 0, "▲", "▼")
VAR AbsChange = ABS(Change)

RETURN
"
<div class='card orders'>

  <div class='header'>
    <div class='title'>" & Label & "</div>
    <div class='icon'>" & Icon & "</div>
  </div>

  <div class='value'>" & FORMAT(Value, "#,##0") & "</div>

  <div class='change " & Class & "'>
    " & Arrow & " " & FORMAT(Change, "0.00%") & "
  </div>

  <div class='bar'>
    <div class='fill' style='width:" & FORMAT(AbsChange, "0%") & "'></div>
  </div>

  <div class='footer'>" & Footer & "</div>

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

## When to Use

Use inside a Card visual with "Show value" enabled and the measure applied to the Card's field well. Works in any Power BI report where a single key metric needs to stand out.

## Variations

- **Revenue card:** change `.orders` class to `.revenue` and gradient to `linear-gradient(135deg, #065f46, #10b981)`
- **Cost card:** gradient to `linear-gradient(135deg, #7f1d1d, #ef4444)`
- **Remove animation:** delete the `.orders::before` block and `@keyframes pulse` for a static card

## Related

- [[HTML-KPI-Card-CSS-Composition-Pattern]]
- [[KPI-Card-Pulse-Glow-Animation]]
- [[Progress-Bar-Indicator-CSS-Trick]]
