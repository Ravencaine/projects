---
title: "Using Detail Rows Expressions to drill to a different fact table in Power BI"
source: "https://blog.crossjoin.co.uk/2026/08/09/using-detail-rows-expressions-to-drill-to-a-different-fact-table-in-power-bi/?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
  - "[[Chris Webb]]"
  - "[[View all posts by Chris Webb]]"
published: 2026-08-09
created: 2026-08-13
description: "Detail Rows Expressions can sometimes offer an alternative to user defined aggregations"
Processed: "Unprocessed"
---
If you have a DirectQuery fact table in Power BI you can use user-defined [aggregations](https://learn.microsoft.com/en-us/power-bi/transform-model/aggregations-advanced) to improve query performance; querying a smaller, summarised copy of your data in an Import mode aggregation table is always going to be faster than querying a large fact table containing all your detail data that is in DirectQuery mode. What’s more a composite model like this can have a much smaller footprint in memory than a model where all your tables are in Import or Direct Lake mode, which means you can use a smaller Fabric capacity SKU. However, in some cases you can take the same tables that you would use to create a composite model like this and solve the same problem slightly differently without using aggregations.

To illustrate, consider the following semantic model:

![](https://i0.wp.com/blog.crossjoin.co.uk/wp-content/uploads/2026/08/image-6.png?w=945&ssl=1)

There are two dimension tables in Dual mode, a totally hidden fact table called SalesDetail in DirectQuery mode which contains transaction-level data:

![](https://i0.wp.com/blog.crossjoin.co.uk/wp-content/uploads/2026/08/image-4.png?w=383&ssl=1)

…and a fact table called SalesSummary in Import mode which contains an aggregated copy of the same data:

![](https://i0.wp.com/blog.crossjoin.co.uk/wp-content/uploads/2026/08/image-5.png?resize=292%2C156&ssl=1)

There is one visible measure called Sales Amount which sums up data from the Sales column on the SalesSummary table:

```
Sales Amount = SUM(SalesSummary[Sales])
```

At this point, an end user would only be able to query data from the SalesSummary table – which would be nice and fast because they are querying the aggregated data. But since the SalesDetail table is hidden there’s no way an end user can query it (or at least query it *easily* because remember, folks, hiding an object is not security). So how can they get at that detailed, transaction-level data that all end users love?

The answer is through the use of Detail Rows Expressions, the finest feature in the whole of Power BI that nobody knows about. Marco has a great article on it [here](https://www.sqlbi.com/articles/controlling-drillthrough-in-excel-pivottables-connected-to-power-bi-or-analysis-services/) that I suggest you read but basically it allows you to configure a DAX table expression associated with a measure that is usually used to show all the rows that contribute to the value that the measure displays. I’m going to use it that way here but the important point about it is that you can use it to return a table expression from anywhere in your semantic model – not just the table where your measure gets its data.

So for example, I can set the Detail Rows Expression on the Sales Amount measure to this:

```sql
SELECTCOLUMNS (
    'SalesDetail',
    "Order ID", 'SalesDetail'[OrderID],
    "Product", 'SalesDetail'[Product],
    "Customer", 'SalesDetail'[Customer],
    "Sales Amount", 'SalesDetail'[Sales]
)
```

Even though the Sales Amount measure sums up data from the Sales column on the **SalesSummary** table, when an end user clicks Show Details on the Sales Amount measure in an Excel PivotTable:

![](https://i0.wp.com/blog.crossjoin.co.uk/wp-content/uploads/2026/08/image-7.png?w=526&ssl=1)

…they can get the detail rows from the **SalesDetail** table showing all the order data for the cell they clicked on:

![](https://i0.wp.com/blog.crossjoin.co.uk/wp-content/uploads/2026/08/image-8.png?w=419&ssl=1)

Thus the Detail Rows Expression allows you to “drill to detail” from the SalesSummary table to the hidden SalesDetail table. This works because the Customer and Product dimension tables are related to both SalesSummary and SalesDetail, so whatever selection has been applied to SalesSummary is also be applied to SalesDetail.

What are the advantages of doing this instead of configuring SalesSummary as an aggregation table? Because data from the SalesDetail table is only available via the Detail Rows Expression feature then it gives you as a semantic model developer a lot more control over how end users access that detail fact data: you can make sure they get the rows they need in the most efficient way because you have total control over the DAX used and you can also prevent them from dumping out large amounts of data by writing controls on how much data can be returned. For example you could write some logic in your Detail Rows Expression that ensures data is only returned if a single date is selected. With this approach users would not be able to drag all the Order IDs into a PivotTable (potentially running a very expensive query) because they could not see the Order ID column to do so.

There are plenty of disadvantages to this technique too though, compared to building aggregations. First and foremost you can only make use of Detail Rows Expressions in Excel PivotTables; I wish we supported them natively in Power BI reports but we don’t. It is possible, however, to use the Paginated Report Visual in a Power BI report to partially work around this limitation and I’ll show you how in my next post. Also, while this allows you to have one Import mode table with aggregated data and one DirectQuery fact table, with aggregations you can have multiple Import mode aggregation tables for a single DirectQuery fact table which can result in even better performance. And of course it might be that you actually want your end users to see and access all the data in your DirectQuery fact table and query it however they want.

This is in fact an old technique I remember from the days of Analysis Services Multidimensional, but it has somehow been forgotten. I wanted to blog about it, though, because as DirectQuery and composite models become more and more important I think it deserves to be used more.