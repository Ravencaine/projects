---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring Data Analysis with Power BI's Decomposition Tree.md"
note_type: workflow
tags: [power-bi, decomposition-tree, filter, drill-through, slicer, workflow]
---

# Decomposition Tree Filter and Drillthrough Workflow

**Type:** Workflow · **KB:** Power BI · **Source:** [[source-decomposition-tree-power-bi]]

Use slicers and drill-through pages to add context and detail to the Decomposition Tree.

## Filtering the Decomposition Tree

The tree responds to all slicers on the same report page:

1. Add a Year or Month slicer (or any slicer)
2. Select a value — the tree updates to reflect the filter context
3. Filter by Category, Region, or any dimension as needed

This is useful for time-period analysis: filter to a specific year to see which dimensions contributed most in that period.

## Drill-through on a data point

Set up a drill-through page to show detailed information when the user clicks a specific node:

### Step 1 — Create the drill-through page

1. Add a new page
2. Add visuals (table, card, matrix) showing detailed data

### Step 2 — Configure drill-through field

1. Drag the field matching the Decomposition Tree node (e.g., Model Name) into the drill-through page's visual
2. Set the page's visual-level filter to allow drill-through

### Step 3 — Enable drill-through on tree

1. Select the Decomposition Tree visual
2. Right-click on a node (e.g., "Mountain 200")
3. Select **Drill through** → choose the drill-through page

When the user clicks the node, the drill-through page opens with filtered context.

## Combining filters and drill-through

1. User applies slicer filter (e.g., Year = 2024)
2. User clicks a tree node
3. Drill-through page opens with Year = 2024 AND the selected node context

## Related

- [[decomposition-tree-setup-workflow]] — initial visual setup
- [[decomposition-tree-analyze-field-requires-aggregate]] — measure requirement
