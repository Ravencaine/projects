---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Connecting to Your First Data Source.md"
note_type: atomic
tags: [power-bi, cloud, onedrive, sharepoint, data-sources, beginner, refresh]
---

# Cloud Data Sources: OneDrive and SharePoint

OneDrive for Business and SharePoint Online are the primary cloud file storage options for Microsoft-centric Power BI deployments. The key difference from local files is the connection type: live vs copy.

## OneDrive for Business

**Connector:** Get Data → OneDrive for Business

Requires Microsoft 365 / Microsoft account authentication.

| Characteristic | Detail |
|---------------|--------|
| Connection type | **Live connection**: not a copy |
| File access | Browse to locate the file, select, connect |
| Refresh behaviour | When the source Excel/CSV/other file changes in OneDrive, Power BI automatically detects the change and refreshes on next schedule |
| Report vs data | Works for both Power BI report files (.pbix) and data files (.xlsx, .csv) stored in OneDrive |
| Authentication | Must maintain Microsoft 365 session — expired credentials break the connection |

**When to use:** Team-shared data files that are updated regularly by colleagues. Power BI reports automatically stay current without manual refresh.

## SharePoint Online Lists

**Connector:** Get Data → SharePoint Online List

Requires the SharePoint site URL (not a file path — a site URL like `https://company.sharepoint.com/sites/TeamName`).

| Characteristic | Detail |
|---------------|-------|
| Connection type | Live connection to the SharePoint list |
| What is imported | The list structure and current data |
| Authentication | Microsoft 365 credentials with read access to the site |
| Refresh | Scheduled refresh in Power BI Service reflects updates made in SharePoint |
| Limitations | Large lists may have performance implications; some column types (people, choice, lookup) require handling in Power Query |

**When to use:** Team-maintained lists for project tracking, task management, or operational data that colleagues update without touching Power BI.

## The Critical Distinction: Live vs Copy

| Source location | Connection | Auto-refresh |
|----------------|-----------|-------------|
| Local file (desktop) | Copy stored in workspace | No — manual refresh only |
| OneDrive / SharePoint | Live connection | Yes — when source file changes |

> **Always use OneDrive/SharePoint for data that changes frequently.** Local files work for static reference data or one-off analysis. Anything that lives in a shared team folder should be OneDrive or SharePoint.

## Related

- [[file-based-data-sources-power-bi]] — local file behaviour for comparison
- [[import-vs-directquery-connection]] — applies to all cloud sources
- [[data-source-documentation-practice]] — document which files are cloud vs local
