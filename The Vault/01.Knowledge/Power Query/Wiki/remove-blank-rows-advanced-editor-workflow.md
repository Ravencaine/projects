---
created: 2026-08-09
updated: 2026-08-09
source: "Easily Remove Blank Rows in a Table using Power Query(.pbix included).md"
note_type: workflow
tags: [power-query, blank-rows, advanced-editor, workflow]
---

# Remove Blank Rows Advanced Editor Workflow

**Type:** Workflow · **KB:** Power Query · **Source:** [[source-remove-blank-rows-power-query]]

Remove blank rows from a table using `Table.SelectRows` in the Power Query Advanced Editor. Best for datasets where blank rows come from CSV imports, Excel sheets with empty rows, or database exports with formatting inconsistencies.

## When to use

- Blank rows appear in imported CSV, Excel, or database tables
- Rows inflate row counts and distort aggregations
- Removal needs to be repeatable across future data refreshes

## Step 1 — Open Power Query

Home tab → Transform Data → Power Query Editor opens.

## Step 2 — Open Advanced Editor

In the Queries pane: select the table → Home tab → Advanced Editor.

## Step 3 — Modify M code

Replace or add a `Table.SelectRows` step. The filter checks the column that indicates a blank row:

```m
let
    Source = Csv.Document(File.Contents("C:\path\to\file.csv"), [Delimiter=",", Columns=3, Encoding=1252, QuoteStyle=QuoteStyle.None]),

    // Filter out rows where the reference column is blank
    FilterJunkRows = Table.SelectRows(Source, each ([Column2] <> "" and [Column2] <> null)),

    // Promote the first remaining row to headers
    PromotedHeaders = Table.PromoteHeaders(FilterJunkRows, [PromoteAllScalars=true])
in
    PromotedHeaders
```

Replace the file path with your own source path.

## Step 4 — Apply changes

Click Done / OK in the Advanced Editor → verify the blank rows are removed → Home tab → Close & Apply.

## Step 5 — Verify in Data pane

After Close & Apply, confirm the table in the Data pane no longer contains blank rows.

## Note on column scope

This filter checks only the specified column. For multi-column datasets, consider checking all columns that must be populated.
