---
created: 2026-08-09
updated: 2026-08-09
source: "Designing for Impact 6 Ideas to Enhance the User Experience and Accessibility of Your Power BI Dashboards.md"
note_type: pattern
tags: [power-bi, ux, non-data-savvy, simple-visualization, drop-down-slicer, drill-down, pattern]
---

# Non-Data-Savvy User Design Pattern

> **Type:** pattern
> **Routed to:** Power BI
> **Primary source:** Isabelle Bittar — 2024-03-02

## Problem

End users consuming the dashboard are not data analysts. They expect dashboards to behave like professional apps and websites, not like Power BI training exercises. Complex visualizations and advanced features confuse rather than inform.

## Design Principles

### 1. Choose Simple Visualizations

**Prefer:**
- Bar charts
- Line charts
- KPI cards
- Simple tables

**Avoid:**
- Complex or "cool" visualizations just because they're available
- Overlaid columns (fun but confusing for non-data users)
- Treemaps, Sankeys, or other non-obvious chart types unless the audience is familiar

> "The ultimate value of a report lies in its ability to communicate insights clearly and effectively, not in its adherence to the latest graphical trends."

### 2. Replace Drill-Downs with Drop-Down Slicers

Drill-down requires knowing to click the drill-down arrows — non-obvious for unfamiliar users.

**Instead:** Add a drop-down slicer that lets users select the view they want (e.g., "View by Category", "View by Region"). One click, no learning curve.

### 3. Embed Instructions for Advanced Features

If drill-down or other non-obvious features must be used, add text instructions directly on the page (e.g., bottom-right of the chart: "Use the arrows to explore Category → Subcategory").

### 4. Test with Real Users

Design decisions should be validated with actual end users — not sponsors, project managers, or BI developers. If non-data-savvy users can't interpret a visual immediately, simplify it.

## Key Rule

> A bar chart that a non-data-savvy user understands immediately is worth more than a sophisticated visual that requires interpretation.

## See Also

- [[Source-Designing-for-Impact-6-Ideas]] — source article
- [[Summary-Overview-Page-Pattern]] — summary page pattern for quick comprehension
- [[Drillable-Hierarchy-Sentence-Tooltip-Pattern]] — tooltip pattern that handles drill without confusing users
