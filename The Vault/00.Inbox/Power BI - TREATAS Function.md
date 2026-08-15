---
title: "Power BI - TREATAS Function"
source: "https://medium.com/@michalmolka/power-bi-treatas-function-f105ed6f8a76"
author:
  - "[[Michal Molka]]"
published: 2020-09-11
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

Today’s post is about the **TREATAS()** function. I will show you a short example how to deal with a data lineage.

Inside tabular models every column has its own lineage — it is a special mark added to a column. The data lineage is operated by the DAX engine during an entire process of data calculations. So, in most cases you don’t have to bother how it works. But there are a few cases when you can take an advantage of it.

Our model is composed of two tables: a \[**Users**\] and a \[**Badges**\] from the Stack Overflowdatabase.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jJRok3PzAL-4GMOqejl6MQ.png)

The first example. When you don’t have a relationship between tables and for some reason you don’t want to create it; you can make a virtual relationship between tables which changes the data lineage. The example below.

```c
Badge Quantity = COUNTROWS(Badges)

//AND

Badge Quantity Treatas = 
  CALCULATE(
    [Badge Quantity],
    TREATAS(
      VALUES(Users[Id]),
      Badges[UserId]
    )
  )
```

As you can see, a standard measure won’t give you a correct result because of lack of a relationship between tables. Implementing the **TREATAS()** function in the second case solves the problem.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ynUDu7Rhgp8Ag3fO-WAa5w.png)

The second example; can occur, when you use the **ADDCOLUMN()** function. In this case additional columns don’t contain a lineage information.

The script below, shows how it works and how you can manage it.

```c
DEFINE
// #1
MEASURE Badges[BadgesCount] =
    CALCULATE (
        COUNTROWS ( Badges )
    )
MEASURE Badges[BadgesValues] =
    CALCULATE (
        VALUES ( Badges[Name] )
    )
EVALUATE
// #2
VAR BadgesFiltered =
    CALCULATETABLE (
        Badges,
        CONTAINSROW (
            {
                "dax",
                "powerbi",
                "azure",
                "azure-storage"
            },
            Badges[Name]
        )
    )
// #3
VAR BadgesSummarised =
    SUMMARIZE (
        BadgesFiltered,
        Badges[Name]
    ) 
// #4
VAR NameColumns =
    ADDCOLUMNS (
        BadgesSummarised,
        "NameNoLineage", Badges[BadgesValues]
    )
// #5
VAR WithLineage =
    SELECTCOLUMNS (
        NameColumns,
        "NameWithLineage", [Name]
    ) 
// #6
VAR WithNoLineage =
    SELECTCOLUMNS (
        NameColumns,
        "NameNoLineage", [NameNoLineage]
    ) 
// #7
VAR NoLineageTreatas =
    TREATAS (
        WithNoLineage,
        Badges[Name]
    )
// #8
VAR BadgesSummaryTable =
    ADDCOLUMNS (
        NoLineageTreatas,
        "BadgesCount", Badges[BadgesCount]
    )
RETURN
    BadgesSummaryTable
```

Firstly, I wrote two simple measures, filtered a table and summarized it: #1, #2, #3

I added a new column, which doesn’t contain information about a lineage: #4

I saved the column with a lineage and with no lineage into two separate variables: #5, #6

Now, we have two columns.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*3dnO27n2Y-pTakuHO7zYAA.png)

When we put the ***WithLineage*** variable in the point #8 then we have an expected result.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*sfc3i_1Fa_ljDfizeXsZyg.png)

In the same point (#8). When we replace the ***WithLineage*** with the ***WithNoLineage*** variable then the result doesn’t look well.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*NPi9Bxj2BFpzffkn_Grt3Q.png)

What can we do? The **TREATAS()** function comes to the rescue. We can add a lineage. Like at the point #7. Now our result looks better.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*sfc3i_1Fa_ljDfizeXsZyg.png)