---
created: 2026-08-09
updated: 2026-08-09
source: "Enhance Data Modelling in Power BI.md"
note_type: workflow
tags: [power-bi, data-modeling, measures, display-folder, model-view, workflow]
---

# Display Folder Organization Workflow

**Type:** Workflow · **KB:** Power BI · **Source:** [[source-enhance-data-modelling-power-bi]]

Use the Display Folder property in Power BI model view to group and categorize measures inside the `_Measures` repository table. Improves navigation and discoverability for large measure collections.

## Step 1 — Open model view

1. In Power BI Desktop, click **Model View** in the left sidebar
2. Locate the `_Measures` table

## Step 2 — Select a measure

1. Click on the measure you want to organize
2. The Properties pane opens on the right

## Step 3 — Set display folder

1. In the Properties pane, find **Display Folder**
2. Type a folder name (e.g., `Time Intelligence`, `Finance`, `KPI`)
3. Press Enter

## Folder naming conventions

| Folder | Contains |
|--------|----------|
| `Time Intelligence` | Date hierarchy, YTD, MTD measures |
| `Finance` | Revenue, margin, cost measures |
| `KPI` | Scorecard, variance, target measures |
| `Filters` | Helper measures for slicers |
| `_Calculations` | Intermediate calculated columns |

## Nested folders

Use `\` as separator for nested folders: `Finance\Revenue`, `Finance\Costs`.

## Multi-select for bulk assignment

1. Hold **Ctrl** and click multiple measures
2. Set Display Folder in Properties once
3. All selected measures go to the same folder

## Benefits

- Field list stays manageable at any scale
- Logical grouping matches business domains
- Works alongside `_Measures` repository structure

## Related

- [[measures-repository-setup-workflow]] — create the repository first
- [[measures-repository-underscore-table]] — concept explanation
- [[home-table-property-move-measures]] — move measures into repository
