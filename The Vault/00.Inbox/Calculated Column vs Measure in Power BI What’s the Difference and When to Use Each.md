---
title: "Calculated Column vs Measure in Power BI: What’s the Difference and When to Use Each?"
source: "https://medium.com/write-a-catalyst/calculated-column-vs-measure-in-power-bi-whats-the-difference-and-when-to-use-each-7378a54df93b"
author:
  - "[[Anurodh Kumar]]"
published: 2025-05-24
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oT2dce5JUr0MvjInG20Avg.png)

image by Anurodh Kumar

Power BI has revolutionized the way we analyze and visualize data. But when you dive deeper, especially into DAX (Data Analysis Expressions), you’ll encounter two powerful tools that often confuse beginners: Calculated Columns and Measures.

Both serve different purposes, and choosing the right one can drastically improve your report’s performance and logic. So, let’s break them down with simple examples and use cases.

## 🟨 What is a Calculated Column?

A Calculated Column is like adding a new column to your dataset using a DAX formula. It is evaluated row by row, just like Excel.

When you create a calculated column, Power BI evaluates the expression as data loads into the model, and stores the result in memory — making it part of the data model.

🔧 Syntax Example:

```c
FullName = Employees[FirstName] & " " & Employees[LastName]
```

This new column FullName becomes a physical column in the Employees table.

## ✅ Use Calculated Columns When:

- You need a new field for slicing, grouping, or filtering visuals.
- You want to create relationships between tables using new data columns.
- You need row-level calculations during data modeling.

## 🟩 What is a Measure?

A Measure is a DAX formula that performs calculations on aggregated data. Unlike calculated columns, measures are calculated on the fly, based on the filter context of your report (like slicers, rows, or columns).

🔧 Syntax Example:

```c
Total Sales = SUM(Sales[Amount])
```

When you add this measure to a visual, it sums the Amount values based on the current context — for example, by year, region, or product.

## ✅ Use Measures When:

- You need dynamic, context-sensitive calculations.
- You’re aggregating data (SUM, COUNT, AVERAGE, etc.).
- You want to optimize performance — since measures don’t take up storage space like calculated columns.

## 📊 Real-World Example

Let’s say you have a Sales table with Quantity and Price columns.

- Calculated Column: TotalAmount = Sales\[Quantity\] \* Sales\[Price\] This creates a physical column for TotalAmount in every row.
- Measure: Total Sales = SUMX(Sales, Sales\[Quantity\] \* Sales\[Price\]) This evaluates only when used in a visual, and adjusts dynamically based on filters.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*XjJXEEpnEaM37-GY)