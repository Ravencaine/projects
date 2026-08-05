---
created: 2026-08-05
updated: 2026-08-05
source: Auto-Refresh SharePoint Excel Data in Power BI (Boniface Muchendu)
note_type: reference
tags: [power-bi, sharepoint, refresh, ms-learn, microsoft-docs, onedrive]
---

# Power BI SharePoint Refresh Frequency (MS Learn)

Microsoft Learn documentation on how Power BI handles automatic refresh for Excel workbooks and CSV files stored on OneDrive or SharePoint Online.

> **URL:** https://docs.microsoft.com/en-us/power-bi/connect-data/refresh-excel-file-onedrive
> **Referenced from:** [[Auto-Refresh-SharePoint-Excel-Power-BI-Boniface-Muchendu-source]]

## Summary

Key points from Microsoft's documentation on this refresh pattern:
- Power BI checks OneDrive/SharePoint Online sources approximately every **60 minutes**
- Changes in the Excel file trigger a dataset refresh within that window
- No gateway required for cloud sources
- OAuth2 (organisational account) is the required authentication method
- Scheduled refresh via Power BI Service is available for Pro users; Premium supports more frequent schedules

## Related

- [[Auto-Refresh-SharePoint-Excel-Power-BI-Boniface-Muchendu-source]]
- [[Power-BI-Auto-Refresh-Schedule-SharePoint]]
- [[Power-BI-OAuth2-Org-Account-Authentication]]
