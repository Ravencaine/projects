---
title: "RELATED DAX Function in Power BI"
source: "https://databear.com/related-dax-function-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2023-04-09
created: 2026-08-04
description: "Discover the power of the RELATED DAX function in Power BI for efficient data analysis. Enhance your data visualization skills with this insightful blog post."
Processed: "Unprocessed"
---
Today, we are going to discuss the RELATED DAX function in Power BI. This function is one of the powerful relationship functions that helps in looking up related values from another table. In this blog post, we will dive into the details of how the RELATED function works and how to use it with a demo.

## What is the RELATED DAX Function?

The RELATED DAX function is used to return a related value from another table. It will look up the related value in another table and return the result. The syntax for the RELATED function is:

**RELATED(ColumnName)**

Where ColumnName is the column that contains the value you want to retrieve. The RELATED function returns a single value that is related to the current row.

### Demo: Using Adventure Works Data Warehouse Tables

In today’s example, we will be using Adventure Works Data Warehouse tables. Our data model consists of four different tables:

1. Fact Internet Sales Table
2. Dim Sales Territory Table
3. Dim Date Table
4. Dim Customer Table

Our main focus will be on calculating the sales for non-United States countries. We will be using the Sales Territory Key in the Dim Sales Territory table, which is related to the Fact Internet Sales table with a one-to-many relationship.

### Example 1: Calculating Total Sales for Non-US Countries without RELATED Function

First, let’s see how we can calculate the total sales for non-US countries without using the RELATED function. We can do this using the FILTER function only. Here’s how the measure looks like:

> Total Sales Non-US Filter =  
> CALCULATE(  
> SUM(FactInternetSales\[SalesAmount\]),  
> FILTER(  
> FactInternetSales,  
> FactInternetSales\[SalesTerritoryKey\] <> 1 &&  
> FactInternetSales\[SalesTerritoryKey\] <> 2 &&  
> FactInternetSales\[SalesTerritoryKey\] <> 3 &&  
> FactInternetSales\[SalesTerritoryKey\] <> 4 &&  
> FactInternetSales\[SalesTerritoryKey\] <> 5  
> )  
> )
> 
> ![Related table ](99.System/Attachments/Related_table_.png)

In this measure, we are calculating the sum of total sales amount and filtering the table where the Sales Territory Keys are not 1, 2, 3, 4, or 5 (which represent the United States in our data).

### Example 2: Calculating Total Sales for Non-US Countries using RELATED Function

Now let’s see how we can use the RELATED function to achieve the same result. We can create a measure using the RELATED function as follows:

> Total Sales Non-US RELATED =  
> SUMX(  
> FILTER(  
> FactInternetSales,  
> RELATED(DimSalesTerritory\[SalesTerritoryCountry\]) <> “United States”  
> ),  
> FactInternetSales\[SalesAmount\]  
> )
> 
> ![Related table ](99.System/Attachments/Related_table_.png)

In this measure, we are using the SUMX function, which takes a table and an expression. The table is generated using the FILTER function, and we use the RELATED function to look up the country value in the Sales Territory table. We then filter out the rows where the country is equal to “United States” and calculate the sum of the sales amount.

### Comparing the Two Examples

The first approach (using FILTER function only) is counter-intuitive, prone to typing errors, and might not work if any of the existing regions are split in the future. Moreover, it is slower and can have performance issues.

On the other hand, the second approach (using the RELATED function) proves more efficient as it actively looks up the country value in the Sales Territory table. The FILTER function then uses this value to determine whether or not to filter the Internet Sales row. This results in better performance and more accurate results.

### Important Points to Remember about RELATED Function

As we approach the conclusion of this blog post, it’s crucial to highlight several key points that you should keep in mind while working with the RELATED function in Power BI:

1. Firstly, the RELATED function necessitates the existence of a relationship between the current table and the table containing the related information. If a relationship is not already present, you must create one; otherwise, the function will fail to work.
2. Secondly, when performing a lookup, the RELATED function inspects all values within the specified table, irrespective of any filters that might have been applied.
3. Thirdly, the RELATED function requires a row context. As a result, its application is restricted to calculated column expressions where the current row context is unambiguous or as a nested function within an expression that utilizes a table scanning function.
4. Lastly, it’s important to note that the RELATED function is not compatible with fetching a column across weak relationships, such as many-to-many relationships. Instead, only strong relationships, like one-to-many, are supported.

### Conclusion

In this blog post, we explored the power of the RELATED DAX function in Power BI and how it can be used to fetch related values from another table. The RELATED function offers a more efficient and accurate way to calculate values based on related data, compared to using multiple FILTER functions.

You can visit the rest of our [blog](https://databear.com/blog/) posts for more insightful information on everything related to Power BI.

Learn more about Power BI by taking our training [course](https://databear.com/power-bi-training/).