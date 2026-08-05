---


title: "Power Query Remove Duplicates"
created: 2026-07-28
updated: 2026-08-02
tags: [power-query, pattern]
note_type: reference
description: "Remove Duplicates in Power Query — deduplication of rows. Critical pitfall: duplicate removal is based on all visible columns unless specific columns are selected first. From Dunlop."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Power Query: Remove Duplicates

Removes duplicate rows from a table based on **all visible columns** or **selected columns**.

## How It Works

Power Query keeps the **first occurrence** of each unique row and removes subsequent duplicates.

## The Critical Pitfall

In a table of stock prices by day, if you remove duplicates based on stock symbol alone, **only one row per stock** will be retained — regardless of how many days of data exist.

> **Always check which columns are selected before removing duplicates.**

## Example: Safe Duplication Removal

```
1. Select only the columns that define uniqueness (e.g., OrderID + LineItemID)
2. Home → Remove Duplicates
3. Result: one row per unique combination
```

## Removing Duplicates vs. Group By

| Operation | Result |
|-----------|--------|
| Remove Duplicates | Keeps one row per unique key; discards all other columns |
| Group By | Groups by key and aggregates other columns (count, sum, etc.) |

## Source Reference

Chapter 8, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
