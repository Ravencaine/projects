---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring Data Analysis with Power BI's Decomposition Tree.md"
note_type: workflow
tags: [power-bi, decomposition-tree, setup, ai-splits, workflow]
---

# Decomposition Tree Setup Workflow

**Type:** Workflow · **KB:** Power BI · **Source:** [[source-decomposition-tree-power-bi]]

Add and configure the Decomposition Tree visual in Power BI Desktop.

## Step 1 — Add the visual

1. Click the Decomposition Tree icon in the Visualization pane
2. Drag it onto the report canvas

## Step 2 — Configure Analyze Field

1. Drag a measure or aggregated field into the **Analyze Field** well
2. If no measure exists, create one: `Total = SUM(Table[Column])`
3. See [[decomposition-tree-analyze-field-requires-aggregate]] if Analyze Field is blank

## Step 3 — Configure Explain By

1. Drag dimensions to the **Explain By** well (e.g., Country, Region, Model Name, Color)
2. Order of Explain By fields determines the suggested drill sequence, but drill order is flexible

## Step 4 — Manual drill-down

1. Click **+** next to any node
2. Select a dimension from the dropdown
3. Click **+** again to add another dimension
4. Repeat to build hierarchy

## Step 5 — AI splits (cloud only)

1. Click **+** next to any node
2. Select **High Value** (biggest contributors) or **Low Value** (smallest contributors)
3. AI suggests the most significant dimension automatically
4. Note: AI splits not supported on-prem/Azure AS/PBIRS/Publish to Web — see [[decomposition-tree-ai-splits-limitations]]

## Step 6 — Filter by context

Connect slicers (Year, Month, Category) to filter the tree dynamically — see [[decomposition-tree-filter-drillthrough-workflow]].

## Related

- [[decomposition-tree-analyze-field-requires-aggregate]] — common setup issue
- [[decomposition-tree-ai-splits-limitations]] — AI split environment restrictions
- [[decomposition-tree-limits]] — 50 levels, 5,000 data points
