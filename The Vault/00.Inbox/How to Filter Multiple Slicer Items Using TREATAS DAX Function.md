---
title: "How to Filter Multiple Slicer Items Using TREATAS DAX Function"
source: "https://databear.com/filtering-with-treatas-dax-functions-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2023-09-24
created: 2026-08-04
description: "Dive deep into TREATAS DAX function in Power BI. Learn how to harness the power of CONCATENATEX and TREATAS for dynamic data filtering."
Processed: "Unprocessed"
---
In this blog post, we’ll dive into the world of DAX functions, specifically focusing on the `CONCATENATEX` and TREATAS DAX function. Mastering these functions can help you leverage the full power of Power BI for enhanced data visualization and analysis.

## Understanding DAX CONCATENATEX Function

The `CONCATENATEX` function is a text-based DAX function that works by evaluating an expression for each row in a table. It then returns a concatenated string of those values, separated by a specified delimiter. Here’s the basic syntax for this function:

> **CONCATENATEX(\<Table>, \<Expression>, \[\<Delimiter>\], \[<OrderBy\_Expression>\], \[\<Order>\])**

- **Table**: The expression evaluates the rows in the table.
- **Expression**: Each row in the table evaluates this.
- **Delimiter**: This optional parameter determines what character or string will separate the concatenated values.
- **OrderBy\_Expression** & **Order**: These are optional parameters that help sort the table.

### Exploring the TREATAS DAX Function

The `TREATAS` DAX function is another powerful tool, specifically meant for table manipulation. This function treats columns from the input table as if they were from other tables. For each column, it filters out any values that are not present in the respective output column. The syntax for this function is:

> **TREATAS(\<Expression>, \<ColumnName>)**

- **Expression**: This generates the set of columns to be remapped.
- **ColumnName**: This is the name of the output column.

![TREATAS DAX](99.System/Attachments/TREATAS_DAX.png)

### Practical Use Case: Filtering with Slicers

A common use case for these functions is when working with slicers in Power BI. Slicers are a handy tool for filtering data on your report. For our example, imagine you have three cards displaying data based on sales for different months – January, February, and March. If you select any of these months in the slicer, the data in the cards changes to reflect the sales for those specific months.

Now, let’s say you want to dynamically calculate the total sales based on the months selected in the slicer. Here’s how you can do it using the TREATAS DAX function:

> **Sales Using TREATAS =**  
> **CALCULATE(**  
> **SUM(‘Sales'\[SalesAmount\]),**  
> **TREATAS(VALUES(‘Date'\[MonthName\]), ‘Date'\[MonthName\])**  
> **)**

What’s happening here is that whenever a month is selected from the slicer, the `VALUES` function fetches the unique month names, and the `TREATAS` function then uses these values to filter the data.

Additionally, with the `CONCATENATEX` function, you can also showcase the selected months. This can be done as:

> **Selected Months =**  
> **CONCATENATEX(VALUES(‘Date'\[MonthName\]), ‘Date'\[MonthName\], “, “)**

### Conclusion

Mastering `TREATAS` DAX functions can significantly enhance your data analysis capabilities in Power BI. The `CONCATENATEX` and `TREATAS` functions, in particular, are very versatile and can be extremely useful when working with slicers and trying to reflect dynamic data based on user selections. If you’re just starting with DAX, take the time to understand and experiment with these functions, as they can be instrumental in creating insightful and interactive reports.

You can visit the rest of our [blog](https://databear.com/blog/) posts for more insightful information on everything related to Power BI.

Learn more about Power BI by taking our training [course](https://databear.com/power-bi-training/).