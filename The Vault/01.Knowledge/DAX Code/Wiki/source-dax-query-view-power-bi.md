---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring the New DAX Query View in Power BI.md"
source_url: "https://databear.com/exploring-the-new-dax-query-view-in-power-bi/"
author: "[[Boniface Muchendu]]"
site: https://databear.com
published: 2024-04-14
source_type: article
kb_routing: DAX Code
tags: [power-bi, dax, dax-query-view, preview-feature, evaluate, quick-queries]
---

# Exploring the New DAX Query View in Power BI

Boniface Muchendu · Data Bear · databear.com · 2024-04-14

## What this article covers

DAX Query View: new preview feature (Nov 2023+). Write/edit/preview DAX queries inside Power BI Desktop. Query Editor, Data Pane, Results, Query Pages. EVALUATE for basic queries. Quick Queries right-click templates. Format Query, Comment/Uncomment, Search & Replace. Define and Evaluate measures in-place. Define with References and Evaluate (dependency chain).

## Components

- **Query Editor:** write/edit DAX; supports formula-bar syntax
- **Data Pane:** right side; all tables, columns, measures
- **Results:** bottom; query output
- **Query Pages:** tabs at bottom; saved inside the .pbix model

## Key features

- **EVALUATE:** basic table query (equivalent to SELECT * FROM)
- **Quick Queries:** right-click table/column/measure → Show Top 100, Show Column Statistics
- **Define and Evaluate:** right-click measure → see formula + result
- **Define with References and Evaluate:** shows full measure dependency chain
- **Format Query:** auto-indent/beautify
- **Comment/Uncomment:** exclude lines without deleting
- **Update Model:** save measure changes directly to the model

## Enable

File → Options and settings → Options → Preview features → DAX Query View → OK → restart Power BI.
