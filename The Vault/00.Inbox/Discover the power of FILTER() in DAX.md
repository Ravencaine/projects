---
title: "Discover the power of FILTER() in DAX"
source: "https://medium.com/data-science/discover-the-power-of-filter-in-dax-4bfeac3dd786"
author:
  - "[[Salvatore Cagliari]]"
published: 2021-11-22
created: 2026-08-12
description: "The FILTER() function in DAX is potent, but it has some intricacies. Let’s dig into these details to build a good understanding of the FILTER() function."
Processed: "Unprocessed"
---
## The FILTER() function in DAX is potent, but it has some intricacies. Let’s dig into these details to build a good understanding of the FILTER() function.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*JoGsNynVwYzAm-JT)

Photo by Nathan Dumlao on Unsplash

## Introduction

Most of you know something about the FILTER() function in DAX.

But, there are chances that you misuse it or don’t use this function’s full power.

For example, some time ago, I saw a query similar to this:

```c
EVALUATE
    SUMMARIZECOLUMNS(
        ‘Product’[BrandName]
        ,”Sales”, CALCULATE([Sum Online Sales]
            ,FILTER(‘Product’
            ,’Product’[ProductCategoryName] = “Computers”
            )
        )
    )
```

While this query is syntactic correct, it is not optimal.

In the following picture, you can see the Timing information from DAX Studio:

![Timing of Query with FILTER (Figure by Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yLR_Qg3NsJySeiyibhvbNQ.png)

Figure 1 — Timing of Query with FILTER (Figure by Author)

A much better version is this one:

```c
EVALUATE
    SUMMARIZECOLUMNS(
        ‘Product’[BrandName]
        ,”Sales”, CALCULATE([Sum Online Sales]
            ,’Product’[ProductCategoryName] = “Computers”
            )
        )
```

And here is the Server timing without FILTER from DAX Studio:

![Timing of Query without FILTER() (Figure by Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Hc73kyrpJr5ue8VPv5Xweg.png)

Figure 2 — Timing of Query without FILTER() (Figure by Author)

When you look at the SE CPU time, you can see that the second query needs almost half the processing time without FILTER.

And, while the first query needs three storage engine operations to complete, the second query can be processed with only one SE operation.

Let’s look at why this happens and what we can do with the FILTER() function.

## What exactly is FILTER()

The FILTER function is an Iterator like SUMX and the other X-functions.

Consequently, you can use the Row-Context and Context transition to unleash the full power of FILTER().

If you are not familiar with context transition in DAX, look at my article about this topic:

[https://towardsdatascience.com/whats-fancy-about-context-transition-in-dax-efb5d5bc4c01](https://towardsdatascience.com/whats-fancy-about-context-transition-in-dax-efb5d5bc4c01)

The fact that FILTER() is an iterator explains why it’s slower than adding a “normal” filter when using it with CALCULATE() or CALCULATETABLE() as shown above.

But, when you need to work with row-based expressions or filter data based on Measures, you need to use FILTER().

Another fact is that FILTER() returns a table. For this reason, you can use FILTER() to generate filtered tables and use them in your data model or your measures.

## Create a DAX table with FILTER()

Because FILTER() returns a table, you can use it to create a calculated table in Power BI or to query your model. Or you can use the function to create a calculated table in your model.

The following query shows an example with the use of FILTER to query a table and filter the result:

```c
EVALUATE
 FILTER(Store
        ,Store[StoreType] <> “Store”
        )
```

And, as an Iterator, you can use the row context to filter the result:

```c
EVALUATE
 FILTER(‘Online Sales’
   ,’Online Sales’[UnitPrice] * ‘Online Sales’[SalesQuantity] > 1000
   )
```

Of course, this is a very costly query, as the multiplication of the two columns has to be executed for every row in the Online Sales table. But it can be run entirely by the Storage engine and, consequently, use all available CPU cores, which makes this approach very efficient.

While the Storage Engine (SE) can process data on multiple CPU cores, the Formula Engine (FE) can use only one CPU core per query. Thus, whatever can be processed by the SE, is more efficient than the processing with the FE.

Next, we can use context transition to find the Stores, which had more than 1'000'000 of Sales:

```c
EVALUATE
 FILTER(Store
        ,[Sum Retail Sales] > 1000000
        )
```

The possibility to use a Measure to filter a table is handy to calculate results, as we will see in the next section.

But, these queries always return all columns from the filtered table. What if I want to retrieve only a subset of columns?

In this case, I can use a table function to get only the columns I’m interested in.

For example:

```c
EVALUATE
    FILTER(SUMMARIZECOLUMNS(Store[StoreType]
                            ,Store[StoreName]
                            ,Store[StoreManager])
             ,[Sum Retail Sales] > 1000000
             )
```

Here is the result of the query above:

![Query with column selection (Figure by the Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hXDOqq54r3OaE-dEzohUIw.png)

Figure 3 — Query with column selection (Figure by the Author)

FILTER() accepts all table functions as the first parameter.

## Use in CALCULATE() and CALCULATETABLE()

CALCULATE() and CALCULATETABLE() accepts tables as filter parameter.

Due to this fact, you can generate a table with FILTER() and modify the result of the measure with this mechanism.

Look at the following query with the measure \[Large Stores\]:

```c
DEFINE
 MEASURE ‘All Measures’[Large Stores] =
          CALCULATE([Sum Retail Sales]
                     ,FILTER(Store
                             ,[Sum Retail Sales] > 100000000
                             )
                     )
 
 EVALUATE
 CALCULATETABLE(
                SUMMARIZECOLUMNS(Store[StoreName]
                      ,”Sales”, [Sum Retail Sales]
                      ,”Is large Store”, IF([Large Stores]>0
                                              ,TRUE(), FALSE())
                      )
                      ,’Date’[Year] = 2020
                )
 ORDER BY [Is large Store] DESC, [Sum Retail Sales] DESC
```

This query aims to find all Stores with a Sales Amount over 100'000'000 ($, €, or whatever) in 2020.

See the following picture for the result of the query:

![Result of measure with FILTER() (Figure by the Author)](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*9FmiuLAQ9XeJMyf-SKKeuw.png)

Figure 4 — Result of measure with FILTER() (Figure by the Author)

Let’s analyse what’s happening here:

1. The query uses SUMMARIZECOLUMNS() to generate a list of all Stores
2. CALCULATETABLE() is used to add a filter for the year 2020
3. I call the \[Sum Retail Sales\] measure to get the sales for each Store for 2020
4. I call the measure \[Large Stores\] and check the result if it’s larger than 0  
	a. If yes, I return TRUE()  
	b. If no, I return FALSE()

The measure uses the existing filter context to calculate the result. The filter context contains the filter for the year 2020.

The FILTER() function considers this filter when evaluating the list of stores with more than 100'000'000 sales.  
FILTER() returns a list of Stores, which are above the threshold.

CALCULATE() perform the calculation of \[Sum Retail Sales\] only for those Stores, as the result of FILTER() is used as a filter-modifier in the measure.  
Therefore we can use a check in the query, like IF(\[Large Stores\]>0,TRUE(), FALSE()), to generate the desired output.

## Take care on context transition

Context transition is an important topic when you’re working with FILTER().

Let’s assume that we want to filter our Sales transactions to get only the rows, which have a value of 1000 or more.

You might be tempted to use FILTER() to construct a table and use this table as a source for SUMX():

```c
Large Sales Amount =SUMX(
    FILTER(
           ‘Retail Sales’
  ,’Retail Sales’[SalesQuantity] * ‘Retail Sales’[UnitPrice] >= 1000
  )
  ,[Sum Retail Sales]
 )
```

Here, I use FILTER() to generate a list of transactions above the threshold mentioned above.

While the result might be correct, I’m triggering a context transition by calling the \[Sum Retail Sales\] measure inside SUMX.

A better and faster approach is the following measure:

```c
Large Sales Amount =CALCULATE (
 [Sum Retail Sales],
   FILTER (
           ALL ( ‘Retail Sales’[SalesQuantity]
                 ,‘Retail Sales’[UnitPrice] ),
   ‘Retail Sales’[SalesQuantity] * ‘Retail Sales’[UnitPrice] >= 1000
   )
 )
```

Here I use the measure in CALCULATE(), and I use FILTER() to apply a filter on the ‘OnlineSales’ table to calculate the desired result.

The difference in performance is dramatic, as you can see in the following picture:

![Comparison of good vs bad FILTER() usage (Figure by Author)](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Hb6FITWHMtohvAwTYz2wsw.png)

Figure 5 — Comparison of good vs bad FILTER() usage (Figure by Author)

The first measurement shows the timing and query plan of the first measure with SUMX() and FILTER(). Below, you can see the timing of the second measure with CALCULATE() and FILTER().

The reason is visible in the Query plan, where you can see that the query processes 1'451'337 rows twice. In addition, two CallbackDataID steps are executed, which pushes data between the formula and the storage engine. These operations are very costly.

## Conclusion

The FILTER() function is essential for your DAX toolbelt.

You need to understand his capabilities and the potential issues when using this function.

But, it gives you a lot of opportunities for enhancing your DAX expressions.

As a summary:

- FILTER() is an iterator
- FILTER() returns a table
- FILTER() can be used in CALCULATE() to set the filter context
- You can use context transition in FILTER()
- If not used properly, you can slow down your DAX expressions

As soon as you understand this function correctly, you can start using it at the right places and unleash the full power of FILTER().

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*-p3cvM3c-Bosb4Rj)

Photo by David Suarez on Unsplash

## References

The FILTER() function is described on this page: [FILTER — DAX Guide](https://dax.guide/filter/)

This page has an embedded video with further information and examples.

Information about what to avoid when using FILTER() in CALCULATE(), can be found here: [Avoid using FILTER as a filter argument in DAX — DAX | Microsoft Docs](https://docs.microsoft.com/en-us/dax/best-practices/dax-avoid-avoid-filter-as-filter-argument)

I use the Contoso sample dataset, like in my previous articles. You can download the ContosoRetailDW Dataset for free from Microsoft [here](https://www.microsoft.com/en-us/download/details.aspx?id=18279).

The Contoso Data can be freely used under the MIT License, as described [here](https://github.com/microsoft/Power-BI-Embedded-Contoso-Sales-Demo).

I enlarged the dataset to make the DAX engine work harder.  
The Online Sales table contains 63 million rows (instead of 12.6 million rows), and the Retail Sales table contains 15.5 million rows (instead of 3.4 million rows).

## [Join Medium with my referral link - Salvatore Cagliari](https://medium.com/@salvatorecagliari/membership?source=post_page-----4bfeac3dd786---------------------------------------)

### As a Medium member, a portion of your membership fee goes to writers you read, and you get full access to every story…

medium.com

If you appreciate my work, feel free to support me through

## [Salvatore Cagliari](https://buymeacoffee.com/salvatorecagliari?source=post_page-----4bfeac3dd786---------------------------------------)

### I write technical articles about Data Analysis and Reporting with Power BI. In addition I love building and flying RC…

buymeacoffee.com

Or scan this QR Code:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*btH95UXO7gboS30eZMk6ug.png)

Any support is greatly appreciated.

Thank you.