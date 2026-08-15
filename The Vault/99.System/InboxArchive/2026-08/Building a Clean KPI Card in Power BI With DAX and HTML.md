---
title: "Building a Clean KPI Card in Power BI With DAX and HTML"
source: "https://medium.com/microsoft-power-bi/building-a-clean-kpi-card-in-power-bi-with-dax-and-html-dfc4a0f934ea"
author:
  - "[[Esther]]"
published: 2026-03-28
created: 2026-08-03
description: "More"
Processed: "Unprocessed"
---
![](99.System/Attachments/1!2uRCXN1jl4vIY1v_o84vIQ.png.webp)

KPI Card in HTML and native Power BI Visual

Most Power BI dashboards are perfectly functional, but they often feel a bit mechanical. You get the numbers, maybe a chart or two, but the experience rarely feels intentional or thoughtfully designed.

I wanted to experiment with something slightly different: taking a simple KPI and turning it into a small, well-structured UI component using only DAX and HTML — no custom visuals, no external tools.

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## What I wanted to achieve

Instead of just showing a number, the goal was to create a KPI card that:

- clearly highlights the main value
- provides context (growth, min, average, max)
- explains what is happening in plain language
- stays fully interactive with slicers and charts

## Step 1 — Start with the core measures

Before thinking about layout or styling, the most important part is having clean measures that respect filter context.

```c
Total Sales = SUM(Sales[Amount])
```
```c
Previous Sales =
CALCULATE(
    [Total Sales],
    DATEADD(Sales[Date], -1, MONTH)
)
```
```c
Growth % =
DIVIDE(
    [Total Sales] - [Previous Sales],
    [Previous Sales]
)
```

These measures are intentionally simple. There is no use of `ALL()`, because we want the KPI to react naturally to slicers and chart selections.

## Step 2 — Add logic for presentation

Next, we introduce a few variables that control how the KPI behaves visually.

```c
VAR Total = [Total Sales]
VAR Growth = [Growth %]
```
```c
VAR Arrow = IF(Growth >= 0, "▲", "▼")
VAR Color = IF(Growth >= 0, "#22c55e", "#ef4444")
```

At this point, we are not thinking about design yet, just about how the data should be interpreted and displayed.

We can also add a simple summary that turns numbers into a short explanation:

```c
VAR Summary =
IF(
    Growth > 0,
    "Sales are increasing compared to last month",
    "Sales declined compared to last month"
)
```

## Step 3 — Build the structure in HTML

Now we start shaping the card itself. It helps to think in sections: header, value, growth, details, and summary.

```c
RETURN
"
<div style='
  width:380px;
  padding:26px;
  border-radius:18px;
  background:#111827;
  color:white;
  font-family:sans-serif;
'>
"
```

This outer container defines the size, spacing, and overall look of the card.

## Step 4 — Show the main value

The main number should be the most prominent element.

```c
<div style='
  font-size:46px;
  font-weight:700;
  margin-bottom:8px;
  color:#fbbf24;
'>
  " & FORMAT(Total, "$#,##0") & "
</div>
```

The goal here is clarity: large size, strong contrast, and simple formatting.

## Step 5 — Add growth context

The KPI becomes much more useful when you add a comparison.

```c
<div style='display:flex;justify-content:space-between;margin-bottom:15px;'>
```
```c
<div style='
  color:" & Color & ";
  font-size:14px;
  font-weight:600;
'>
  " & Arrow & " " & FORMAT(Growth,"0.0%") & "
</div>
```
```c
<div style='font-size:12px;color:#6b7280;'>
  vs last month
</div>
```
```c
</div>
```

This small section adds immediate meaning to the number without overwhelming the layout.

## Step 6 — Add supporting statistics

To give more context, we include minimum, average, and maximum values.

```c
<div style='display:flex;justify-content:space-between;margin-bottom:14px;'>
```
```c
<div>
  <div style='font-size:10px;color:#6b7280;'>MIN</div>
  <div>" & FORMAT([Min Sales], "$#,##0") & "</div>
</div>
```
```c
<div>
  <div style='font-size:10px;color:#6b7280;'>AVG</div>
  <div>" & FORMAT([Avg Sales], "$#,##0") & "</div>
</div>
```
```c
<div>
  <div style='font-size:10px;color:#6b7280;'>MAX</div>
  <div>" & FORMAT([Max Sales], "$#,##0") & "</div>
</div>
```
```c
</div>
```

These values are not the focus, but they help the user understand the range and distribution.

## Step 7 — Add a simple summary

Finally, we include a short sentence that interprets the data.

```c
<div style='
  font-size:12px;
  color:#9ca3af;
  background:#020617;
  padding:10px;
  border-radius:10px;
'>
  " & Summary & "
</div>
```

This is a small detail, but it makes the KPI feel more complete and easier to understand.

## Interaction with the rest of the report

![](99.System/Attachments/1!hgBjn6INy4pRbxdEQpSWsg.gif)

One important detail is that this KPI is placed next to a native Power BI bar chart.

Because all measures respect filter context:

- the Date slicer filters both the KPI and the chart
- clicking on the chart updates the KPI
- selecting a range keeps everything in sync

There is no extra logic required — just clean measures and a proper model.

## Final thought

What started as a simple KPI turned into a small, reusable UI component. The main takeaway is not about HTML or styling, but about combining, clear structure, simple DAX and consistent interaction.

When those pieces come together, even a basic dashboard can feel much more thoughtful and usable.

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----dfc4a0f934ea---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** Data Visualization

**Tags:** Tutorial, Data Visualization