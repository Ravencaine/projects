---
title: "Master Power BI: Connecting to Your First Data Source"
source: "https://medium.com/microsoft-power-bi/master-power-bi-connecting-to-your-first-data-source-5a291d80ecb2"
author:
  - "[[Janvi Gupta]]"
published: 2025-08-27
created: 2026-07-29
description: "More"
Processed: "Unprocessed"
---
Data scattered across Excel files, databases, and cloud services is a common challenge for most organizations. Power BI Desktop can connect to data from many different sources, and understanding these connections is essential for building effective reports.

![](99.System/Attachments/0!M9s-39J2PeCHJeHA.png.webp)

This blog covers the main data source categories in Power BI, with examples and step-by-step instructions for each type.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## How to Access Data Sources in Power BI

To see available data sources, in the Home group of the Power BI Desktop ribbon, select the Get data button label or down arrow to open the Common data sources list.

![](99.System/Attachments/1!2G-Xl_UVeCB_YZYNRqZhZA.png.webp)

The Get Data button is located in the Home tab of the ribbon

If the data source you want isn’t listed under Common data sources, select More to open the Get Data dialog box. The dialog organizes data sources into logical categories: All, File, Database, Power Platform, Azure, Online Services, and Other.

## Category 1: File-Based Data Sources

## Excel Workbooks — The Most Common Starting Point

Excel remains the most frequently used data source for Power BI reports. Since this data source is an Excel file, select Excel from the Get Data window, then select the Connect button.

**Example Scenario:** Monthly sales reports stored as Excel files in a shared folder. Check the Testing section for your reference.

**Steps:**

1. Click **Get Data > Excel Workbook**
2. Navigate to your Excel file location
3. The Navigator pane shows you the data. You can expand each table by selecting the arrow beside its name
4. Select the worksheets or tables you need
5. Choose **Load** to import immediately, or **Transform Data** to clean first

**Important:** When you upload Excel files from OneDrive or SharePoint, Power BI creates a connection to the file. When you upload a local file, Power BI adds a copy of the file to the workspace.

## CSV Files — Universal Data Format

Comma-separated value, or.csv files, are simple text files with rows of data that contain values separated by commas. Almost every system can export data in CSV format.

**Example Scenario:** Daily transaction exports from an e-commerce platform.

**Steps:**

1. Click **Get Data > Text/CSV**
2. Select your CSV file
3. Power BI automatically detects column separators and data types
4. Preview the data to ensure correct formatting
5. Click **Load** or **Transform Data** if adjustments are needed

## JSON Files — Structured Data Format

JSON files are common when working with web APIs or modern applications that export structured data.

**Example Scenario:** Customer data exported from a CRM system in JSON format.

**Steps:**

1. Click **Get Data > JSON**
2. Select the JSON file
3. Power BI automatically converts nested JSON structures into tabular format
4. Review the data structure in Navigator
5. Load the converted tables

## Category 2: Database Connections

## SQL Server — Enterprise Database Standard

To connect, go to Get data > More… > Database, select the preferred database, and click Connect.

**Example Scenario:** Connecting to a company’s SQL Server database containing customer and order information.

**Steps:**

1. Click **Get Data > SQL Server**
2. Enter **Server name** (e.g., `server.company.com`)
3. Enter **Database name** (optional, can browse available databases)
4. Choose connection mode:
- **Import**: This will take a snapshot of data when loading and store it
- **DirectQuery**: This will query the database at the time of run
![](99.System/Attachments/0!ULQMIo_-TmwqJhMr.png.webp)

![](99.System/Attachments/0!re7WWeVjxBN4sfyJ.png.webp)

**Authentication:** You’ll need to provide database credentials. Contact your IT department for the appropriate login information.

## MySQL and PostgreSQL — Popular Open Source Options

The process is similar to SQL Server connections. These databases are common in web applications and smaller organizations.

**Steps:**

1. Click **Get Data > MySQL database** (or PostgreSQL)
2. Enter server details and credentials
3. Select tables to import
4. Choose Import or DirectQuery mode

**Note:** Some database connectors may require additional drivers to be installed on your computer.

## Category 3: Cloud-Based Data Sources

## OneDrive for Business — Microsoft Cloud Integration

When you upload Excel files from OneDrive or SharePoint, Power BI creates a connection to the file. This means updates to the source file automatically reflect in your Power BI reports.

**Example Scenario:** Team collaboration files stored in OneDrive that need regular reporting.

**Steps:**

1. Click **Get Data > OneDrive for Business**
2. Sign in with your Microsoft 365 credentials
3. Browse to locate your file
4. Select the file and click **Connect**

## SharePoint Lists — Collaborative Data Management

SharePoint lists function like simple databases that business users can manage without technical expertise.

**Example Scenario:** Project tracking list maintained by a project management team.

**Steps:**

1. Click **Get Data > SharePoint Online List**
2. Enter your SharePoint site URL
3. Authenticate with your credentials
4. Select the specific list you want to connect to
5. Choose columns to include in your report

## Category 5: Web and Online Service Connections

## Web Data Sources — Direct from Websites

Power BI can extract data directly from web pages that contain tables.

**Example Scenario:** Stock prices or currency exchange rates from financial websites.

**Steps:**

1. Click **Get Data > Web**
2. Enter the website URL
3. Power BI scans the page and displays available tables
4. Select the table containing your desired data
5. Load or transform as needed
![](99.System/Attachments/1!5G1T9xt_N83L6QFSg32dNA.png.webp)

Here is the sharepoint online file path not a local one.

![](99.System/Attachments/1!PEkiJbgnJy89F0Ch6O4lFw.png.webp)

Sign in for Authentication

## REST APIs — Real-time Data Integration

APIs provide direct access to live data from various online services.

**Example Scenario:** Sales data from Shopify or customer metrics from a custom web application.

**Steps:**

1. Click **Get Data > Web**
2. Enter the API endpoint URL
3. Configure authentication (API keys, OAuth tokens)
4. Power BI automatically parses JSON responses into tables
5. Select relevant data to import
![](99.System/Attachments/0!sDKZkEvTkulJK3Em.webp)

**Note:** API connections often require technical knowledge of authentication methods and endpoint URLs.

## Understanding Connection Modes

When you connect to data in Power BI, you’re given a choice between two major connection modes: Import (which we used previously) and DirectQuery.

### Import Mode

- Power BI pulls the data from your source and stores it locally within the.pbix file
- **Advantages:** Fast performance, full Power BI feature support
- **Best for:** Data that doesn’t change frequently, smaller datasets

### DirectQuery Mode

- Data remains in the source and is queried on-demand
- **Advantages:** Always current data, handles large datasets
- **Limitations:** Some Power BI features (like certain DAX functions, data transformations, and calculated tables) are restricted or unavailable
![](99.System/Attachments/1!4W3UwkFpdp5DO78GcbCMfw.png.webp)

You can check Storage mode Here

## Common Connection Issues and Solutions

### Authentication Problems

Most connection failures relate to incorrect credentials or permissions.

**Solutions:**

- Verify username and password with your IT department
- Ensure your account has read permissions on the data source
- For cloud services, check that appropriate licenses are assigned

### Network Connectivity Issues

If your source goes down, your report breaks or loads slowly.

**Solutions:**

- Test network connectivity to the data source
- Check firewall settings with IT support
- For on-premises databases, ensure the Power BI Gateway is properly configured

### Data Type Recognition Problems

Sometimes Power BI incorrectly identifies data types (dates as text, numbers as text).

**Solutions:**

- Use **Transform Data** to correct data types before loading
- Check for hidden characters or formatting issues in source data
- Ensure consistent data formats across your data source

## Best Practices for Data Connections

### Choose the Right Connection Mode

- Use **Import** for most scenarios requiring fast performance
- Use **DirectQuery** when data freshness is critical and datasets are large
- After setup, you can not switch a data source from import to direct query

### Plan for Data Refresh

- **Local files:** Manual refresh required
- **Cloud files:** Automatic refresh when source files change
- **Databases:** Schedule regular refreshes in Power BI Service

### Document Your Connections

Keep a record of:

Server names and database names

- Authentication methods used
- Refresh schedules and dependencies
- Contact information for data source owners

## Testing Your First Connection

**Start Simple:** Begin with an Excel file or CSV that you can easily access and understand.

**Step-by-Step Test:**

1. Open Power BI Desktop.
2. Click **Get Data** in the Home ribbon and select **Excel Workbook** from the common sources. Another way is to directly select the Excel workbook in the Home ribbon.
3. Choose a simple Excel file with clear data.
4. Load the data and verify it appears correctly in the Fields pane.
![](99.System/Attachments/1!5RGtN_4NWwXgcoBNuQScAg.png.webp)

Select File

![](99.System/Attachments/1!F90MNJ31rmIEngc44lx4cg.png.webp)

Load Data

![](99.System/Attachments/1!USvumNBjsy_IVCvRVMuiAw.png.webp)

Verify the data

**Verification:** Once you load the tables, the Fields pane shows you the data. You can expand each table by selecting the arrow beside its name.

## Troubleshooting Quick Reference

**Problem:** Can’t see expected data after connecting.  
**Solution:** Check data source permissions and verify correct table selection.

**Problem:** Connection works in Power BI Desktop but fails after publishing.  
**Solution:** Configure data source credentials in Power BI Service.

**Problem:** Data appears but looks incorrectly formatted.  
**Solution:** Use Transform Data to adjust data types and formatting.

**Problem:** Large datasets load slowly.  
**Solution:** Consider DirectQuery mode or data source optimization.

### Conclusion

Power BI’s strength lies in its ability to connect to virtually any data source. Start with simple connections to build confidence, then gradually work toward more complex scenarios, such as APIs and real-time data sources.

**The key is understanding the characteristics of your data source, selecting the appropriate connection mode, and planning for ongoing data refresh requirements.**

Once you’ve successfully connected to a data source, your next challenge is ensuring the data is clean and properly formatted for analysis. Raw data often contains inconsistencies, missing values, and formatting issues that need to be addressed before creating visualizations.

In our next article, we’ll explore **Power Query Editor** — Power BI’s built-in data transformation tool that helps convert messy, real-world data into analysis-ready datasets.

Before that, tell me **which data source you will connect first?** Share your experience below — are you starting with Excel files, jumping into databases, or tackling APIs? Don’t hesitate to ask questions if you hit any connection roadblocks. We’ve all wrestled with authentication errors and mysterious connection failures! Your challenges and wins help the entire Power BI community learn together. 🙌😊

**Connect me on LinkedIn —** [**Janvi Gupta**](https://www.linkedin.com/in/janvisgupta/)

![](99.System/Attachments/0!YdneSlc4PCuH5Ddj.webp)

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-end) **🎁**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://powerbi-masterclass.short.gy/linktree?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----5a291d80ecb2---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

powerbi-masterclass.short.gy

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Data Model

**Tags:** Tutorial, Data Model