---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: pattern
tags: [power-query, csv, folder, import, etl]
---

# Power Query: Import Multiple CSV Files from Folder

Power Query can combine all CSV files from a folder into a single query — useful for consolidating periodic exports (daily sales files, monthly logs, etc.) into one table.

## Purpose

When data is exported in separate files per period (e.g., `Sales_2019.csv`, `Sales_2020.csv`, `Sales_2021.csv`), importing them one by one is tedious and fragile. The folder import pattern loads all files automatically and stacks them into one table.

## Components

- A folder containing identically-structured CSV files
- Power Query → From File → From Folder

## Structure

```
1. Power Query tab → From File → From Folder
2. Browse to the folder containing the CSV files
3. Power Query lists all files with Name, Extension, Date accessed, etc.
4. Click Combine → Combine & Edit
5. Power Query:
   - Auto-detects the delimiter
   - Previews the first file's structure
   - Use the dropdown to select which file to use as the template
   - Optionally: check "Skip files with errors"
6. Click OK → Power Query creates a combined query
7. Remove the helper query column ("Source.Name") or keep it as a file identifier
8. Close & Load
```

## Example

Ch8 scenario: stock price CSV files containing opening/high/low/closing prices and volume for each trading day:
1. Place all stock CSV files in one folder
2. From Folder → Browse → select the folder
3. Combined query stacks all files into one table with one row per stock symbol per day
4. Each original file contributes its rows to the combined dataset

## Notes

- All files must have identical column structure — if one file has extra columns, Power Query fills them with nulls
- The "Source.Name" column indicates which file each row came from — useful for filtering by period
- To refresh when new files are added: right-click the query → Refresh

## Related

- [[power-query-import-tables-from-web-pages]] — another import source pattern
- [[power-query-import-json-from-web-api]] — structured data import alternative
- [[hdinsight-power-query-pivot-table-power-map-pipeline]] — the HDInsight pipeline that feeds into Power Query
