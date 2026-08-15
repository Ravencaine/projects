---
title: "Power BI — narrow Date table range"
source: "https://medium.com/@michalmolka/power-bi-narrow-data-table-range-27b7e6540524"
author:
  - "[[Michal Molka]]"
published: 2020-09-01
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1162/format:webp/1*50JnSO9nCQOBq0WGBkqX6w.png)

Often when we use a customised \[**Date\]** dimension table; we need to deal with date values from related tables which aren’t present inside a dimension.

For example, we have a \[**Date**\] table in a database which years’ range is 1950–2030.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Taf8TZowwhpR4WD43otYQA.png)

I imported two tables into the model, the aforementioned \[**Date**\] table and a \[**Users**\] table from the Stack Overflow Database.

Not every column from the \[**Users**\] table was useful, so I deleted a few and I converted a datetime columns type to date.

```c
let
    Source = Sql.Database("DESKTOP-MM\SQLSERVER2019", "StackOverflow"),
    dbo_Users = Source{[Schema="dbo",Item="Users"]}[Data],
    #"Removed Columns" = Table.RemoveColumns(
        dbo_Users,
        {"Id", "AboutMe", "Age", "DisplayName", "Location", "WebsiteUrl", "AccountId", "EmailHash"}
    ),
    #"Changed Type" = Table.TransformColumnTypes(
        #"Removed Columns",
        {
            {"CreationDate", type date}, 
            {"LastAccessDate", type date}
        }
    )
in
    #"Changed Type"
```

At the end I set two relationships between the tables.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7x3cWjtQoigRJn3uSPfglg.png)

This causes the following issue. When I set a \[**Date**\] table’s \[**Year**\] column as a filter then I see all years from this table. As you see the years’ range in the \[**Users**\] table equals 2008–2019.

![](https://miro.medium.com/v2/resize:fit:1206/format:webp/1*te95UosN7E_CAi1aYB8sKw.png)

There are a lot of ways to solve this problem. This one deals with the \[**Date**\] table on a loading stage. You don’t need to write measures, create filters or set bidirectional relationships.

You can do it through the Power Query (M language). By calculating a minimum and a maximum value from two date columns inside the \[**Users**\] table, converting to year and use as a filter during refreshing data in a model for the \[**Date**\] table.

```c
let
    Source = Sql.Databases("DESKTOP-MM\SQLSERVER2019"),
    StackOverflow = Source{[Name="StackOverflow"]}[Data],
    dbo_Date = StackOverflow{[Schema="dbo",Item="Date"]}[Data],
    dbo_Users = StackOverflow{[Schema="dbo",Item="Users"]}[Data],
    
    Users_Min = 
        Date.Year(
            List.Min(
                {
                List.Min(dbo_Users[CreationDate]),
                List.Min(dbo_Users[LastAccessDate])
                }
            )
        ),
    Users_Max = 
        Date.Year(
            List.Max(
                {
                List.Max(dbo_Users[CreationDate]),
                List.Max(dbo_Users[LastAccessDate])
                }
            )
        ),
    
    dbo_Date_Range = Table.SelectRows(dbo_Date, each [Year] >= Users_Min and [Year] <= Users_Max)
in
    dbo_Date_Range
```

After we applied and refreshed the model, the visualizations look better.

![](https://miro.medium.com/v2/resize:fit:1264/format:webp/1*9nq9xNn9iHF3aF_-il2bKw.png)