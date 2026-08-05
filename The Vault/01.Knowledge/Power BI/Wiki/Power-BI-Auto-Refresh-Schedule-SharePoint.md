---
created: 2026-08-05
updated: 2026-08-05
source: Auto-Refresh SharePoint Excel Data in Power BI (Boniface Muchendu)
note_type: atomic
tags: [power-bi, sharepoint, auto-refresh, scheduled-refresh, on-demand, gateway, power-bi-service]
---

# Power BI Auto-Refresh Schedule SharePoint

Automatic refresh behaviour for SharePoint Online Excel data sources in Power BI Service — refresh frequency, on-demand refresh, daily limits, and refresh history monitoring.

## Auto-Refresh Frequency

Power BI Service automatically checks SharePoint Online for changes and refreshes the dataset approximately **every hour** when a change is detected.

| Setting | Value |
|---------|-------|
| Automatic refresh | ~Hourly (Power BI managed) |
| Gateway required | No (cloud source) |
| Configurable frequency | No — managed by Power BI Service |
| Minimum gap between auto-refreshes | ~1 hour |

The hourly refresh is designed for scenarios where the Excel file on SharePoint is updated periodically (e.g., daily or multiple times a day). Changes made to the file are picked up within roughly 1 hour.

## On-Demand Refresh

If you need immediate updates before the next hourly cycle:

1. Navigate to the workspace in Power BI Service
2. Find the dataset → click **Refresh Now**

**Daily limits on on-demand refreshes:**

| License | On-demand limit |
|---------|----------------|
| Power BI Pro | 8 per dataset per day |
| Power BI Premium | 48 per dataset per day (or unlimited with XMLA) |

## Refresh History

Refresh History in Power BI Service provides a log of all refresh attempts:

- **Start time** and **end time** of each refresh
- **Status**: Success / Failed / Partial
- **Error details** for failed attempts (including credential expiry, file not found, etc.)

Access: Dataset → **Refresh History** (ellipsis menu).

## When to Use On-Demand vs Scheduled

| Scenario | Approach |
|---------|---------|
| Excel updated once a day | Let auto-refresh handle it |
| Need latest data immediately | On-demand Refresh Now |
| Frequent intra-day updates | Power BI Premium + more frequent scheduled refreshes |
| Sensitive/large dataset | Scheduled refresh (Premium) with monitoring |

## No Gateway Required

SharePoint Online is a **cloud source**. Power BI Service connects directly to SharePoint via OAuth2 — no on-premises data gateway is needed, unlike SQL Server or file-system sources.

## Optimising Refresh Performance

- Keep the Excel file lean — avoid large unused worksheets
- Remove unnecessary columns before publishing (use Transform Data)
- Publish only the necessary tables/queries
- Monitor Refresh History for slow or failed refreshes

## Related

- [[SharePoint-Excel-Web-Connector-Power-BI]]
- [[Power-BI-OAuth2-Org-Account-Authentication]]
- [[Power-BI-SharePoint-Refresh-Frequency-MS-Learn]]
