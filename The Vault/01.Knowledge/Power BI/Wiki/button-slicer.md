---
created: 2026-08-06
updated: 2026-08-06
source: Button Slicer Level Up Your Power BI Reports!
note_type: atomic
tags: [button-slicer, power-bi, new-card-visual, visual-design]
---

# Button Slicer

An interactive filtering control in Power BI that renders slicer items as styled buttons instead of a traditional list.

<!-- one-line description: A slicer visual that displays filter options as interactive, styled buttons using the New Card visual -->

## Definition

The Button Slicer uses the **New Card visual** (preview feature) configured in slicer mode. Each slicer item renders as an individual button with its own shape, color, image, and conditional formatting — replacing the plain vertical list of the standard slicer.

## Key Points

- Requires **File → Options → Preview features → "New card visual"** to be enabled
- The "New slicer" in the visualization pane is actually a New Card visual in slicer mode
- Each button supports four states: **Default, Hover, Pressed, Selected:** each independently formatable
- Supports **images** via image URL fields (requires Data category → Image URL on the column)
- Supports **conditional formatting** rules tied to data values (thresholds, saturation, color)
- Supports **drill-through** page navigation via button actions
- Shape options include rectangle, rounded rectangle, ellipse, and custom shapes

## Examples

- E-commerce report: product photos on buttons → click to filter product gallery
- Sales dashboard: region flags as button images → click to filter by country
- HR report: department buttons with gold highlight for top-performing teams
- KPI dashboard: period buttons that dim unselected periods for visual focus

See also [[Image-URL-Data-Category]] for the data model requirement to display images in slicers.

## Related

- [[Create-a-Button-Slicer]] — step-by-step workflow
- [[New-Power-BI-Slicer-Features]] — general new slicer capabilities
- [[conditional-formatting-via-dax]] — conditional formatting techniques
