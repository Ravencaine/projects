---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: pattern
tags: [power-bi, pattern, slicer, filter, interactive]
---

# Interactive Slicer Configuration

A set of slicer visuals on a dashboard that allow users to filter the entire report by specific dimensions — enabling drill-down without building multiple reports.

## Purpose

Gives each stakeholder a personalized view of the same dashboard. Executives can filter to their region or product category without needing separate reports for each team.

## Components

- **Slicer visuals** for each filter dimension
- **Dimensions**: Year, Quarter, Month, Region, State, Product Category, Customer Segment
- **Slicer type**: dropdown (compact for many values) or list (visible for 10 or fewer)
- **Single-select vs multi-select** depending on whether combinations are meaningful
- **Sync slicers** across report pages using the Sync Slicer pane

## Structure

| Slicer | Dimension | Type | Multi-select |
|--------|-----------|------|-------------|
| Year | Calendar[Year] | Dropdown | No |
| Quarter | Calendar[Quarter] | Dropdown | No |
| Month | Calendar[Month Name] | List | No |
| Region | Geography[Region] | List | Yes |
| State | Geography[State] | Dropdown | Yes |
| Category | Product[Category] | List | Yes |
| Segment | Customer[Segment] | List | Yes |

## Best Practices

- Place slicers in a dedicated "filter pane" or at the top of each page
- Default slicers to "all selected" or the most common filter value
- Use **slicer sync** (View → Sync Slicers) to propagate one slicer selection across all pages
- Avoid more than 7 slicers on a single page — cognitive overload
- Use **visual-level filter** for page-level defaults, slicers for user-controlled overrides

## Related

- [[power-bi-dashboard-development-workflow]] — `pattern`
- [[retail-kpi-framework]] — `atomic`
