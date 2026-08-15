---
created: 2026-08-09
updated: 2026-08-09
source: "Enhance Data Modelling in Power BI.md"
note_type: workflow
tags: [power-bi, data-modeling, measures, repository, model-view, workflow]
---

# Measures Repository Setup Workflow

**Type:** Workflow · **KB:** Power BI · **Source:** [[source-enhance-data-modelling-power-bi]]

Create a centralized `_Measures` repository table in Power BI Desktop to store and organize all DAX measures in one logical location.

## Step 1 — Create the table

1. Open Power BI Desktop
2. Go to **Home ribbon → Enter Data** (or **Home → New Table**)
3. Power Query editor opens with a new table

## Step 2 — Name the table

1. Rename the table to `_Measures` (leading underscore)
2. Rename the default column to `Hide Me`

## Step 3 — Add placeholder row

1. Enter any value in the first row (e.g., `1`)
2. This value is never used — it only creates the column
3. Click **Load** to create the table

## Step 4 — Hide the column (optional)

1. In **Model View**, right-click the `Hide Me` column
2. Select **Hide in report view**
3. Column is invisible to report users

## Step 5 — Create or move measures

- **New measures**: write DAX in the `_Measures` table
- **Existing measures**: select in model view → Properties → Home Table → `_Measures`

## Step 6 — Organize with display folders

Apply Display Folder property to group related measures (see [[display-folder-organization-workflow]]).

## Result

All measures live in `_Measures` at the top of the field list, organized into folders. Data tables contain only raw data.

## Related

- [[measures-repository-underscore-table]] — concept explanation
- [[home-table-property-move-measures]] — moving existing measures
- [[display-folder-organization-workflow]] — organize after setup
