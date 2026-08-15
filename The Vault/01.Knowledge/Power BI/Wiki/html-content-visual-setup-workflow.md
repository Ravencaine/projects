---
created: 2026-08-09
updated: 2026-08-09
source: "Elevating Power BI Reports with HTML & CSS Joining Forces 💪.md"
note_type: workflow
tags: [power-bi, html, html-content-visual, setup, workflow]
---

# HTML Content Visual Setup Workflow

**Type:** Workflow · **KB:** Power BI · **Source:** [[source-html-css-joining-forces-fp20]]

Install the HTML Content visual in Power BI Desktop and configure it to display HTML-returning DAX measures. Pre-requisite for all HTML/CSS patterns in Power BI.

## Step 1 — Import HTML Content visual

1. Open Power BI Desktop
2. In the Visualizations pane, click the three dots `(…)` next to the built-in visuals
3. Select **Get more visuals**
4. Search for **HTML Content** in the search bar
5. Click **Add** to import

Note: HTML Content is a third-party visual (html-content.com), not a Microsoft built-in.

## Step 2 — Add visual to report

1. Click the HTML Content visual icon in the Visualizations pane
2. Add it to the report canvas
3. Drag a measure returning HTML onto the visual

## Step 3 — Create HTML measure

```dax
My HTML Measure =
"<b>Hello</b> from HTML Content visual"
```

## Step 4 — Assign measure to visual

Drag the HTML measure into the HTML Content visual's Fields well.

The visual renders the HTML output.

## Step 5 — Test dynamic content

```dax
Variance Label =
"Variance: " & "<b>" & FORMAT([Variance], "0.0%") & "</b>"
```

Combine HTML tags with DAX FORMAT, IF, and concatenation.

## Documentation

https://www.html-content.com/examples/dax-simple

## Prerequisites

- Power BI Desktop
- HTML Content visual (third-party)
- Measures returning HTML strings enclosed in double quotes

## Related

- [[html-measure-integration-pattern]] — creating the measures
- [[html-shape-measure-template]] — shape template pattern
- [[font-awesome-dax-icon-measure]] — icon integration
