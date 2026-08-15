---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring the New DAX Query View in Power BI.md"
note_type: atomic
tags: [power-bi, dax, dax-query-view, ui-components, query-editor, results, atomic]
---

# DAX Query View UI Components Atomic

**Type:** Atomic · **KB:** DAX Code · **Source:** [[source-dax-query-view-power-bi]]

DAX Query View has four main components: Query Editor, Data Pane, Results, and Query Pages. Each serves a distinct role in the query development workflow.

## Component 1 — Query Editor

- Center of the DAX Query View
- Write and edit DAX queries
- Supports the same DAX syntax as the formula bar
- Has toolbar: Run, Format Query, Comment, Uncomment, Search & Replace

## Component 2 — Data Pane

- Right side of the view
- Shows all tables, columns, and measures in the current model
- Supports right-click context menu for Quick Queries
- Reference fields directly from here when writing queries

## Component 3 — Results

- Bottom of the view
- Displays output of executed queries
- Updates dynamically when Run is clicked
- Shows table results with row/column structure

## Component 4 — Query Pages

- Bottom of the view (tab strip, similar to report pages)
- Create and switch between multiple DAX queries
- **Saved inside the .pbix model:** queries persist after closing and reopening the file
- Rename, duplicate, delete via right-click

## Related

- [[evaluate-basic-query-run-workflow]] — writing and running first query
- [[quick-queries-right-click-templates]] — Quick Queries from the Data Pane
