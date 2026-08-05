---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Connecting to Your First Data Source.md"
note_type: atomic
tags: [power-bi, data-sources, excel, csv, json, beginner]
---

# File-Based Data Sources in Power BI

Three file formats cover the majority of beginner data connections in Power BI. Each has distinct behaviour that affects how data is read and how Power BI handles refresh.

## Excel Workbooks (.xlsx, .xlsb)

**Connector:** Get Data → Excel Workbook

Excel is the most common starting point for Power BI beginners. Power BI reads named tables, named ranges, and the data model from any sheet.

| Behaviour | Detail |
|-----------|--------|
| Table detection | Power BI auto-detects tables with headers; individual sheets are also available |
| Multiple tables | Navigator lets you select any combination of sheets and tables |
| Data model | If the workbook has a Power Pivot data model, Power BI reads it as a separate table |
| Refresh | When imported from OneDrive/SharePoint, Excel file updates automatically reflect in Power BI |

**Key distinction — OneDrive vs local file:**
- **Local file:** Power BI stores a static copy. Changes to the source file do not update the report.
- **OneDrive/SharePoint:** Power BI creates a live connection. Changes to the source Excel file automatically trigger a refresh in Power BI Service.

## CSV Files (.csv)

**Connector:** Get Data → Text/CSV

CSV files are plain text — no formatting, no formulas, no multi-sheet structure. Every row has the same columns separated by a delimiter (comma by default, but Power BI detects semicolon, tab, and pipe as well).

| Behaviour | Detail |
|-----------|--------|
| Auto-detection | Power BI automatically detects column separators, headers, and common data types |
| Single table | One CSV = one table. No navigation needed. |
| Data types | Often misidentified — review in Navigator before loading |
| Encoding | Handle non-UTF-8 files (international character sets) with care; Power BI may show garbled text |

**Best practice:** Open in Navigator, check column types before loading. A CSV that looks correct may have numbers stored as text or dates in a non-standard format.

## JSON Files (.json)

**Connector:** Get Data → JSON

JSON is common from web APIs, modern SaaS tools, and cloud services.

| Behaviour | Detail |
|-----------|--------|
| Nested structure | Power BI automatically flattens nested JSON into tabular format |
| Arrays | Power BI converts JSON arrays into rows |
| Schema discovery | Navigator shows the detected structure — expand to see available tables |

**Best practice:** After loading, verify the table structure in the Fields pane. Nested JSON that didn't flatten cleanly will produce unexpected columns or empty tables.

## Related

- [[load-vs-transform-data]] — use Transform Data on any file that needs schema review
- [[import-vs-directquery-connection]] — Import mode applies to all three formats
- [[cloud-data-sources-onedrive-sharepoint]] — the OneDrive distinction for Excel applies here too
