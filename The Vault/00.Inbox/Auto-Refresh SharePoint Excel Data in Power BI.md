---
title: "Auto-Refresh SharePoint Excel Data in Power BI"
source: "https://databear.com/auto-refresh-sharepoint-excel-data-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2024-09-29
created: 2026-08-04
description: "Learn how to connect Power BI with Excel files stored on SharePoint. This blog explains how to establish live data connections, automate refresh schedules,"
Processed: "Unprocessed"
---
##### Introduction

Keeping your Power BI reports synchronized with data stored in Excel files on SharePoint can be challenging. However, by leveraging Power BI’s capabilities, you can set up an automatic refresh that updates your reports whenever the source Excel file changes. This not only saves time but also ensures that stakeholders always have access to the latest data.

In this guide, we’ll explore how to configure Power BI to automatically refresh data from Excel files stored on SharePoint. By following these steps, you can maintain up-to-date reports without manual intervention.

##### Connecting to the Excel File on SharePoint

###### Step 1: Obtain the SharePoint File Path

First, navigate to your Excel file on SharePoint:

1. Go to the SharePoint site where your Excel file is stored.
2. Locate your Excel file (e.g., `AirportsData.csv`).
3. Click on the information icon (**ℹ️**) next to the file to open the details pane.
4. Then, scroll down to the **Path** section and copy the file URL.

*Note:* Ensure that the copied URL does not contain any query parameters starting with a question mark (`?`). If it does, remove everything from the question mark onward.

###### Step 2: Connect to the File in Power BI Desktop

Next, open Power BI Desktop:

1. Click on **Get Data** in the Home tab, and select **Web**.
2. In the URL field, paste the copied SharePoint file path.
3. After that, click **OK** to proceed.

###### Step 3: Authenticate Your Connection

Power BI will prompt you to authenticate:

1. Choose **Organizational account** as the authentication method.
2. Click on **Sign in**.
3. Enter your organizational account credentials associated with SharePoint.
4. Once signed in, click **Connect**.

###### Step 4: Load the Data

After establishing the connection:

1. Power BI will display a preview of the data.
2. If the data looks correct, click **Load** to import it into Power BI.
3. Alternatively, you can click **Transform Data** to make any adjustments using Power Query Editor.

##### Publishing the Report to Power BI Service

Once your report is ready in Power BI Desktop, the next step is to publish it to the Power BI Service.

###### Step 1: Sign In to Power BI Service

To begin:

1. In Power BI Desktop, click on **Sign In** (if you haven’t already).
2. Enter your Power BI Pro account credentials.

###### Step 2: Publish the Report

Then:

1. Click on **Publish** in the Home tab.
2. Choose the desired workspace where you want to publish the report.
3. Finally, click **Select** to confirm.

*Tip:* Even though your Power BI Desktop file is saved locally, the data source (Excel file) resides on SharePoint.

##### Configuring Automatic Data Refresh

To ensure your report automatically refreshes when the Excel file changes, follow these steps:

###### Step 1: Access the Dataset Settings

In Power BI Service:

1. Navigate to the workspace where you published the report.
2. Find your dataset, click on the **ellipsis (⋯)** next to it, and select **Settings** from the dropdown menu.

###### Step 2: Edit Data Source Credentials

Within the **Settings** page:

1. Expand the **Data source credentials** section.
2. You may see a warning about missing credentials. Click on **Edit credentials**.
3. Select **OAuth2** as the authentication method.
4. Set the **Privacy Level** to **Organizational**.
5. Then, click **Sign in** and authenticate with your organizational account.

###### Step 3: Verify the Connection

After updating the credentials:

- Ensure that the connection status shows as **Connected** without any errors.
- If there are issues, double-check your credentials and privacy level settings.

##### Understanding the Refresh Process

According to Microsoft’s documentation on [refreshing datasets imported from Excel workbooks on OneDrive or SharePoint Online](https://docs.microsoft.com/en-us/power-bi/connect-data/refresh-excel-file-onedrive), Power BI automatically checks for updates to your Excel file approximately every **one hour**. If it detects any changes, it refreshes the dataset and updates the associated reports and dashboards.

**Key Points:**

- **No Data Gateway Required:** Since the data source is in the cloud (SharePoint Online), you don’t need to set up an on-premises data gateway.
- **Automatic Refresh:** Power BI handles the refresh process without manual intervention.
- **Refresh Frequency:** The automatic refresh occurs roughly every hour, but this is managed by the Power BI Service and cannot be adjusted for this type of connection.

##### Tips and Best Practices

To make the most of this setup, consider the following tips:

- **Use Organizational Accounts:** Always authenticate using your organizational account to ensure secure access.
- **Monitor Data Changes:** When you update the Excel file on SharePoint, allow up to an hour for the changes to reflect in Power BI.
- **Perform On-Demand Refreshes:** If you need immediate updates, you can manually trigger a refresh in Power BI Service:
	- Navigate to your dataset.
		- Click on the **Refresh Now** option.
	*Note:* There are limits on the number of on-demand refreshes you can perform per day, depending on your Power BI license.
- **Check Refresh History:** Regularly review the **Refresh History** in the dataset settings to monitor the refresh process and troubleshoot any issues.
- **Optimize Your Data Model:** Keeping your data model efficient reduces refresh times and improves performance.

##### Conclusion

By following these steps, you can effortlessly set up an automatic data refresh from Excel files stored on SharePoint in Power BI. This ensures that your reports are always up-to-date, allowing you and your stakeholders to make informed decisions based on the latest data. Automating the refresh process not only saves time but also enhances the reliability of your reporting solutions.