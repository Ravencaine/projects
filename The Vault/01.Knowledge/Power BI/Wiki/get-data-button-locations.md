---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Connecting to Your First Data Source.md"
note_type: atomic
tags: [power-bi, get-data, beginner, ui, navigation]
---

# Get Data Button Locations

Power BI Desktop gives you two ways to reach the Get Data window — the quick list and the full catalogue. Knowing both prevents wasted time hunting for connectors buried in submenus.

## Entry Point 1: Common Data Sources

**Location:** Home ribbon → Get Data button (labelled button, not the down arrow)

The primary button opens a short list of the most frequently used sources:
- Excel Workbook
- Text/CSV
- Web
- SQL Server
- More…

Use this when you know the source type and want the fastest path.

## Entry Point 2: Full Catalogue

**Location:** Home ribbon → Get Data down arrow → More…

Opens the full Get Data dialog with sources organised into logical categories:
- **All**: every available connector
- **File**: Excel, CSV, JSON, XML, Folder
- **Database**: SQL Server, MySQL, PostgreSQL, Oracle, SAP, and more
- **Power Platform**: Power BI datasets, dataflows
- **Azure**: Azure SQL, Synapse, Blob, Data Lake
- **Online Services**: SharePoint Online, Salesforce, Google Analytics
- **Other**: Web, R scripts, Python scripts, OData, ODB

## Practical Rule

| Situation | Use |
|-----------|-----|
| Excel, CSV, Web, SQL Server (common) | Get Data button |
| SharePoint, MySQL, API, or any less common source | Get Data → More |
| Looking for a specific connector by name | More → All (search bar at top) |

The More dialog is also where you access **Get Data without selecting a specific type**: useful when exploring an unfamiliar data source.

## Related

- [[load-vs-transform-data]] — what to do after selecting a source
- [[import-vs-directquery-connection]] — connection mode choice after selection
