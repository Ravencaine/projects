---
title: "Power Query Merge Duplicates: Fix One-to-Many Join Issues"
source: "https://databear.com/power-query-merge-duplicates/"
author:
  - "[[Boniface Muchendu]]"
published: 2026-01-19
created: 2026-08-04
description: "Fix one-to-many merge issues in Power Query using aggregation and Enable Load to avoid duplicates and keep your data model clean."
Processed: "Unprocessed"
---
**Power Query merge duplicates** are a common issue when joining tables in Power BI, especially when working with lookup tables that contain multiple matching rows. If you are not careful, **Power Query merge duplicates** can quickly turn a clean dimension table into a one-to-many mess that breaks relationships, inflates row counts, and causes inaccurate reporting.

In this article, you will learn how to fix Power Query merge duplicates by using aggregation during the merge process and by disabling unnecessary tables with Enable Load. These simple techniques help you maintain a clean data model while still enriching your data with the information you need.

> Interested in deepening your Power BI skills? Explore our [Power BI Training Programs](https://databear.com/power-bi-training/)

##### The Scenario: Joining Customer Tables on Email Address

In this example, we have two tables:

- `DimCustomer` contains core customer data such as name, email, and subscription status.
- `CustomerLookup` includes additional information like company, address, and state.

We want to join these tables to enrich our customer records with company data. While **email address** is not an ideal join key, it’s sometimes the only available option when pulling from disparate systems.

Using Power Query’s **Merge Queries** feature, we attempt to join on email. On preview, the results look fine two out of two matches. But when we expand the new column, we see:

- One match for Mitchell (as expected).
- **Three rows** for Brian Knight.

This immediately creates a problem: our once-clean `DimCustomer` table is now **duplicated** for each matching row in `CustomerLookup`. This makes it unsuitable for use as a **dimension table** in your data model.

##### The Problem: One-to-Many Merge Causing Duplicate Rows

In SQL, this is a classic one-to-many join issue. Instead of returning just one related row per customer, the merge returns **all matching rows**, causing duplication. If left unresolved, this can skew your measures, create ambiguous relationships, and break your model’s integrity.

##### The Solution: Aggregating in Power Query Merge

To fix this, you can **aggregate the joined table** during the merge step. Here’s how:

1. Perform the merge as usual on `EmailAddress`.
2. When expanding the merged column, choose **Aggregate** instead of Expand.
3. By default, you’ll only see `Count` options.
4. Click the small dropdown next to the count field this reveals more aggregation options.
5. Choose **Minimum**, **Maximum**, or another appropriate aggregation (in our case, any single value will do, as all company names are the same).
6. Click OK.

This returns a **single row per customer**, preserving the one-to-one structure needed for dimension tables.

##### Why This Works

By aggregating at the merge step, you’re instructing Power Query to return only **one representative value per key match**, eliminating the need to filter or deduplicate later. This is ideal when you just need one field like company name from a lookup table.

##### Bonus Tip: Using Enable Load to Keep Your Model Clean

After the merge is complete, you may not need the `CustomerLookup` table to be loaded into your Power BI model. Keeping unnecessary tables loaded can:

- Confuse end users
- Increase data model size
- Slow down refresh and processing

To avoid this:

1. In Power Query, right-click the `CustomerLookup` table.
2. Uncheck **Enable Load**.
3. The table name will appear italicized, indicating it’s not being loaded into the data model.
4. When you click **Close & Apply**, only `DimCustomer` will be loaded, but the transformation logic using `CustomerLookup` remains active.

##### Summary

Joining tables in Power Query is straightforward, but handling one-to-many relationships requires care. Here’s what you should take away:

- **Always check for duplicates** after a merge.
- Use the **Aggregate** option with **Minimum**, **Maximum**, or another summarization to avoid duplication.
- Use **Enable Load** to prevent unnecessary tables from being added to your data model.

With these techniques, your data model remains clean, fast, and user-friendly.

Explore more practical [Power BI tips and training](https://databear.com/power-bi-training)