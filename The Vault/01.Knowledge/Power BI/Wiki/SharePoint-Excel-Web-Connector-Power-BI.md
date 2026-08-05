---
created: 2026-08-05
updated: 2026-08-05
source: Auto-Refresh SharePoint Excel Data in Power BI (Boniface Muchendu)
note_type: workflow
tags: [power-bi, sharepoint, web-connector, excel, oauth2, get-data, sharepoint-online]
---

# SharePoint Excel Web Connector Power BI

Full step-by-step for connecting Power BI Desktop to an Excel file on SharePoint Online: extracting the file URL, using the Web connector, authenticating, and loading data.

## Step 1: Copy the SharePoint File Path

1. Navigate to the SharePoint site containing the Excel file
2. Click the **information icon (ℹ️)** next to the file
3. Scroll to the **Path** section in the details pane
4. Copy the file URL

**Critical:** Remove any query parameters (`?param=value`) from the URL — only keep the base file path. Query parameters cause authentication failures.

## Step 2: Connect via Web Connector in Power BI Desktop

1. Open Power BI Desktop → **Get Data** → select **Web**
2. In the URL field, paste the SharePoint file path
3. Click **OK**

## Step 3: Authenticate

1. Power BI prompts for authentication type → select **Organizational account**
2. Click **Sign in** and enter your organisational (Azure AD) credentials
3. Click **Connect**

Use organisational account credentials — not your personal SharePoint login or Windows credentials.

## Step 4: Load or Transform Data

- **Load**: import all data into Power BI (standard import mode)
- **Transform Data**: open Power Query Editor to clean, shape, or add calculated columns before loading

## Step 5: Publish to Power BI Service

1. In Power BI Desktop, click **Publish**
2. Select the target workspace
3. Click **Select** to publish

The published dataset maintains the live connection to SharePoint Online.

## Important Notes

| Topic | Detail |
|-------|--------|
| No gateway needed | SharePoint Online is cloud → Power BI Service handles refresh directly |
| Web connector vs SharePoint List | This recipe uses the Web connector for Excel/CSV files, not the SharePoint List connector |
| File must be Excel (.xlsx) or CSV | The Web connector reads the file directly; .xlsx is recommended |
| Organisational account | Must have at minimum read access to the SharePoint site and file |

## Related

- [[Power-BI-OAuth2-Org-Account-Authentication]]
- [[Power-BI-Auto-Refresh-Schedule-SharePoint]]
- [[Power-BI-SharePoint-Refresh-Frequency-MS-Learn]]
