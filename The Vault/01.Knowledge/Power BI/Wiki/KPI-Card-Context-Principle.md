---
created: 2026-08-10
updated: 2026-08-10
source: ChatGPT Thinks. Copilot Builds. Power BI Proves.
source_url: https://medium.com/@Jamesabryant/chatgpt-thinks-copilot-builds-power-bi-proves-827a505d5b36
note_type: atomic
tags: [power-bi, kpi, dashboard-design, data-literacy, misleading-metrics, context]
---

# KPI Cards Hide Distribution, Trend, and Outliers

A KPI card shows a number. That number is incomplete. Always pair it with context that reveals what the summary is hiding.

## The Problem

Example: **Average Speed: 8.30 m/s**

This number is helpful but incomplete:
- Does not show whether one athlete is consistently strong or wildly inconsistent
- Does not reveal whether speed is improving or declining
- Does not explain whether a drop followed a heavy training period
- Masks distribution across the underlying records

The same problem applies to every business KPI: average revenue, average cycle time, average response rate.

## The Fix

Pair every KPI card with at least one contextual element:

| What the KPI hides | What to add |
|--------------------|-------------|
| Consistency vs variation | Distribution chart, min/max range |
| Trend | Trend line, sparkline |
| Target performance | Benchmark, target line, YoY comparison |
| Drill-down | Filterable detail view, tooltip with breakdown |
| Interpretation | Short plain-language note |

## The Design Rule

> Add the right context, not more charts. The goal is not to show more — it is to reveal what the summary conceals.

## The ChatGPT Prompt

After building the first version, ask:
*What could this KPI be hiding, and what supporting visual would help explain it?*

This often surfaces the single most important addition.

## Related

- [[Two-Page-Dashboard-UX-Pattern]] — Overview page should front-load KPI cards with their context
- [[Two-Layer-AI-Workflow-ChatGPT-Copilot-Power-BI]] — Layer 1 ChatGPT helps identify what context each KPI needs
