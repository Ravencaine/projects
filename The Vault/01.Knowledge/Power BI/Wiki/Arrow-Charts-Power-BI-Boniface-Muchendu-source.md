---
created: 2026-08-05
updated: 2026-08-05
source: Arrow Charts in Power BI Enhancing Data Visualization (Boniface Muchendu)
source_url: https://databear.com/arrow-charts-in-power-bi/
note_type: source
tags: [power-bi, arrow-chart, line-chart, error-bars, conditional-formatting, markers, data-visualization]
---

# Arrow Charts in Power BI Enhancing Data Visualization (Boniface Muchendu)

Builds an Arrow (AR) chart: a line chart with conditional-formatting on markers (green/red) and error bar arrows showing direction/magnitude of period-over-period change. Covers the full build process: line chart setup, dual positive/negative measures, marker conditional formatting, error bar arrow configuration, and label strategies.

> **Type:** article
> **Author:** Boniface Muchendu (DataBear)
> **Published:** 2023-11-19
> **URL:** https://databear.com/arrow-charts-in-power-bi/
> **Routed to:** Power BI

## Summary

Arrow charts tell a data story — not just showing what the numbers are, but showing the direction and magnitude of change between periods. Built on a line chart with two dual-purpose measures (positive/negative series) enabling conditional formatting on markers, then enhanced with Power BI's native error bar arrows. Boniface walks through: starting with a column → line chart transition, creating current/previous quarter measures, splitting into positive/negative series, applying colour coding, configuring error bar arrows, and perfecting labels (absolute vs % change).

## Key Claims

- Arrow charts excel where column charts fail: showing the journey from A to B, not just the values at A and B
- Power BI doesn't natively support conditional formatting on line chart markers directly — the workaround is dual series (positive/negative) with conditional formatting on each
- Error bars on line charts in Power BI provide the arrow visual (positive = up arrow, negative = down arrow)
- Two DAX measures needed: one for current period, one for previous period
- Two additional series needed: positive series (current > previous) and negative series (current < previous)
- Label strategy: absolute values for detail, percentage changes for emphasis on magnitude

## Notable Details

- Conditional formatting workaround: create separate series for "when positive" and "when negative" — each can have its own marker colour
- Error bar arrows: enabled in the Error bars section of the line chart formatting pane; upper/lower bounds set per series
- Arrow customisation: straight/curved arrows, arrowhead style, size, transparency, thickness
- Labels: can show absolute values or percentage change; background colour and transparency can be adjusted
- DAX for positive series: `IF([Current Qtr] > [Prev Qtr], [Current Qtr], BLANK())`
- DAX for negative series: `IF([Current Qtr] < [Prev Qtr], [Current Qtr], BLANK())`

## Extracted Notes

Links to notes derived from this source:

- [[Arrow-Chart-Build-Line-Marker-ErrorBar]] — `atomic` — full build: line chart + dual series + conditional formatting + error bar arrows
- [[Dual-Measure-Conditional-Formatting-Positive-Negative]] — `atomic` — positive/negative series split with IF/BLANK, colour coding
- [[Period-over-Period-DAX-Measures-Arrow-Chart]] — `pattern` — current quarter, previous quarter, % change DAX measures
- [[Error-Bars-Power-BI-Native]] — `reference` — native Power BI error bar feature (bounds, direction, arrow options)
- [[Author-Boniface-Muchendu]] — `author` — Boniface Muchendu, DataBear (8 sources)
