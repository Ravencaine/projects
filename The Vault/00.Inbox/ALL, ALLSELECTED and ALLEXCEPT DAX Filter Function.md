---
title: "ALL, ALLSELECTED and ALLEXCEPT DAX Filter Function"
source: "https://databear.com/all-allselected-and-allexcept-dax-filter-function/"
author:
  - "[[Boniface Muchendu]]"
published: 2022-11-19
created: 2026-08-04
description: "I'm going to talk about 3 DAX functions, that is ALL, ALLSELECTED, and ALLEXCEPT DAX Filter Function. When and where to use all this Function"
Processed: "Unprocessed"
---
Welcome back to another post to help you on your Power BI journey. Today I’m going to talk about 3 DAX functions, that is ALL, ALLSELECTED, and ALLEXCEPT DAX Filter Function.

Here is the dataset

![All Function ](99.System/Attachments/All_Function_.png)

Here we have two slicers. One is for the Region and Category. The data help us understand the difference between ALL, ALLSELECTED, and ALLEXCEPT. Let start.

## DAX ALL Filter Function

Here is the Syntax

**ALL( \[\<table> | \<column>\[, \<column>\[, \<column>\[,…\]\]\]\] )**

**Table** The table that you want to clear filters on.

**Column** The column that you want to clear filters on.

Let’s create **ALL** Functions using the syntax above. We need to use Calculate function, which is going to evaluate an expression in the context of the modified filters and we will modify the sales.

![All Function Dax filter](99.System/Attachments/All_Function_Dax_filter.png)

When using the ALL function, we can either give a table name or a column name. In our case, we when provided the column name. But I will explain the difference between the whole table using and using this one column.

So basically, the ALL function is useful for clearing filters and creating calculations on all the rows in the table. It’s going to remove all the filters on this category column. Instead of a column, if we are going to use the whole table name. That means it’s going to remove all the filters that are going to apply to this table.

![All Function Dax filter](99.System/Attachments/All_Function_Dax_filter.gif)

You will notice in the image above the **Sale (ALL) column** measure gives us the same value for all the Categories when the Category filter is applied, this is because it’s calculating the total sales and removing all the filters on this Category column. That means it’s not going to consider any of these categories.

If we select all Region filters, you will see the value is changing. ALL filter function to remove all the filters that are being applied on the Category column, not on the Region or any other column.

If we use the table name represented by **Sale (ALL) Table** not any particular column name, you will notice that no matter what we do, with the filter the total sales remain the same.

And the difference between using a table and a column on the ALL filter function.

## DAX ALLSELECTED Filter Function

Here is the syntax

**ALLSELECTED(\[\<tableName> | \<columnName>\[, \<columnName>\[, \<columnName>\[,…\]\]\]\] )**

**tableName** The name of an existing table, using standard DAX syntax. This parameter cannot be an expression. This parameter is optional. columnName The name of an existing

**column** using standard DAX syntax, usually fully qualified. It cannot be an expression. This parameter is optional.

ALLSELECTED function removes context filters from columns and rows in the current query while retaining all other context filters or explicit filters.

We will use the calculate functions that are going to evaluate our expression, we can directly use our measure which is total sales.

ALLSELECTED will ignore the filter which you have applied inside the query while keeping filters that are coming from outside the query. ALLSELECTED has two parameters choose table and column.

If we select all, in this Category filter, you will see in the image above the values of **Totalsale** all and **Sale (ALLSELECTED) Table** is the same. This is because ALLSELECTED filters the data with the query from outside

## DAX ALLEXCEPT Filter Function

Here is the syntax

**ALLEXCEPT(\<table>,\<column>\[,\<column>\[,…\]\])**

**Parameters**

**Table** The table over which all context filters are removed, except filters on those columns that are specified in subsequent arguments.

**Column** The column for which context filters must be preserved.

ALLEXCEPT Functions remove all context filters in the table except filters that have applied to the specified column.

![All Function Dax filter](99.System/Attachments/All_Function_Dax_filter-1.gif)

ALLEXCEPT returns all the rows in the table except for those rows that are not affected by a specified column filter or multiple columns.  
If we apply any filter to the region, it’s not going to consider them it’s going to ignore them.

Read more about Apps in Power BI [here](https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-create-distribute-apps).