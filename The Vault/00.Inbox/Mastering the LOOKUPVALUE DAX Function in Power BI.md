---
title: "Mastering the LOOKUPVALUE DAX Function in Power BI"
source: "https://databear.com/mastering-the-lookupvalue-dax-function-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2023-04-15
created: 2026-08-04
description: "LOOKUPVALUE DAX function in Power BI with this comprehensive blog post. Learn its syntax, use cases, and important considerations for efficient data analysis."
Processed: "Unprocessed"
---
In today’s blog post, we will discuss the LOOKUPVALUE function: what it is, how to use it, and what you should consider before using this DAX function.

## What is the LOOKUPVALUE Function?

The LOOKUPVALUE DAX function returns the value for the row that meets all criteria specified by one or more search conditions. In other words, it allows you to search for a particular value based on specific criteria and return the corresponding result.

#### Syntax of LOOKUPVALUE Function

> LOOKUPVALUE(Result\_ColumnName, Search\_ColumnName, Search\_Value, \[Alternate\_Result\])

1. Result\_ColumnName: The column containing the values you are looking for.
2. Search\_ColumnName: The criteria by which you have to search.
3. Search\_Value: The value you want to search for; this can be a column or a particular value.
4. Alternate\_Result (optional): The value to return if no result is found.

## Use Cases

### Example 1: Employee and Master Table

![Model table ](99.System/Attachments/Model_table_.png)

Suppose we have an Employee table and a Master table. The Employee table contains employee names, company names, position names, and states, while the Master table has state and country information. We want to create a new column in the Employee table that shows the corresponding country for each state.

![Employee](99.System/Attachments/Employee.png)

To achieve this, we can use the LOOKUPVALUE function as follows:

> Country = LOOKUPVALUE(Master\[Country\], Master\[State\], Employee\[State\])

### Example 2: Fact Internet Sales Table

![internet](99.System/Attachments/internet.png)

In another example, we have a Fact Internet Sales table containing customer keys, sales order numbers, order quantities, and other columns. Our goal is to find the sales order number corresponding to a particular customer key.

To do this, we can create a new measure using the LOOKUPVALUE function:

> Sales Order Number by Customer Key = LOOKUPVALUE(Fact\[Sales Order Number\], Fact\[Customer Key\], 148, “N/A”)

## Points to Consider for LOOKUPVALUE

1. If there is a relationship between the result and search table, using the [RELATED function](https://databear.com/related-dax-function-in-power-bi/) instead of LOOKUPVALUE is more efficient and provides better performance.
2. The search value and alternate result parameters are evaluated before the function iterates through the rows of the search table.
3. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security rules.

We hope this blog post has given you a better understanding of the LOOKUPVALUE DAX function and its use cases. If you have any questions or concerns, please let us know in the comment section below.

You can visit the rest of our [blog](https://databear.com/blog/) posts for more insightful information on everything related to Power BI.

Learn more about Power BI by taking our training [course](https://databear.com/power-bi-training/).

Check out our [consulting](https://databear.com/power-bi-consulting/) page.