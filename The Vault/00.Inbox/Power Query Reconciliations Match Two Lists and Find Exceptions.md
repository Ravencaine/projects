---
title: "Power Query Reconciliations: Match Two Lists and Find Exceptions"
source: "https://www.excel-university.com/power-query-reconciliations-match-two-lists-and-find-exceptions/?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
  - "[[Excel University]]"
published: 2026-08-09
created: 2026-08-13
description: "Explore Excel tips and tutorials at our blog. Sharpen your Excel skills and learn how to get your work done faster!"
Processed: "Unprocessed"
---
When you need to reconcile two lists in Excel — matching transactions, comparing account balances, or identifying exceptions — Power Query offers a more reliable and repeatable approach than manual VLOOKUP formulas. For CPAs and accountants who run the same reconciliation every month, Power Query turns a tedious, error-prone process into a structured, refreshable workflow. The result: faster close cycles, fewer missed exceptions, and a process you can hand off or repeat without rebuilding from scratch.

This post walks through how to use Power Query’s merge functionality to match two lists and surface exceptions — the records that appear in one list but not the other. No macros required, and no formula maintenance when your data changes.

## Why Power Query Works Well for Reconciliations

Traditional Excel reconciliations rely on VLOOKUP or XLOOKUP formulas to find matches, with conditional formatting or helper columns to flag exceptions. That approach works for small, one-time comparisons. But it breaks down when:

- Your source data changes shape or size each period
- You need to reconcile thousands of rows reliably
- Multiple people need to run the same process
- You want a documented, auditable transformation

Power Query handles all of these scenarios. Every step is recorded in the query editor, making the logic transparent and repeatable. When new data arrives, you refresh — and the reconciliation runs again automatically.

## How to Match Two Lists and Find Exceptions in Power Query

The core technique is a **merge query** using a left anti join or full outer join, depending on what you need to find. Here is the step-by-step process.

### Step 1: Load Both Lists into Power Query

1. Format each list as an Excel Table (Insert > Table).
2. Select the first table, then go to **Data > Get & Transform > From Table/Range**.
3. In the Power Query Editor, rename the query clearly (e.g., *GL\_Transactions*).
4. Choose **Close & Load To… > Only Create Connection**.
5. Repeat for the second list (e.g., *Bank\_Statement*).

### Step 2: Merge the Queries

1. Go to **Data > Get Data > Combine Queries > Merge**.
2. Select your first query as the primary table.
3. Select your second query as the related table.
4. Click the matching column in each table (e.g., a transaction ID or reference number).
5. Choose your **Join Kind** based on what you want to find (see table below).
6. Click OK, then expand the merged column to bring in fields from the second table.

### Step 3: Filter for Exceptions

After expanding the merged column, rows with **null** values in the joined fields represent exceptions — records that did not find a match. Filter the expanded column to show only nulls to isolate your unmatched items.

## Choosing the Right Join Type

| Join Kind | What It Returns | Best For |
| --- | --- | --- |
| Left Outer | All rows from List 1; matched rows from List 2 | Finding what’s in GL but not in bank |
| Right Outer | All rows from List 2; matched rows from List 1 | Finding what’s in bank but not in GL |
| Full Outer | All rows from both lists | Complete two-way exception report |
| Left Anti | Only rows from List 1 with no match in List 2 | Clean exception-only output from List 1 |
| Right Anti | Only rows from List 2 with no match in List 1 | Clean exception-only output from List 2 |
| Inner | Only matched rows | Confirming what reconciles cleanly |

**Recommended for most reconciliations:** Run a *Left Anti* join and a *Right Anti* join as two separate queries, then append them. This gives you a single, clean exceptions list showing everything unmatched from either side.

## Practical Example: Bank Reconciliation

Suppose your GL export has a *Reference* column and your bank statement has a *Check Number* column. Both represent the same transaction identifier, but the column names differ. In the merge dialog, simply select *Reference* from the first query and *Check Number* from the second — Power Query matches on values, not column names. After merging with a Full Outer join and expanding, add a custom column to label each row:

```
= if [GL_Amount] = null then "Bank Only" else if [Bank_Amount] = null then "GL Only" else "Matched"
```

Filter this column to exclude “Matched” rows, and you have your exception report — ready to refresh next month with one click.

## When to Use Power Query vs. Formulas for Reconciliation

- **Use Power Query when** the reconciliation repeats monthly, involves large datasets, or needs to be shared with others.
- **Use XLOOKUP/formulas when** it’s a one-time comparison on a small dataset and you need results immediately without setting up queries.
- **Not ideal for Power Query when** your organization restricts external data connections or you need real-time cell-level interactivity.

## Frequently Asked Questions

### Can Power Query reconcile lists with different column names?

Yes. When you set up the merge, you select the matching columns from each table independently. The column names do not need to match — only the values need to correspond. You can also rename columns in Power Query before merging to keep your output clean.

### What if my two lists have duplicate entries?

Duplicates can cause a merge to expand unexpectedly, multiplying rows. Before merging, consider whether you need to deduplicate or aggregate one or both lists first. Power Query’s *Remove Duplicates* and *Group By* steps handle this cleanly before the merge runs.

### Does this work with data from different sources, like a CSV and an Excel file?

Yes. Power Query can connect to Excel tables, CSV files, databases, and other sources simultaneously. You load each source as a separate query, then merge them the same way. This makes it especially useful when your GL export and bank statement come in different file formats.

### How do I refresh the reconciliation when new data comes in?

If your source data is in Excel Tables, simply update the table data and then right-click your output query and select **Refresh**. Power Query reruns every transformation step automatically. If your sources are external files, make sure the file paths remain consistent and refresh the same way.

## Build Reconciliation Skills That Earn CPE

The workflow above gives you a solid foundation for Power Query reconciliations. If you want structured, step-by-step training on Power Query — including hands-on exercises built around real accounting scenarios — Excel University offers CPE-eligible courses designed specifically for CPAs and finance professionals. Browse available courses at [store.excel-university.com](https://store.excel-university.com/), or compare training pass options at [excel-university.com/training-passes](https://www.excel-university.com/training-passes) to find the right fit for your learning goals.

Posted in ,