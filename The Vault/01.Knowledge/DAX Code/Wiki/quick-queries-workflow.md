---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring the New DAX Query View in Power BI.md"
note_type: workflow
tags: [power-bi, dax, dax-query-view, quick-queries, right-click, workflow]
---

# Quick Queries Workflow

**Type:** Workflow · **KB:** DAX Code · **Source:** [[source-dax-query-view-power-bi]]

Use Quick Queries to generate DAX query templates from the Data Pane without writing code manually.

## Use Case 1 — Show Top 100 Rows

### Step 1 — Open Quick Queries menu

1. Open DAX Query View
2. In the **Data Pane** (right side), locate the table you want to inspect
3. Right-click the table name

### Step 2 — Select Show Top 100 Rows

1. From the context menu, select **Quick Queries**
2. Choose **Show Top 100 Rows**
3. Query auto-executes and results appear in the Results pane

### Step 3 — Customize and save

1. Edit the generated DAX (e.g., change `100` to `50`, add an ORDER BY)
2. Right-click the Query Page tab → **Save** or rename the page
3. The saved query persists in the .pbix

## Use Case 2 — Show Column Statistics

### Step 1 — Open Quick Queries menu

1. Right-click any **table** in the Data Pane
2. Select **Quick Queries**
3. Choose **Show Column Statistics**

### Step 2 — Read the statistics

Results show per-column statistics:
- Distinct value count
- Total row count
- Min/Max for date/numeric columns
- Null and empty string flags

### Step 3 — Use for data profiling

- Identify high-cardinality columns
- Find columns with nulls or single dominant values
- Inform modeling decisions (slicer candidates, aggregation strategy)

## Related

- [[quick-queries-right-click-templates]] — template reference
- [[quick-queries-column-statistics]] — statistics output details
- [[evaluate-basic-query-run-workflow]] — running custom queries after template generation
