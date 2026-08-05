---
title: "Power Query Folder Import: Combine Files Automatically"
source: "https://databear.com/power-query-folder-import/"
author:
  - "[[Boniface Muchendu]]"
published: 2026-01-19
created: 2026-08-04
description: "Learn how to use Power Query folder import to combine multiple Excel or CSV files and refresh data automatically with each new file."
Processed: "Unprocessed"
---
The **Power Query folder import** feature is one of the most efficient ways to combine multiple Excel or CSV files into a single table. It allows you to automate the consolidation process, ensuring that any new files added to the folder are automatically included when you refresh your data. However, many users run into errors because they don’t apply transformations in the correct place. In this guide, you’ll learn how to correctly use Power Query folder import and avoid the common mistakes that lead to broken queries or duplicated data.

Learn more about Power BI automation with expert-led [Power BI Training](https://databear.com/power-bi-training/)

##### Why Use Power Query Folder Import?

Whether you’re working in **Excel or Power BI**, using **Power Query to get files from a folder** allows you to:

- Automatically consolidate multiple files with the same structure
- Apply consistent transformations across all files
- Easily refresh your data when new files are added

It works with CSV, TXT, and Excel files and is ideal for monthly reports, sales data, or exports from other systems.

##### Step 1: Organize Your Source Folder

Place only the files you want to import into a dedicated folder. While you can filter out unwanted files later, it’s much safer to keep the folder clean.

For example, if you store your query file in the same folder as the data files, it could get counted as a data source leading to incorrect results.

##### Step 2: Use Power Query to Get Data from Folder

In Excel:

- Go to the **Data** tab > **Get Data** > **From File** > **From Folder**

In Power BI:

- Go to the **Home** tab > **Get Data** > **More** > **Folder**

Browse to the folder and Power Query will display a list of all files found.

Click **Transform Data** instead of loading immediately. This allows you to filter or clean files before combining them.

##### Step 3: Combine Files Using the Correct Method

Once you’re in the Power Query editor:

1. Click the **double-arrow** icon next to the **Content** column to combine files.
2. Choose a **sample file** for structure reference (default is the first file).
3. Adjust settings as needed, such as delimiter or data type detection.
4. Click **OK**.

Power Query will automatically create several queries, but only two are important:

- **Transform Sample File**: Used as a template for applying transformations.
- **Final Combined Query**: The result of combining all files using the template.

##### Step 4: Where People Go Wrong (And How to Fix It)

If your source files are **not clean** (e.g., multiple header rows, merged cells), you **must fix the structure in the Sample File query** not in the final combined query.

For example, if your files have headers spanning two rows:

1. Go to the **Transform Sample File** query.
2. Remove the automatic “promote headers” step.
3. Use transformations like **transpose**, **merge columns**, and **promote headers** to create a single header row.
4. These steps will be applied to **every file in the folder** before they are combined.

If transformations are applied only to the final combined query, errors may occur due to inconsistent file structures.

##### Step 5: Final Clean-up and Data Load

Once your data is correctly combined and structured:

- Rename your final query (e.g., `Orders`) for clarity
- Delete unnecessary columns (like Source.Name)
- Use **Transform > Detect Data Type** to reset column types if needed

In Excel:

- Use **Close & Load To** to choose where the data goes (e.g., a table, PivotTable, or data model)

In Power BI:

- Use **Close & Apply** to load the data into your model

##### Step 6: Automatically Refresh When New Files Are Added

This is the true power of the folder import method.

When a new file is added to the folder:

1. Click **Refresh** in Excel or Power BI
2. Power Query re-applies all transformation steps
3. Your new data is instantly included in your model or report

This method eliminates the need to manually import each file, saving time and reducing error.

##### Summary: Best Practices for Power Query Folder Import

- Keep your source folder clean and only include relevant files
- Always choose **Transform Data** when importing
- Apply transformations in the **Sample File** query when needed
- Use consistent sheet or table names across Excel files
- Refresh to automatically include new data
- Rename your queries and remove unnecessary columns before loading

By following these steps, you’ll create a flexible, scalable solution that handles regular file imports with ease.

For more in-depth Power BI techniques, explore our [Power BI Training](https://databear.com/power-bi-training/)