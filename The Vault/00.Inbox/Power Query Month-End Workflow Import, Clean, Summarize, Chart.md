---
title: "Power Query Month-End Workflow: Import, Clean, Summarize, Chart"
source: "https://www.excel-university.com/power-query-month-end-workflow-import-clean-summarize-chart/"
author:
  - "[[Excel University]]"
published: 2026-07-26
created: 2026-08-13
description: "Explore Excel tips and tutorials at our blog. Sharpen your Excel skills and learn how to get your work done faster!"
Processed: "Unprocessed"
---
A Power Query month-end workflow lets accountants automatically import, clean, summarize, and visualize financial data in a repeatable, one-click process — eliminating the manual copy-paste routines that consume hours every close cycle. When built correctly, this workflow transforms raw exports from your ERP or accounting system into a polished, chart-ready summary with virtually no manual intervention after the initial setup.

This post walks through each stage of that workflow using practical, accountant-focused examples you can adapt immediately.

## Why Power Query Is Built for Month-End Close

Most month-end processes involve the same steps repeated every period: export a report, clean up the formatting, build a summary, and update a chart. Power Query automates the first three steps and feeds the fourth. Once your queries are built, refreshing the entire workflow takes seconds — not hours.

Power Query also creates an auditable, documented transformation process. Every step is recorded in the Applied Steps pane, so reviewers and auditors can trace exactly how raw data became a final report.

## Stage 1: Import Your Source Data

The workflow starts with connecting Power Query to your data source. Common sources for accountants include:

- **CSV or Excel exports** from QuickBooks, Sage, NetSuite, or similar systems
- **Folders of files** — for example, a folder containing one trial balance export per month
- **SharePoint or OneDrive** for team-shared workbooks
- **SQL databases** for larger organizations with direct data access

To connect to a folder of monthly exports, go to **Data → Get Data → From File → From Folder**. Point Power Query to the folder, and it will automatically combine all files into a single table. This is especially powerful when you drop a new monthly export into the folder and refresh — the new data is pulled in automatically.

### Best Practice: Standardize Your Source File Names

Use a consistent naming convention like `TrialBalance_2026-06.csv` so Power Query can sort and filter files by period without additional configuration.

## Stage 2: Clean the Data

Raw accounting exports are rarely clean. Power Query handles the most common issues accountants face:

- **Remove header/footer rows** — Use *Remove Top Rows* or *Remove Bottom Rows* to strip out report titles, date stamps, and totals rows that ERP systems add automatically.
- **Promote headers** — Use *Use First Row as Headers* when column names are embedded in row 1 of the export.
- **Fix data types** — Change amount columns from Text to Decimal Number so calculations work correctly. Power Query often misdetects these from CSV files.
- **Trim and clean text** — Account names with leading spaces or inconsistent capitalization will break grouping. Use *Transform → Format → Trim* and *Clean*.
- **Filter out blank rows** — Filter the Account column to remove null or empty rows that appear at the bottom of many exports.
- **Unpivot columns** — If your export has months as column headers (Jan, Feb, Mar…), unpivot those columns into a single “Month” column and “Amount” column for proper summarization.

Each of these steps is recorded in the Applied Steps pane on the right side of the Power Query Editor. You can rename steps with descriptive labels like “Remove ERP Footer Rows” to make the logic self-documenting.

## Stage 3: Summarize with Group By

Once the data is clean, use Power Query’s **Group By** feature to build your summary. This is the equivalent of a SUMIF or pivot table — but it runs automatically on refresh.

A practical example: group by **Department** and **Account Category**, then sum the **Amount** column. The result is a clean summary table that feeds directly into your Excel model.

To apply Group By: in the Power Query Editor, go to **Transform → Group By**. Select your grouping columns, choose *Sum* as the operation, and point it at your amount column. Power Query generates the M code automatically.

### When to Use Group By vs. a Pivot Table

Use Group By inside Power Query when you want the summarized data to load directly into a structured Excel table that other formulas or charts reference. Use a PivotTable when you need interactive slicing and filtering by end users. Both approaches can coexist in the same workbook.

## Stage 4: Load and Chart the Results

Load your cleaned, summarized query to an Excel table by selecting **Close & Load To** and choosing *Table* in an existing worksheet. This table becomes the live data source for your chart.

Build your chart directly from the loaded table — not from a separate copy of the data. When you refresh the query next month, the table updates and the chart updates automatically. No manual chart editing required.

Recommended chart types for month-end reporting:

- **Clustered bar chart** — Compare actuals vs. budget by department
- **Line chart** — Show revenue or expense trends across 12 months
- **Waterfall chart** — Visualize variance from prior period

## Putting It All Together: The One-Click Refresh

Once the workflow is built, your month-end process looks like this:

1. Export the trial balance or transaction detail from your accounting system
2. Drop the file into the designated folder (or overwrite the existing source file)
3. Open the Excel workbook and press **Refresh All** (Data tab, or Ctrl+Alt+F5)
4. Review the updated summary table and charts

That’s the entire process. The import, cleaning, and summarization all happen automatically in the background.

## Limitations to Know

- Power Query does not write data back to source systems — it is read-only
- Very large datasets (millions of rows) may be slow in Excel; consider Power BI for those scenarios
- If source file structure changes (column names, column order), queries may break and need updating

## Take Your Skills Further with CPE Credit

Building this workflow once in a guided environment — with real data and step-by-step instruction — is far more effective than piecing it together from scattered tutorials. Excel University offers structured, hands-on Power Query courses designed specifically for accountants, and many qualify for CPE credit.

Browse available courses at [store.excel-university.com](https://store.excel-university.com/), or compare training pass options at [excel-university.com/training-passes](https://excel-university.com/training-passes) to find the best fit for your learning goals and CPE requirements.

Posted in