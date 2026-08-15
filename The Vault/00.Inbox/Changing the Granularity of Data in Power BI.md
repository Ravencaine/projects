---
title: "Changing the Granularity of Data in Power BI"
source: "https://medium.com/data-science/changing-granularity-of-data-in-power-bi-3a2b81356990"
author:
  - "[[Salvatore Cagliari]]"
published: 2021-10-14
created: 2026-08-12
description: "Sometimes you need to create reports at a different granularity as you have in your data. Let’s look at how you can solve this challenge in Power BI"
Processed: "Unprocessed"
---
## Sometimes you need to create reports at a different granularity as you have in your data. Let’s look at how you can solve this challenge in Power BI

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*bReWLRpcJQXY3OrV)

Photo by Luke Chesser on Unsplash

## The Problem

I use the Contoso sample dataset, like in my previous articles. You can download the ContosoRetailDW Dataset for free from Microsoft [here](https://www.microsoft.com/en-us/download/details.aspx?id=18279).

The Contoso Data can be freely used under the MIT License, as described [here](https://github.com/microsoft/Power-BI-Embedded-Contoso-Sales-Demo).

Now, let’s look at the Online Sales Fact table (FactOnlineSales).

When you look at the following picture, you can see that each order has one or more rows. Each row has a SalesOrderLineNumber, and each row has a ProductID.

![Sample data (Image by the author)](https://miro.medium.com/v2/resize:fit:1328/format:webp/1*n0ajQxOpx_20Nw6BSbkGaA.png)

Figure 1 — Sample data (Image by the author)

Now, I have one of the following problems:

- Too much data — I have too much data, and I want to reduce the amount of data to save space and memory to improve performance
- Reporting requirements — I need to create reports based on the Orders and Product Categories.
- I don’t need the highest granularity, and I want to remove the unnecessary details from my data

So, I want to reduce the Granularity from Product to Product Subcategory and from OrderLineNumber to OrderNumber. Because of this reduction, I have to join the Product table to map the Product Subcategory.

This Aggregation will reduce the dataset from 12'627'608 to 3'432'947 rows with retaining the SalesOrderNumber, the CustomerKey and other Dimension references.

You can use one of three methods to reduce the granularity of your data:

1. Change it when retrieving the data from the source system
2. Change it during the import in Power Query
3. Change it in DAX after loading the data in Power BI

From these three variants, I like the first the most.

My Mantra is: “If you need to change your data, do it as early as possible”.

But let’s take a look at each of those variants in detail:

## In the Source system

If your source system is a relational database, write a SQL Query to aggregate your data.

The Aggregation Query will look like this:

```c
SELECT [FOS].[DateKey], [FOS].[StoreKey], [FOS].[PromotionKey], [FOS].[CurrencyKey]
,[FOS].[CustomerKey], [P].[ProductSubcategoryKey], [FOS].[SalesOrderNumber]
,SUM([FOS].[SalesQuantity]) AS [SalesQuantity]
,SUM([FOS].[SalesAmount]) AS [SalesAmount]
,SUM([FOS].[ReturnQuantity]) AS [ReturnQuantity]
,SUM([FOS].[ReturnAmount]) AS [ReturnAmount]
,SUM([FOS].[DiscountQuantity]) AS [DiscountQuantity]
,SUM([FOS].[DiscountAmount]) AS [DiscountAmount]
,SUM([FOS].[TotalCost]) AS [TotalCost]
,SUM([FOS].[UnitCost]) AS [UnitCost]
,SUM([FOS].[UnitPrice]) AS [UnitPrice]
,[FOS].[UpdateDate], [FOS].[DueDate], [FOS].[ShipDate]
FROM [dbo].[FactOnlineSales] AS [FOS]
    LEFT OUTER JOIN [dbo].[DimProduct] AS [P]
        ON [P].[ProductKey] = [FOS].[ProductKey]
GROUP BY [FOS].[DateKey], [FOS].[StoreKey], [FOS].[PromotionKey], [FOS].[CurrencyKey]
, [FOS].[CustomerKey], [P].[ProductSubcategoryKey], [FOS].[SalesOrderNumber]
,[FOS].[UpdateDate], [FOS].[DueDate], [FOS].[ShipDate];
```

I aggregate all Measures with a SUM after analyzing the data. You need to select the correct aggregation function carefully, as a simple SUM is not always the right choice.  
And sometimes, you cannot simply aggregate your data. Possibly you need to do calculations with the aggregated data to get the correct Results.

If the Source is not a relational database, try to prepare the data as much as possible in advance in the source system to reduce the transformation work in Power BI.

Some application allows you to create Aggregation- or Reporting-Views over the data, which you can consume in Power BI.

If none of this is possible, Power Query is the next step.

## Power Query

You can use the Group By function in Power Query to reduce the granularity of your data.

![Group By in Power Query (Figure by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*PsXqIkyyRV6IGDeRXw5Qgw.png)

Figure 2 — Group By in Power Query (Figure by the Author)

This feature calculates the Grouping and Aggregation in Power Query and loads the data into Power BI.

However, this approach has the drawback that the Group By function doesn’t fold the Query back to SQL Server. This means that it has to load the entire dataset in the Power Query Engine. Only after all the data is loaded, it can perform the Grouping and Aggregations.

From the perspective of Power BI, it makes no difference between using a Query/View in the Datasource or Power Query. Power BI still gets only the reduced dataset with the aggregated figures.

## What when you need both granularities?

Sometimes you need to do calculations on both the higher and the lower Granularity levels.

In such a case, you need to have both tables, and you have to change your Data model to accommodate all requirements.

In my case, my PBIX file needed ~15% more space after adding the aggregated table and a new table for the Product Categorizations.

But, sometimes, this is not an option, as you may have much more data in your Fact table, and you cannot simply add one more large table to your model for various reasons.

When you have huge Datasets, you can read my last article on this topic:

## [Change your approach with large datasets in Power BI](https://towardsdatascience.com/change-your-approach-with-large-datasets-in-power-bi-ca488a5b1066?source=post_page-----3a2b81356990---------------------------------------)

### It’s difficult to load huge datasets with hundreds of millions of rows in Power BI Desktop. Let’s take a different…

towardsdatascience.com

On the other side, if you have only a small amount of data, you may want to have only one Fact table, and you want to change the granularity on the fly in a Measure.

Let’s look into this approach.

## Do it in a Measure, and let’s look at the Results

Unfortunately, it’s not trivial to author a Measure while changing the granularity of your data.  
There are a lot of variables to consider.

Let’s look at the following question: What is the Average Sales Amount overall Orders?  
I want to consider the entire orders, not the Sales Amount of each order line. So, I had to aggregate the Sum of SalesAmount per Order number. Then calculate the Average over the result.

The Measure itself is not that difficult:

```c
AvgSalesOverOrders =VAR SalesPerOrder = SUMMARIZE(‘Online Sales’
        ,’Online Sales’[Sales Order Number]
        ,”SalesAmountPerOrder”, SUMX(‘Online Sales’,
                                      [SalesAmount])
)RETURN
AVERAGEX(SalesPerOrder
           ,[SalesAmountPerOrder])
```

My first approach was to use AVERAGE() over the Table Variable SalesPerOrder.  
Unfortunately, AVERAGE can only work with a materialized table, which can also be a DAX table.

But, I didn’t want to create a calculated DAX-table to solve this challenge. I aimed to create a DAX Measure without adding more tables to my data model.

In this case, AVERAGEX() was the solution.

But is the result correct?  
Well, it depends.

As you might have read in one of my last Articles, there are multiple ways to calculate an Average:

## [To weigh or not to weigh — this is the Average question](https://towardsdatascience.com/to-weigh-or-not-to-weigh-this-is-the-average-question-ece33fad9180?source=post_page-----3a2b81356990---------------------------------------)

### Average is a simple calculation. But sometimes, there is more to explore. Let’s take look at this underrated topic

towardsdatascience.com

In this case, it depends on the Granularity of the Data if the result is correct.

I imported the aggregated data, prepared with the Power Query method described above as a new table named “‘Online Sales Aggr” in my data model.

Look at the following Query:

```c
DEFINE
 
MEASURE ‘Online Sales’[AvgSalesOverOrders] = 
    VAR SalesPerOrder = SUMMARIZE(‘Online Sales’
                            ,’Online Sales’[Sales Order Number]
                            ,”SalesAmountPerOrder”
                                ,SUMX(‘Online Sales’, [SalesAmount])
                            )
 
 RETURN
     AVERAGEX(SalesPerOrder
                ,[SalesAmountPerOrder])
 
MEASURE ‘Online Sales Aggr’[AvgSalesOverOrders_Aggr] =
                          AVERAGE(‘Online Sales Aggr’[SalesAmount])
 
EVALUATE
    ROW( “AvgSalesOverOrders”, [AvgSalesOverOrders],
          “AvgSalesOverOrders_Aggr”, [AvgSalesOverOrders_Aggr] )
```

And here is the result:

![Result of two Averages (Image by the author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*WkV1kt38RT-CMF4ZsnS8Qw.png)

Figure 3 — Result of two Averages (Image by the author)

Why are they different?

The first Measure aggregates the Data from the highest granularity, with all the Details, up to each Order Number.  
The second uses the pre-aggregated Data. But this table contains Details per Customer, Stores, promotions, etc. Therefore the table contains much more Details than the table generated in the Measure.  
As a consequence, the Pre-Aggregated Data have lower Numbers in the Sales Amount columns. This is the reason why the Average is lower.

When I change the Granularity of the second Measure to the same level, the result is much more similar.

Here is the full Query:

```c
DEFINE
 
MEASURE ‘Online Sales’[AvgSalesOverOrders] = 
    VAR SalesPerOrder = SUMMARIZE(‘Online Sales’
                             ,’Online Sales’[Sales Order Number]
                             ,”SalesAmountPerOrder”
                                ,SUMX(‘Online Sales’, [SalesAmount])
                                 )
 
RETURN
    AVERAGEX(SalesPerOrder
             ,[SalesAmountPerOrder])

MEASURE ‘Online Sales Aggr’[AvgSalesOverOrders_Aggr] =
                           AVERAGE(‘Online Sales Aggr’[SalesAmount])
 
MEASURE ‘Online Sales’[AvgSalesOverOrders_Aggr_2] = 
    VAR SalesPerOrder = SUMMARIZE(‘Online Sales Aggr’
                            ,’Online Sales Aggr’[Sales Order Number]
                            ,”SalesAmountPerOrder”
                                 ,SUMX(‘Online Sales Aggr’
                                              [SalesAmount])
                             )
 
RETURN
    AVERAGEX(SalesPerOrder
              ,[SalesAmountPerOrder])
 
EVALUATE
    ROW( “AvgSalesOverOrders”, [AvgSalesOverOrders],
          “AvgSalesOverOrders_Aggr”, [AvgSalesOverOrders_Aggr],
          “AvgSalesOverOrders_Aggr_2”, [AvgSalesOverOrders_Aggr_2] )
```

And here is the result:

![Result at Similar Granularity (Image by the author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ikef74ub3O2SJ3dtV1qMNQ.png)

Figure 4 — Result at Similar Granularity (Image by the author)

Anyway, the results can’t be equal as the base values are different.

How the values per row can influence the outcome is only one variable of many. You need to validate the results and change your approach accordingly to get the correct result from your calculations.

## Conclusion

I have shown you three different approaches:

1. Prepare the data in the Source
2. Manipulate the Data in Power Query
3. Create a Measure and change the granularity there

I prefer the first option over the others as, in most cases, it is the most efficient way to do it.

In case that your Source is a database, you can pass a Query to the Source and calculate the aggregations with it.

The second option has some limitations. As mentioned above, Power Query cannot pass the Grouping and Aggregation of the data to SQL Server with [Query folding](https://docs.microsoft.com/en-us/power-query/power-query-folding).

Therefore Power Query will always read the entire dataset and perform the Aggregation in Power Query, taking time and resources.

You have to write a Measure when you want to keep the data at the lowest granularity.  
But caution. This approach can be the least performant solution.

The first Measure shown above took almost two seconds to compute the result in a query showing only the total of the result:

![Timing of Measure on base data (Image by the author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*NkuzyWIO6VooT3rAHxgMsg.png)

Figure 5 — Timing of Measure on base data (Image by the author)

But it takes over 15 seconds when using it in a Matrix:

![Timing of Measure with Matrix (Image by the author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*IPX5lcwyR3oZmZRWDi1XPA.png)

Figure 6 — Timing of Measure with Matrix (Image by the author)

The simpler version of the Measure on the Aggregated data took 65 ms to complete in Power BI:

![Timing of simple Measure on aggregated data (Image by the author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*yfUnNT3nYKxON9dVF5xnfQ.png)

Figure 7 — Timing of simple Measure on aggregated data (Image by the author)

But the last Measure, which calculated the Average in the same way as the first Measure, took just ~25% less time to complete than the first one:

Here from the Query:

![Timing of Measure on aggregated data (Image by the author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*y8cgKYhqr3qu1dTTeSkLPA.png)

Figure 8 — Timing of Measure on aggregated data (Image by the author)

And here in Power BI, with the use of the same Matrix Visual as above:

![Timing of Measure on aggregated data in Matrix (Image by the author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*XkHXiZWTlECiMz9MMbMcjg.png)

Figure 9 — Timing of Measure on aggregated data in Matrix (Image by the author)

The correct solution depends on the requirements of your users. If those are not clear, you need to show them the differences and ask for a concise answer, which version is the correct one.

The Average is only one example of calculations. But you need to clarify the requirement for all calculations bases on aggregated data.

The same applies to the approach to aggregate the data in the first place.

You may load the data twice. Once with all Details and once in an aggregated form to facilitate some calculations.

But, take care of how you perform the aggregations. The wrong method can lead to bad results.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*ZgdNXn2FuBF3f57l)

Photo by Sascha Bosshard on Unsplash

I hope that I was able to give you some inspiration on how to approach such a scenario.

If you appreciate my work, feel free to support me through

## [Salvatore Cagliari](https://buymeacoffee.com/salvatorecagliari?source=post_page-----3a2b81356990---------------------------------------)

### I write technical articles about Data Analysis and Reporting with Power BI. In addition I love building and flying RC…

buymeacoffee.com

Or scan this QR Code:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*btH95UXO7gboS30eZMk6ug.png)

Any support is greatly appreciated.

Thank you.