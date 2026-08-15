---
title: "10 CSS Tricks Used in This Modern HTML KPI Card in Power BI"
source: "https://medium.com/microsoft-power-bi/10-css-tricks-used-in-this-modern-html-kpi-card-in-power-bi-3c71bd836012"
author:
  - "[[Esther]]"
published: 2026-03-31
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
A breakdown of the exact CSS techniques behind this clean and modern KPI card UI.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*01sF8WnGaZUQN9YwdouESQ.png)

These are a few simple techniques I regularly use in KPI card design — hopefully, you’ll find them useful too.

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## 1\. Gradient Background

This card uses a smooth blue gradient to create depth.

```c
.card {
  background: linear-gradient(135deg, #2b5cff, #3a7bff);
}
```

## 2\. Rounded Corners

Soft edges make the card feel modern.

```c
.card {
  border-radius: 16px;
}
```

## 3\. Soft Shadow

Gives the card a floating effect.

```c
.card {
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}
```

## 4\. Clear Visual Hierarchy

Large number → small label → subtle footer.

```c
.title {
  font-size: 14px;
  opacity: 0.8;
}
```
```c
.value {
  font-size: 32px;
  font-weight: bold;
}
```

## 5\. Accent Color for Growth

Green instantly communicates positive change.

```c
.growth {
  color: #00ffb3;
}
```

## 6\. Progress Bar Indicator

Adds visual feedback for performance.

```c
.bar {
  height: 4px;
  background: rgba(255,255,255,0.2);
  border-radius: 10px;
}
```
```c
.bar::after {
  content: "";
  display: block;
  width: 40%;
  height: 100%;
  background: #00ffb3;
}
```

## 7\. Subtle Divider Line

Separates sections without clutter.

```c
.divider {
  height: 1px;
  background: rgba(255,255,255,0.15);
  margin: 10px 0;
}
```

## 8\. Minimal Icon Usage

Small icon adds context without distraction.

```c
.icon {
  width: 20px;
  opacity: 0.8;
}
```

## 9\. Consistent Spacing

Clean layout comes from good spacing.

```c
.card {
  padding: 20px;
}
```
```c
.card * {
  margin-bottom: 8px;
}
```

## 10\. Smooth Font Rendering

Modern UI uses clean, readable fonts.

```c
body {
  font-family: 'Inter', sans-serif;
}
```

## Full Code:

```c
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

  <!-- 🔥 progress bar -->
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

/* hover effect */
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
  0% { transform: scale(1); opacity: 0.1; }
  50% { transform: scale(1.2); opacity: 0.2; }
  100% { transform: scale(1); opacity: 0.1; }
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

/* change */
.change {
  font-size: 18px;
}

.positive { color: #86efac; }
.negative { color: #fecaca; }

/* 🔥 progress bar */
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

/* footer */
.footer {
  font-size: 13px;
  opacity: 0.6;
}
</style>
"
```

## 👉Final Thoughts

This card works because of **small, well-combined details**:

- gradient + shadow
- strong typography
- subtle indicators

Individually simple — together, they feel premium.

Try recreating this and tweak colors to match your own dashboard.

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----3c71bd836012---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** Data Visualization

**Tags:** Tutorial, Data Visualization