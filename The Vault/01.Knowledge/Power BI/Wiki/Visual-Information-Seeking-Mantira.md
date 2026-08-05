---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: atomic
tags: [visual-design, information-seeking, Shneiderman, overview, zoom, filter, details]
related: [The-3-30-300-Rule, Data-Narratives-Report-Design]
---

# Visual Information-Seeking Mantra

A design framework from Ben Shneiderman that prescribes the optimal sequence for presenting data at different levels of detail.

## The Mantra

> **Overview first, zoom and filter, then details-on-demand.**

## Three-Level Sequence

### Level 1 — Overview (Overview First)

Show the entire dataset in context.

- The entire chart area shows all data points.
- The user gets a complete picture: range, density, outliers.
- In Power BI: the main visual on page 1 of a report.

### Level 2 — Zoom and Filter

Let the user narrow the view.

- Slicers and filters reduce the dataset.
- Zooming changes the granularity (e.g., from monthly to daily).
- In Power BI: slicers, filter pane, and field parameters.

### Level 3 — Details on Demand

Provide full information for a selected item.

- Tooltip shows the full record.
- Drillthrough page shows related data.
- Export shows raw data.
- In Power BI: tooltips, drillthrough pages, Q&A.

## Mapping to Power BI

| Mantra Level | Power BI Feature |
|-------------|-----------------|
| Overview first | Main visual on each page |
| Zoom/Filter | Slicers, filter pane, field parameters |
| Details on demand | Tooltips, drillthrough, Q&A visual |

## Relationship to the 3-30-300 Rule

The mantras are complementary:

| Mantra | 3-30-300 Tier |
|--------|--------------|
| Overview first | 3 seconds — the overview page |
| Zoom/Filter | 30 seconds — the exploration page |
| Details on demand | 300 seconds — the analysis page |

## Notes

- Bittar's data narrative process (see [[Data-Narratives-Report-Design]]) embeds the mantra as the structural logic of multi-page reports.
- The mantras are a communication design principle — they guide page sequencing, not individual visual design.

## Related

- [[The-3-30-300-Rule]] — time-budget framework
- [[Data-Narratives-Report-Design]] — process that implements the mantra
- [[Power-BI-UX-7-Features]] — specific Power BI features that serve each level
