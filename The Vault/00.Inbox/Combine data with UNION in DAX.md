---
title: "Combine data with UNION in DAX"
source: "https://medium.com/microsoft-power-bi/combine-data-with-union-in-dax-aabd5de104a0"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2023-11-13
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*toXiqQucs5Jz0hm1.png)

Using UNION in DAX is a another option to combine data for analysis in Power BI

We recently showed how to do this in SQL

[UNION in SQL](https://www.selectdistinct.co.uk/2023/09/21/union-in-sql/)

and how to do similar in Power Query  
[APPEND in Power Query](https://www.selectdistinct.co.uk/2023/09/27/append-data-in-power-query/)

It isn’t always possible to do this in SQL such as if the datasets are coming from separate systems, and depending on the circumstances you may not want to do it in Power Query either.

Doing it using DAX in Power BI to create the table is another alternative

## UNION in DAX Syntax

Before you can use the DAX command, the tables you want to union must be in the data model

We will use the same two sample data tables that we used for the Append example last week

the first covers store numbers 1 to 5 (SalesA)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*vN_8tWHWCSrGspni.png)

And the second covering store numbers 5 to 10 (SalesB)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*wGL6Ut29aoUpKpeh.png)

to create a new UNION table, go into the table view pane and click ‘New Table’

![](https://miro.medium.com/v2/resize:fit:1204/format:webp/0*Brjf1JeBYthVtrr7.png)

The syntax for the UNION function is

New Table Name = UNION(table1,table2)

We will call the new table ‘Sales Combined’

In the DAX formula bar we enter

```c
Sales Combined = UNION(SalesA,SalesB)
```
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*9Te2h3s0fm5RQpM7.png)

Once you press enter the DAX code runs and the new table is produced

We can see that the new table contain all 5 rows from SalesA and all 5 rows of SalesB

This is very straight forward in this example and simply combines the two datasets in a simple way

If you look carefully you can see that Store 5 Product 1 does have the same data for now we will assume these are not duplicates, but we will return to this to show how to deal with duplicates

## Important points to note

For UNION to work there are a few considerations that must be in place, and these are essentially the same as UNION ALL in SQL

1. The columns MUST be in the same order in both tables, if they are not it is possible that the UNION could still run, but give strange mixed results
2. The data types of the columns must be compatible
3. Column names are inherited from the first table, they do not have to be the same
4. Tables must have the same number of columns
5. Duplicates are not eliminated (we will explore this)

## How to remove duplicates?

To demonstrate this we firstly need to remove our Source column

```c
SELECTCOLUMNS(SalesA,"Product_ID",SalesA[Product_ID], "Store_ID", SalesA[Store_ID], "qty_sold", SalesA[qty_sold])
```

This DAX code just selects the three columns we need

We repeat this for both tables, then apply this into the union

```c
Sales Combined = 
union
(SELECTCOLUMNS(SalesA,"Product_ID",SalesA[Product_ID], 
"Store_ID", SalesA[Store_ID], "qty_sold", SalesA[qty_sold])
,SELECTCOLUMNS(SalesB,"Product_ID",SalesB[Product_ID]
, "Store_ID", SalesB[Store_ID], "qty_sold", SalesB[qty_sold])
)
```

We now see the 10 rows without the source column

To remove the duplicate for store 5, we can now use the DISTINCT command

```c
Sales Combined = 
DISTINCT
(union
(SELECTCOLUMNS(SalesA,"Product_ID",SalesA[Product_ID], 
"Store_ID", SalesA[Store_ID], "qty_sold", SalesA[qty_sold])
,SELECTCOLUMNS(SalesB,"Product_ID",SalesB[Product_ID]
, "Store_ID", SalesB[Store_ID], "qty_sold", SalesB[qty_sold])
)
)
```

This results in 9 rows

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*KTmzLTEKtwBRsnt0.png)

You can see here that other table based operations can be used within UNION, here we use the select columns to only select the relevant columns for the union

This method would work with tables which have a different number of columns

## UNION with more than two tables

Union needs to have at least 2 table references, but it is not limited to a fixed number

If we want to union three tables we just add more

***Sales Combined Three = UNION(SalesA,SalesB,SalesA)***

This example also shows that you can repeat the same table if you need to

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*GCLDqG-x_Bgv2OXYfcqhKw.png)

## Conclusion

With this third way to combine data tables in Power BI you are now equipped to perform your data consolidation

Having a seamless integration of multiple tables or queries is a great way to simplify onward analysis

Subscribe to our channel to see more SQL tips and timesavers

[Select Distinct YouTube Channel](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)