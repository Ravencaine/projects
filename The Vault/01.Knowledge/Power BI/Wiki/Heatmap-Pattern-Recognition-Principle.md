---
created: 2026-08-11
updated: 2026-08-11
source: How I Built a Calendar Heatmap in Power BI with Plotly.js.md
note_type: atomic
tags: [visualization, heatmap, pattern-recognition, data-storytelling]
---

# Heatmaps Reveal Behavioral Patterns Tables Miss

A calendar heatmap encodes daily intensity as color, enabling instant pattern recognition across a full year — something a table of numbers or a line chart cannot do without precise reading.

## Definition

A calendar heatmap (GitHub contribution graph style) maps:
- **X-axis:** ISO week number (1–53)
- **Y-axis:** day of week (Monday–Sunday)
- **Color:** activity intensity (darker = quieter, brighter = more active)

The eye reads the whole grid holistically and immediately identifies clusters, dips, trends, and anomalies without scanning individual cells.

## Key Points

- **Pattern > precision:** exact values become secondary once the pattern is visible
- **Time ranges visible at a glance:** year-end dips, summer slowdowns, weekly rhythms — all visible in under 2 seconds
- **Complementary to KPIs:** a KPI card tells you the number; the heatmap tells you the story behind it
- **Colorblind-safe scales available:** Viridis and Cividis work for most audiences
- **Slicer-compatible:** filter context from Power BI slicers flows into the underlying DAX measure, making the heatmap interactive

## Examples

- GitHub's contribution graph: developers instantly spot personal productivity patterns
- Camden Council heatmap: identified ~56% cost reduction opportunity via visual clustering of problem areas
- Email activity, gym visits, code commits, sales volume — any date-keyed count metric

## When to Use

Use a calendar heatmap when:
- The question is about **consistency vs. variation** over time
- You need to show **when** something happened, not just **what** happened
- A table or KPI card obscures the temporal story

Do not use it when:
- Exact daily values are required (a table is better for precision)
- The data grain is not daily (heatmap loses meaning with weekly or monthly aggregation)

## Related

- [[Calendar-Heatmap-Plotly-Power-BI]] — `pattern`
- [[Build-Calendar-Heatmap-Power-BI]] — `workflow`
- [[Data-Storytelling]] — `atomic` — narrative over numbers
