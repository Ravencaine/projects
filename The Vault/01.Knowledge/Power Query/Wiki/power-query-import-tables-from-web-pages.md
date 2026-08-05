---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: pattern
tags: [power-query, web, scrape, table, html]
---

# Power Query: Import Tables from Web Pages

Power Query can scrape HTML tables directly from any web page, automatically parsing them into rows and columns — useful for importing publicly available tabular data.

## Purpose

Many web pages expose data in HTML `<table>` elements. Rather than copy-pasting, Power Query can load them directly as a query — refreshable and cleanable.

## Components

- Power Query → From Web (URL input)
- Table selection dialog (appears after URL is loaded)
- Query Editor for cleaning

## Structure

```
1. Power Query → From Web → enter URL → OK
2. Power Query scans the page and lists all detected HTML tables
3. Select the desired table from the list → click Load or Edit
4. (Optional) Edit in Query Editor to:
   - Promote headers
   - Remove unwanted columns
   - Change data types
5. Close & Load
```

## Example

Ch3 scenario: importing population or GDP data from a public data portal (e.g., World Bank, Census Bureau, Azure Marketplace):
1. Navigate to the web page containing the table
2. Copy the URL
3. Power Query → From Web → paste URL
4. Select the correct table from the list
5. Data lands in the Query Editor — promote headers if needed, clean up extra columns

## Notes

- Power Query scans all `<table>` elements on the page and presents them as numbered options (Table 0, Table 1, etc.)
- If the wrong table appears, try the next numbered option
- Pages with JavaScript-rendered tables may not be fully captured — the data must be in static HTML

## Related

- [[power-query-import-json-from-web-api]] — structured data via JSON API
- [[power-query-import-multiple-csv-files-from-folder]] — file-based alternative
- [[hdinsight-power-query-pivot-table-power-map-pipeline]] — Power Query as the ETL step in the full pipeline
