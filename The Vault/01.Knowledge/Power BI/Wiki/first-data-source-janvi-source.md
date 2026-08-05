---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Connecting to Your First Data Source.md"
source_url: "https://medium.com/microsoft-power-bi/master-power-bi-connecting-to-your-first-data-source-5a291d80ecb2"
note_type: source
tags: [power-bi, data-sources, beginner, get-data, import-mode, directquery]
---

# First Data Source — Janvi Gupta

> **Type:** tutorial / beginner guide
> **Author:** Janvi Gupta
> **Published:** 2025-08-27
> **URL:** https://medium.com/microsoft-power-bi/master-power-bi-connecting-to-your-first-data-source-5a291d80ecb2
> **Routed to:** Power BI

## Summary

Beginner's guide to connecting Power BI Desktop to data. Covers four data source categories (file-based, database, cloud, web/API), Import vs DirectQuery connection modes, step-by-step instructions with GUI navigation, authentication requirements, and a troubleshooting quick reference.

## Data Source Categories

| Category | Examples |
|----------|----------|
| File-based | Excel Workbook, CSV, JSON |
| Database | SQL Server, MySQL, PostgreSQL |
| Cloud | OneDrive for Business, SharePoint Online, Azure |
| Web/API | Web pages (tables), REST APIs |

## Connection Modes

- **Import:** Snapshot of data stored in .pbix file. Fast performance, full feature support. Best for data that doesn't change frequently.
- **DirectQuery:** Data queried from source at runtime. Always current, handles large datasets. Some DAX and transformation features restricted. Cannot switch from Import to DirectQuery after setup.

## Get Data Entry Points

- **Common sources list:** Home ribbon → Get Data button (or down arrow)
- **Full catalogue:** Home → Get Data → More → All / File / Database / Power Platform / Azure / Online Services / Other

## Key Distinctions

- **OneDrive/SharePoint upload:** Power BI creates a live connection — changes to source file automatically reflect in reports
- **Local file upload:** Power BI stores a copy in the workspace — no automatic refresh

## Authentication

Most connection failures stem from credentials or permissions. Required for every source type: username/password for databases; Microsoft 365 credentials for cloud services; API keys or OAuth tokens for REST APIs.

## Troubleshooting Quick Reference

| Problem | Solution |
|---------|----------|
| Connection fails after publishing | Configure data source credentials in Power BI Service |
| Can't see expected data | Check permissions and verify correct table selection |
| Data looks incorrectly formatted | Use Transform Data to correct data types before loading |
| Large datasets load slowly | Consider DirectQuery or data source optimisation |

## Best Practices

1. Start simple (Excel/CSV) to build confidence
2. Plan refresh strategy upfront — local files require manual refresh; cloud files refresh automatically; databases need scheduled refresh in Power BI Service
3. Document all connections: server names, authentication methods, refresh schedules, source owner contacts
4. Understand your data source characteristics before choosing connection mode

## Extracted Notes

- [[get-data-button-locations]] — `atomic` — two Get Data entry points: common sources vs full catalogue
- [[load-vs-transform-data]] — `atomic` — Load: import immediately; Transform Data: open Power Query Editor first
- [[import-vs-directquery-connection]] — `atomic` — snapshot vs live query; irreversible; feature restrictions in DirectQuery
- [[file-based-data-sources-power-bi]] — `atomic` — Excel, CSV, JSON: detection behaviour and OneDrive vs local distinction
- [[cloud-data-sources-onedrive-sharepoint]] — `atomic` — live connection vs copy; automatic refresh; URL format requirement
- [[database-authentication-types]] — `atomic` — SQL auth, Windows auth, cloud credential requirements; contact IT for access
- [[on-premises-gateway-requirement]] — `atomic` — gateway needed for on-premises databases when publishing to Power BI Service
- [[data-source-documentation-practice]] — `atomic` — document server names, auth methods, refresh schedules, owner contacts
- [[data-source-troubleshooting-quick-reference]] — `atomic` — four canonical failure modes and solutions

## Metadata

| Field | Value |
|-------|-------|
| Source file | Master Power BI Connecting to Your First Data Source.md |
| Ingestion date | 2026-08-01 |
| Word count | ~1,200 |
| Level | Beginner |
| Category | Data Model |
