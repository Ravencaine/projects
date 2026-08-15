---
created: 2026-08-10
updated: 2026-08-10
source: Building a Product Hierarchy Analytics Dashboard in Power BI: A Beginner's Journey
source_url: https://medium.com/@mitalimunot64/building-a-product-hierarchy-analytics-dashboard-in-power-bi-a-beginners-journey-6b3c72375d41
note_type: pattern
tags: [power-bi, dashboard-design, slicers, hierarchy, user-experience, drill-down]
---

# Cascading Slicers Mirror Hierarchical Data

When the data has a hierarchy (Primary → Secondary → Tertiary), the filter UI should reflect that structure. Three stacked slicers — one per hierarchy level — enable top-down navigation: picking a Primary category automatically narrows the Secondary list; picking Secondary narrows Tertiary. This makes the *structure of the data* visible in the *structure of the interface*.

## The Pattern

```
[Slicer: Primary Category]   ← most coarse
[Slicer: Secondary Category]  ← middle tier — options filter based on Primary
[Slicer: Tertiary Category]  ← most granular — options filter based on Secondary
```

## Why Three Separate Slicers Beat One Combined Dropdown

- A single dropdown with all hierarchy levels confuses users — they can't reason about it
- Separate slicers make the hierarchy explicit in the UI layout
- Each slicer updates dynamically based on the selection above it
- Users can skip levels: start at Secondary if they already know the Primary

## Implementation in Power BI

1. Create three separate slicer visuals, one per hierarchy column
2. Set each slicer to show only the relevant column from your data model
3. Enable **visual-level filter sync** if the slicers live on different pages
4. Ensure the hierarchy columns are related in the data model (star schema with a bridge or direct relationship)

## Example Use Case

- Page 2 of a Product Hierarchy dashboard
- User selects "Personal Care" → Secondary slicer shows only Personal Care's subcategories
- User selects "Hair Care" → Tertiary slicer shows only Hair Care's product types
- Result: 3 clicks from "big picture" to "exact product list"

## Related

- [[Tagging-Bridge-Table-Pattern]] — bridge tables for many-to-many relationships
- [[Two-Page-Dashboard-UX-Pattern]] — overview-first design approach
