---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [bubble-chart, enhancement-techniques, contextual-support, accessibility]
related: [Dual-Bubble-Chart-Overlay, Context-Sensitive-Visual-Toggle]
---

# Bubble Chart Enhancement — Complete Workflow

A 6-step workflow for turning a basic bubble chart into an insight-rich, accessible visual.

## Step 1 — Contextual Support (Supporting KPIs)

Place Card or KPI visuals beside the bubble chart to provide context:
- Total metric (e.g., average vacancy rate across all industries)
- Top performer / bottom performer as separate cards
- Time period or data source note

This helps users understand the bubble chart's scale without needing to read the axis values.

## Step 2 — Manual Size Legend

Power BI's native bubble chart doesn't explain bubble size. Add a text box or shape-based legend:
- Show 3 sample bubbles with labeled sizes (e.g., "1M employees", "500K", "100K")
- Position in a corner of the chart area.

## Step 3 — Interactive Tooltip

Enable tooltips on the bubble chart:
- Go to **Format → Tooltips → Report page**.
- Create a tooltip page with the industry name, exact values, and ranking context.

## Step 4 — Dynamic Color Coding

Create a color measure using the [[Dual-Bubble-Chart-Overlay]] technique:
- Top 3 industries by the metric → red
- Others → green

See: [[Dual-Bubble-Chart-Overlay]]

## Step 5 — Selective Data Labels

Use two overlaid bubble charts with a `Values To Show` filter:
- Chart A: all bubbles, no labels
- Chart B: top-N bubbles only, data labels enabled

See: [[Dual-Bubble-Chart-Overlay]]

## Step 6 — Tabular Alternative View

Add a toggle button that switches to a table/matrix view:
```dax
Show Table =
    IF([User Selected Table View] = 1, 1, BLANK())
```
Assign to a visual filter to show/hide the table.

## Accessibility Checklist

- [ ] Color contrast: test with color blindness simulators
- [ ] Alt text: describe the chart in the report description
- [ ] Tooltips: include full data in tooltips for screen readers
- [ ] Font: use readable, consistent fonts (Segoe UI)
- [ ] Interactive: tooltips provide additional context on hover

## Notes

- Bittar's bubble chart article covers all 6 techniques — each one addresses a specific usability gap in the native bubble chart visual.
- The manual size legend is often overlooked but critical for executive audiences who won't hover over every bubble.

## Related

- [[Dual-Bubble-Chart-Overlay]] — overlay technique for labels and color
- [[Context-Sensitive-Visual-Toggle]] — toggle between chart and table views
- [[Accessibility-for-Charts]] — full accessibility checklist
