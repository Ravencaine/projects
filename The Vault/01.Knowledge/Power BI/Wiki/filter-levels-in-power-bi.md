---
created: 2026-08-09
updated: 2026-08-09
source: "Filters in Power BI Everything You Need to Know.md"
note_type: atomic
tags: [power-bi, filters, filter-levels, visual-level, page-level, report-level, drillthrough, atomic]
---

# Filter Levels in Power BI Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-filters-in-power-bi-everything-you-need-to-know]]

Power BI has four filter levels, ordered from narrowest to widest scope. Each level affects a different scope of visuals.

## The four levels

| Level | Scope | How applied |
|-------|-------|-------------|
| **Visual-level** | Single visual only | Drag field to the visual's filter well |
| **Page-level** | All visuals on one page | Drag field to the page-level filter section |
| **Report-level** | All visuals across all pages | Drag field to the report-level filter section |
| **Drillthrough** | Specific target page | Right-click → Drillthrough; navigates to detail page |

## Precedence

Filters cascade from report → page → visual. Visual-level filters are narrowest (most specific) and applied last. Report-level filters are widest and applied first.

## Drillthrough specifics

Drillthrough filters carry context from the source visual (e.g., a selected product) to a dedicated detail page. The target page must have the matching field in its drillthrough well.

## Filter direction note

Filters always flow from the one-side toward the many-side of a relationship (in the data model). If a visual-level filter on `Customer[Name]` does not appear to work, check the relationship direction and cross-filter settings.

## Related

- [[filter-types-overview]] — basic, advanced, Top N, relative date, slicer
- [[apply-filters-to-visuals-workflow]] — how to add a filter to a visual
- [[filter-best-practices]] — understand data model first
