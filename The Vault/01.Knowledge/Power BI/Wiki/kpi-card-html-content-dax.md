---
created: 2026-08-06
updated: 2026-08-06
source: Building a Clean KPI Card in Power BI With DAX and HTML.md
source_url: https://medium.com/microsoft-power-bi/building-a-clean-kpi-card-in-power-bi-with-dax-and-html-dfc4a0f934ea
note_type: pattern
tags: [power-bi, kpi, html-content, html, dax, card-visual, user-interface]
---

# KPI Card with HTML Content and DAX

Build a polished KPI card using HTML Content (a free custom visual) driven entirely by DAX measures — no external tools or custom visuals beyond HTML Content. The card shows: main value, growth %, min/avg/max, plain-language summary, and stays in sync with report slicers and chart selections.

## Purpose

Native Power BI KPI cards are functional but mechanical. An HTML-based card provides full control over layout, typography, and colour — while remaining fully interactive with the rest of the report.

## Components

1. **Core measures:** context-preserving `SUM`, `CALCULATE` + `DATEADD`, `DIVIDE`
2. **Presentation variables:** `VAR` blocks that compute arrow, colour, and summary text
3. **HTML measure:** a single `RETURN` string that concatenates HTML markup with measure values
4. **HTML Content visual:** free custom visual that renders the HTML string

## Structure

### Core Measures

```dax
Total Sales = SUM(Sales[Amount])

Previous Sales =
CALCULATE(
    [Total Sales],
    DATEADD(Sales[Date], -1, MONTH)
)

Growth % =
DIVIDE(
    [Total Sales] - [Previous Sales],
    [Previous Sales]
)
```

These measures intentionally do **not** use `ALL()` — they react to slicer and chart filter context.

### Presentation Variables

```dax
VAR Total   = [Total Sales]
VAR Growth  = [Growth %]
VAR Arrow   = IF(Growth >= 0, "▲", "▼")
VAR Color   = IF(Growth >= 0, "#22c55e", "#ef4444")
VAR Summary = IF(Growth > 0,
    "Sales are increasing compared to last month",
    "Sales declined compared to last month"
)
```

### HTML KPI Measure

```dax
KPI Card HTML =
"
<div style='
  width:380px;
  padding:26px;
  border-radius:18px;
  background:#111827;
  color:white;
  font-family:sans-serif;
'>
  <div style='font-size:46px;font-weight:700;margin-bottom:8px;color:#fbbf24;'>
    " & FORMAT(Total, "$#,##0") & "
  </div>
  <div style='display:flex;justify-content:space-between;margin-bottom:15px;'>
    <div style='color:" & Color & ";font-size:14px;font-weight:600;'>
      " & Arrow & " " & FORMAT(Growth,"0.0%") & "
    </div>
    <div style='font-size:12px;color:#6b7280;'>vs last month</div>
  </div>
  <div style='display:flex;justify-content:space-between;margin-bottom:14px;'>
    <div>
      <div style='font-size:10px;color:#6b7280;'>MIN</div>
      <div>" & FORMAT([Min Sales], "$#,##0") & "</div>
    </div>
    <div>
      <div style='font-size:10px;color:#6b7280;'>AVG</div>
      <div>" & FORMAT([Avg Sales], "$#,##0") & "</div>
    </div>
    <div>
      <div style='font-size:10px;color:#6b7280;'>MAX</div>
      <div>" & FORMAT([Max Sales], "$#,##0") & "</div>
    </div>
  </div>
  <div style='font-size:12px;color:#9ca3af;background:#020617;padding:10px;border-radius:10px;'>
    " & Summary & "
  </div>
</div>
"
```

Add supporting `Min Sales`, `Avg Sales`, `Max Sales` measures using `MINX`, `AVERAGEX`, `MAXX` over the sales table.

### HTML Content Visual

1. Install the free **HTML Content** custom visual from AppSource
2. Drop the `KPI Card HTML` measure into the visual
3. Disable all default formatting (background, border, etc.)

## Interaction with Report

The KPI card and adjacent native visuals share the same filter context:

- Date slicer filters both KPI card and bar chart
- Clicking a bar updates the KPI card value
- Selecting a range keeps everything in sync

No additional measure logic required — clean context-preserving measures handle it.

## Variations

- **Multi-metric card**: wrap each metric in its own HTML block with a shared container
- **Trend comparison**: replace "vs last month" with a dynamic `SELECTEDVALUE()` from a comparison field parameter
- **Gauge variant**: embed SVG progress bar inside the HTML using `MIN(1, Total / Target)` as a fill ratio

## Related

- [[kpi-card-context-preserving-measures]] — why these measures avoid `ALL()`
- [[kpi-card-arrow-color-from-growth]] — arrow and colour DAX logic
- [[kpi-card-growth-percent-divide]] — growth % computation
- [[kpi-card-growth-summary-text]] — plain-language summary logic
