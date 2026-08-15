---
created: 2026-08-08
updated: 2026-08-08
source: "6 Excel features I use in every spreadsheet I create"
source_url: https://www.howtogeek.com/microsoft-excel-features-i-use-in-every-spreadsheet/
author:
  - name: Tony Phillips
    source: How-To Geek
note_type: atomic
tags: [excel, power-query, get-transform, etl, refresh, applied-steps]
related:
  - "[[Excel-Table-Ctrl-T]]"
  - "[[Data-Validation-Dropdown]]"
---

# Power Query (Get & Transform)

Power Query (Data → Get & Transform Data → From Table/Range) is Excel's built-in ETL layer. It records data-cleaning steps as a reusable pipeline — the Applied Steps pane — so the same transformation runs automatically every time the source data refreshes.

## The Core Workflow

```
1. Load data into Excel Table (or point to existing range)
2. Data → Get & Transform Data → From Table/Range
3. Power Query Editor opens
4. Perform cleaning steps (remove columns, change types, filter rows, pivot, etc.)
5. Each step is recorded in the Applied Steps pane
6. Close & Load → data loads back into an Excel Table
7. Refresh: Data → Refresh All (or right-click → Refresh)
```

Every subsequent refresh replays the entire Applied Steps sequence automatically.

## Applied Steps

Each transformation in the Power Query Editor creates a named step in the Applied Steps pane:

| Step | What it does |
|------|-------------|
| Source | Points to the original data range or file |
| Change Type | Converts column data types |
| Remove Columns | Drops unwanted columns |
| Filtered Rows | Keeps only rows matching criteria |
| Renamed Columns | Renames column headers |
| Merged Queries | Joins two tables together |
| Custom Column | Adds a computed column via M code |

Steps can be reordered, deleted, or edited. Removing a step recalculates all downstream steps.

## Key Advantages

| Problem | Without Power Query | With Power Query |
|---------|--------------------|--------------------|
| Weekly data arrives messy | Clean manually every time | Set up once; Refresh All handles it |
| Source range changes | Update formulas manually | Source step auto-adapts |
| New columns added upstream | Recreate transformations | Steps replay on new data |
| Column order changes | Breakage in formulas | Steps reference column names, not positions |

Tony Phillips (HowToGeek, 2026-07-10): *"Instead of manually preparing the same report every week, I convert the data into a table and open it with Data → Get & Transform Data → From Table/Range. After the initial setup, all I have to do is update the source data and click Refresh."*

## Power Query vs Excel Formulas for Data Cleaning

| | Power Query | Excel Formulas |
|---|---|---|
| Execution | On-demand or on-open refresh | Recalculate on every sheet change |
| Complexity | Handles complex reshaping (unpivot, merge, group by) | Limited to cell-level operations |
| Transparency | Applied Steps pane shows every operation | Formula audit trail requires tracing each cell |
| Shareability | Query files (.pq or connection-only) can be shared | Each workbook is self-contained |
| Automation | Scheduled refresh via Power Automate | Manual or VBA-triggered |

## Related

- [[Excel-Table-Ctrl-T]] — use an Excel Table as the source for Power Query to benefit from auto-expanding ranges
- [[Data-Validation-Dropdown]] — apply data validation to the Power Query output table to enforce quality on cleaned data
- [[power-query-etl-workflow]] — broader Power Query ETL patterns (unpivot, merge, group by, parameters)
