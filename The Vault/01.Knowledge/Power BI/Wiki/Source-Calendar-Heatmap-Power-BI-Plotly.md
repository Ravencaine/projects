---
created: 2026-08-11
source: How I Built a Calendar Heatmap in Power BI with Plotly.js.md
source_url: https://medium.com/microsoft-power-bi/how-i-built-a-github-style-calendar-heatmap-in-power-bi-c602c6d98454
note_type: source
tags: [power-bi, data-visualization, plotly, html-content, calendar-heatmap]
---

# How I Built a Calendar Heatmap in Power BI with Plotly.js

Builds a GitHub-style calendar heatmap using DAX + HTML Content visual + Plotly.js — bridging Power BI's tabular data world with the JavaScript visualization ecosystem.

> **Type:** article
> **Author:** Esther
> **Published:** 2026-04-02
> **URL:** https://medium.com/microsoft-power-bi/how-i-built-a-github-style-calendar-heatmap-in-power-bi-c602c6d98454
> **Routed to:** Power BI

## Summary

Demonstrates how to create an interactive GitHub-style calendar heatmap inside Power BI using the HTML Content visual and Plotly.js. The DAX layer serialises a date table into JSON; JavaScript maps dates to ISO week numbers and weekday indices; Plotly renders a 7×53 heatmap with the Viridis colour scale. The result is slicer-responsive and self-contained (CDN-loaded Plotly, no custom visual required).

## Key Claims

- Power BI has no native flexible calendar heatmap; the HTML Content visual + JS is the practical workaround
- The Viridis colour scale is perceptually balanced — readable in greyscale, colourblind-safe
- The 7×53 matrix (7 weekdays × up to 53 ISO weeks) maps calendar data to a GitHub-style grid
- CONCATENATEX is the DAX bridge that serialises table data into a JS-readable JSON array
- ISO week numbers require explicit calculation in JavaScript — `Date` objects don't expose week numbers natively

## Notable Details

- Dynamic Plotly CDN loader guards against double-loading when the HTML Content visual re-initialises
- `autorange: 'reversed'` on the y-axis places Monday at the top (matches GitHub convention)
- The `hovertemplate` field controls tooltip content without touching HTML
- Colour scales are hot-swappable: `Viridis`, `Blues`, `RdYlGn`, `Cividis`, or custom RGB arrays

## Extracted Notes

- [[GitHub-Style-Calendar-Heatmap-Pattern]] — `pattern` — full DAX+HTML+JS+Plotly pattern
- [[CONCATENATEX-JSON-Bridge]] — `snippet` — DAX→JS JSON serialisation technique
- [[getISOWeek-JavaScript]] — `snippet` — ISO 8601 week number in JS
- [[getDayNumber-JavaScript]] — `snippet` — weekday index mapping (Sunday=0 → Monday=1...Sunday=7)
- [[Plotly-Heatmap-Snippet]] — `snippet` — Plotly CDN loader + heatmap trace boilerplate
- [[Pattern-Recognition-Over-Exact-Values]] — `atomic` — principle that pattern beats precision

## Metadata

| Field | Value |
|-------|-------|
| Source file | How I Built a Calendar Heatmap in Power BI with Plotly.js.md |
| Ingestion date | 2026-08-11 |
| Word count | ~560 |
