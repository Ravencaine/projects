---
title: "ALL and REMOVEFILTERS in Power BI"
source: "https://databear.com/all-and-removefilters-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2023-04-15
created: 2026-08-04
description: "Learn how to effectively use the ALL and REMOVEFILTERS DAX functions in Power BI for creating powerful measures and calculated columns. Master these filter functions for better analytical solutions."
Processed: "Unprocessed"
---
Today’s blog will discuss ALL and REMOVEFILTER’S DAX functions. These filter functions will help you create numerous measures for your beautiful Power BI reports and make complex calculations easy to work with.

### Definitions:

Let’s first discuss the definitions of ALL and REMOVEFILTERS:

1. ALL Filter: The ALL filter returns all the rows in a table or all the values in a column, ignoring any filters that might have been applied. This function is useful for clearing filters and creating calculations on all the rows in a table.
2. REMOVEFILTERS: Introduced in 2019 after the ALL filter, REMOVEFILTERS clears filters from specified tables or columns. However, there are substantial differences between these two functions, which we will discuss shortly.

Syntax:

The syntax for both filter functions is similar, except for the function name:

- ALL: ALL (TableName or ColumnName, …)
- REMOVEFILTERS: REMOVEFILTERS (TableName or ColumnName, …)

Parameters:

When working with these two filter functions, you need to provide either a table or a column name.

- Table: The table from which you want to clear the filters
- Column: The column from which you want to clear the filters

Return Value:

1. ALL: Returns a table or a column with filters removed
2. REMOVEFILTERS: Does not return a value but removes the filters from the specified table(s) or column(s)

### Comparing REMOVEFILTERS and ALL Function

Let’s explore some examples to illustrate the differences between the ALL and REMOVEFILTERS functions and their use cases in Power BI.

### ALL Functions in Power BI

Using ALL to remove slicer filters In this example, we have two measures, “Total Sales” and “Total Sales ALL,” along with two slicers for “Country” and “Color.” When using the ALL function, the slicer filters do not affect the “Total Sales ALL” measure, as it removes the filters applied.

> Formula: Total Sales ALL = CALCULATE(\[Total Sales\], ALL(DimProduct), ALL(DimSalesTerritory))

![ALL](99.System/Attachments/ALL.png)

### REMOVEFILTERS in Power BI

The REMOVEFILTERS function provides similar functionality to the ALL function but does not return a table or column. It simply clears the filters applied to the specified table or column. Here’s an example that demonstrates the use of REMOVEFILTERS in a measure.

> Formula: Total Sales REMOVEFILTERS = CALCULATE(\[Total Sales\], REMOVEFILTERS(DimProduct), REMOVEFILTERS(DimSalesTerritory))

![RemoveFliter](99.System/Attachments/RemoveFliter.png)

### Difference between ALL and REMOVEFILTERS:

While both functions remove filters, there is a significant difference in their behavior:

1. ALL: Removes filters and returns a table or a column, which can be used in other DAX functions like CALCULATE and SUMX. This makes it possible to create complex measures and calculated columns based on unfiltered data.
2. REMOVEFILTERS: This function does not return a table or a column; it only removes filters from the specified table(s) or column(s). You can use it within a CALCULATE function to remove filters, but unlike ALL, it cannot be used in conjunction with other DAX functions like SUMX.

### Conclusion:

Understanding how to work with the ALL and REMOVEFILTERS functions is crucial for creating powerful measures and calculated columns that provide accurate and meaningful insights for your business. By mastering these functions, you’ll be better equipped to develop sophisticated analytical solutions using Power BI.

We hope you found this guide helpful in understanding the differences and use cases for the ALL and REMOVEFILTERS DAX functions.

You can visit the rest of our [blog](https://databear.com/blog/) posts for more insightful information on everything related to Power BI.

Learn more about Power BI by taking our training [course](https://databear.com/power-bi-training/).