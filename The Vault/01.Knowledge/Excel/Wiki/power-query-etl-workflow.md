---
created: 2026-07-26
updated: 2026-08-02
source: "Beyond VLOOKUP: Unleashing Excel's True Data Power for Business Analysis"
source_url: https://medium.com/@harsh1995hg/beyond-vlookup-unleashing-excels-true-data-power-for-business-analysis-33e9c54a66c4
note_type: workflow
tags: [excel, power-query, etl, automation]
---

# Power Query ETL Workflow

Connect to data sources, clean and transform data, then load it into a usable format — all with a reproducible, automated pipeline.

## Prerequisites

- Excel 2016 or later (Power Query is built in under the Data tab as "Get & Transform Data")
- Data arriving from one or more external sources (CSV, Excel, database, web)

## Steps

1. **Connect**: Open the Data tab and select "Get & Transform Data." Choose the source type (Excel file, CSV, database, web page, folder, etc.). Load the raw data into Power Query.

2. **Clean**: Apply transformations in the Power Query Editor:
   - Remove duplicates
   - Unpivot messy tables
   - Split columns by delimiter
   - Change data types (text → date, text → number)
   - Filter or remove rows by condition

3. **Transform**: Perform any additional reshaping: rename columns, reorder columns, merge queries, append queries (stack tables), pivot/unpivot.

4. **Load**: Close the Power Query Editor and load the result into a worksheet, a Pivot Table, or the Data Model (Power Pivot).

5. **Refresh**: When new data arrives, right-click the query and select "Refresh" — all transformation steps replay automatically on the new data.

## Variations

- **Folder source**: Point Power Query at a folder of identically-structured files. New files dropped in the folder are absorbed on the next refresh.
- **Web scraping**: Use "From Web" to pull tables directly from public URLs. The query refreshes the latest data on each run.
- **Parameters**: Store connection strings or thresholds as named parameters so they can be updated without editing the query steps.

## Common Errors

- <!-- link to error note if column name changes in source -->
- <!-- link to error note if data type mismatch after refresh -->

## Related

- [[power-query-etl-workflow]]
- [[excel-as-bi-tool]] — the broader context: Excel as a BI platform
- [[pivot-tables]] — what to do with cleaned data once loaded
