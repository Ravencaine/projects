---
created: 2026-08-13
source: "Level Up with Custom Visuals Power BI HTML Calculation Groups Deneb"
source_url: https://www.youtube.com/watch?v=QXMMpabHPS4
note_type: reference
tags: [deneb, vega, vega-lite, custom-visual, data-viz]
---

# Deneb

A custom visual for Power BI that renders declarative Vega / Vega-Lite visualizations authored as JSON. Built by Daniel Marsh Patrick (the same author behind the HTML Content visual).

## Why It Exists

Python and R visuals in Power BI have two persistent drawbacks:

1. **Slow** — Python/R script execution can be sluggish for tens of thousands of rows.
2. **No native cross-visual interaction** — they don't respond to slicers or cross-filter from other visuals.

Deneb fixes both: Vega-Lite charts are GPU-friendly in many cases, and the visual participates in the standard Power BI interaction model (selectors / filters / tooltips all work).

## Quick Reference

| Capability | Notes |
|------------|-------|
| Language | JSON (Vega or Vega-Lite spec) |
| Editor | Built-in (three panes: code, preview, data table) |
| Templates | Import from JSON file or community repository |
| Cross-visual interaction | Yes — slicers, cross-filter, tooltips all work |
| Interaction with other visuals | Yes — unlike Python/R visuals |
| Author | Daniel Marsh Patrick |

## Editor Layout

When you click **Edit** on a Deneb visual:

1. **Code area** — the JSON spec (Vega or Vega-Lite)
2. **Preview** — live render of the spec
3. **Data table** — the dataset the spec is operating on (for debugging)

## Workflow

### Standard (Blank Canvas)

1. Add Deneb to the report canvas.
2. Drop the measures/columns you want to chart into **Values**.
3. Click **Edit** → choose **Create new** → Vega or Vega-Lite.
4. Pick a starter chart (bar / line / scatter) and bind fields.
5. Tweak the JSON in the code area.

### Recommended (Template Import)

1. Download a community JSON template — from the Deneb docs, Mike Carlo's Power BI Tips repo, or Kerry's site.
2. Add Deneb to canvas and put Values in place.
3. **Edit → Create new → Import from Template → select the .json file**.
4. The import wizard maps your measures to the template's expected fields.
5. Hit **Create** → Deneb loads the template with your data wired in.

> "I've a hundred percent of the time imported from template, and I advise you to do so as well." — Injae Park

## Community Resources

| Resource | URL |
|----------|-----|
| Deneb documentation | https://deneb-viz.github.io/community/resources |
| Vega-Lite examples | https://vega.github.io/vega-lite/examples |
| Mike Carlo's templates | Power BI Tips GitHub repo (Deneb-Templates folder) |
| Mike Carlo's heatmap-with-bars | https://github.com/PowerBI-tips/Deneb-Templates/blob/main/templates/heatmap%20with%20bars%20-%20red%20themed.json |

## Notes

- You can build IBCS-style charts (gradient bars, label alignment) in Deneb out-of-the-box.
- Hexbin / circle-pack maps that are common in Tableau are reproducible in Deneb.
- Editing is code-based — Vega / Vega-Lite is a small language with strong docs but is a learning curve for devs who haven't used it.
- Deneb is unlikely to disappear "anytime soon" — even with Power BI's planned native visual improvements, the open-spec layer Deneb provides fills gaps Microsoft's roadmap won't touch.

## Related

- [[power-bi-custom-visual-approaches]] — Deneb vs HTML Content vs Python/R vs native visuals
