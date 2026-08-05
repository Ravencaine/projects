---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Transforming Data with Power Query Editor.md"
note_type: atomic
tags: [power-bi, power-query, beginner, workflow, column-quality, column-profile]
---

# Power Query: The Workflow Process

A repeatable four-step process for every data preparation task.

## Step 1: Connect

Import data from any source: Excel, CSV, Database, Web, SharePoint, API, and 100+ others.

Home → Get Data → select source → navigate to data → Transform Data (opens Power Query Editor)

## Step 2: Assess

Before transforming anything, assess the data quality.

**Enable Column Quality:**
View → Column Quality

Shows for each column:
- Valid % — percentage of rows that loaded successfully
- Error % — percentage with errors
- Empty % — percentage that are null/blank

A high error or empty percentage means you need to investigate before proceeding.

**Enable Column Profile:**
View → Column Profile

Shows for the selected column:
- Value distribution (bar chart of top values)
- Statistics (count, distinct, min, max, average, nulls)

**Spot obvious issues:**
- Inconsistent case ("john smith" vs "John Smith")
- Non-standard date formats
- Unexpected values in numeric columns
- Duplicate entries that should be unique keys

## Step 3: Transform

Apply transformations in the recommended order:

1. **Fix structure**: remove unnecessary rows (header rows, blank rows), use first row as headers
2. **Clean data**: handle errors, standardise formats, trim whitespace, replace nulls
3. **Correct data types**: set proper types after cleaning
4. **Add calculated columns**: custom columns, derived values
5. **Filter unnecessary data**: remove rows you don't need before loading

**Rationale:** Clean and type-correct data before adding calculated columns. Errors in source data propagate into derived columns if not fixed first.

## Step 4: Load

Click "Close & Apply" to send clean data to the Power BI model.

Power Query Editor closes. The data loads into the model with all transformations baked in.

**Next month:** Just refresh the data source. All transformation steps replay automatically on the new data.

## The Typical Applied Steps Sequence

```
1. Source            (connect to file/database)
2. Remove Top Rows   (remove header clutter)
3. Use First Row as Headers
4. Change Type      (set correct data types)
5. Replace Errors   (handle N/A, invalid values)
6. Add Custom Column (calculated field)
7. Remove Columns    (drop unnecessary columns)
8. Filter Rows      (exclude test/irrelevant data)
```

Each step is named and can be edited, deleted, or reordered.

## Related

- [[power-query-applied-steps-repeatability]] — why this automation changes everything
- [[power-query-6-transformation-categories]] — transformations used in Step 3
- [[power-query-5-core-components]] — UI components that support this workflow
