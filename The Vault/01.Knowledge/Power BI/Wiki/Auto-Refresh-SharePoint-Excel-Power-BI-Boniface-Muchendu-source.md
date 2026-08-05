---
created: 2026-08-05
updated: 2026-08-05
source: Auto-Refresh SharePoint Excel Data in Power BI (Boniface Muchendu)
source_url: https://databear.com/auto-refresh-sharepoint-excel-data-in-power-bi/
note_type: source
tags: [power-bi, sharepoint, excel, oauth2, web-connector, auto-refresh, data-connectivity]
---

# Auto-Refresh SharePoint Excel Data in Power BI (Boniface Muchendu)

Full guide: connect Power BI to an Excel file on SharePoint via the Web connector + OAuth2 org account authentication, publish to Power BI Service, and configure automatic refresh (~hourly, no gateway required).

> **Type:** article
> **Author:** Boniface Muchendu (DataBear)
> **Published:** 2024-09-29
> **URL:** https://databear.com/auto-refresh-sharepoint-excel-data-in-power-bi/
> **Routed to:** Power BI

## Summary

Boniface Muchendu walks through the end-to-end process of connecting Power BI to Excel files stored on SharePoint Online: extracting the SharePoint file path, connecting via the Web connector in Power BI Desktop, authenticating with OAuth2 using an organisational account, publishing to Power BI Service, configuring data source credentials, and understanding the automatic refresh cycle (~hourly, managed by Power BI Service, no on-premises gateway needed).

## Key Claims

- SharePoint Online is a cloud data source — no on-premises data gateway is required
- The Web connector is used (not the SharePoint List connector) — paste the SharePoint file URL directly
- Authentication method: **Organizational account** (OAuth2) — not Windows credentials
- Power BI Service auto-refreshes approximately every **hour** when it detects a change in the source Excel file
- On-demand refresh is available in Power BI Service but has daily limits per license
- Refresh History in dataset settings provides troubleshooting visibility
- Any query parameters (`?...`) in the SharePoint URL must be removed before pasting

## Notable Details

- The connection is via the **Web** connector, not SharePoint Online List
- The file URL is copied from the SharePoint file details pane (information icon → Path section)
- Privacy level must be set to **Organizational** — not Public or Private
- After publishing from Power BI Desktop, re-authenticate the dataset in Power BI Service (OAuth2)
- Power BI Desktop file is local; the live data connection to SharePoint is maintained in the published dataset

## Extracted Notes

Links to notes derived from this source:

- [[SharePoint-Excel-Web-Connector-Power-BI]] — `workflow` — full step-by-step: copy path, Web connector, org account auth, transform data
- [[Power-BI-OAuth2-Org-Account-Authentication]] — `workflow` — OAuth2 vs other auth methods, sign-in, credential management
- [[Power-BI-Auto-Refresh-Schedule-SharePoint]] — `atomic` — ~hourly auto-refresh, on-demand refresh, daily limits, refresh history
- [[Power-BI-SharePoint-Refresh-Frequency-MS-Learn]] — `reference` — MS Learn reference on Excel/SharePoint refresh
- [[Author-Boniface-Muchendu]] — `author` — Boniface Muchendu, DataBear (9 sources)
