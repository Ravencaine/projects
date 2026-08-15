---
created: 2026-08-11
updated: 2026-08-11
source: "5-Power-BI-Slicer-Tricks-Goodly-Transcript.md"
note_type: pattern
tags: [power-bi, slicer, buttons]
---

# Apply Slicers + Clear Slicers Buttons

Defer slicer application until the user explicitly commits — prevents cascading queries on slow models.

## How It Works

Insert → Buttons → Apply Slicers → places a button on the canvas. When clicked, the button applies all pending slicer selections simultaneously. Pending selections show a clock icon next to each slicer.

Clear Slicers removes all active slicer selections in one click.

## Use Case

On models with slow queries: users make multiple slicer selections, each triggering a query. With Apply Slicers, all selections are queued and applied at once — one query instead of N.

## Related

- [[slicer-default-selection-current-period]] — auto-selecting the current period
- [[disconnected-table-slicer-pattern]] — disconnected table for highlight-only slicers
