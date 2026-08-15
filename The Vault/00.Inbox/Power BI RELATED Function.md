---
title: "Power BI RELATED Function"
source: "https://medium.com/microsoft-power-bi/power-bi-related-function-d52c344fab3b"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2023-08-23
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
How to use this powerful command

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*75EogoiOaXoMTzXS1zt21A.png)

## What is the Power BI RELATED function

The Power BI RELATED function is a powerful tool that allows users to quickly and easily access related data from a related table

It is similar in many ways to using lookups in Excel (VLOOKUP), Excel users wanting to learn this function will find the syntax fairly intuitive to follow. In this example we will use the Related function to return a standard cost per mile using a type of vehicle as a lookup reference, to then calculate the costs depending on the mileage covered in each vehicle

## When to use the Related Function in Power BI

If you need to refer to a value in a related table and use that in a calculated column or a measure in another table, in our example we will show it used in a calculated column

The Related function can be used when there is a clear relationship between tables that can return a single row, if a relationship does not exist one must be created

It will not work if the look up would return more than one record, in our example using vehicles types later on in this post, if there was more than one record in the costs a a vehicle type then it would not work

If you have a use case which needs to find a parent category for a specific item it would work, e.g. If I have a product code relating to a pack of socks I can use that code to find a category name for socks as there is likely to be only one record. But if I try to the reverse, return a product code for the socks category, it would be likely that many product codes could be found so it would not work

## How to use the Related Function in Power BI

You can follow the steps in this guide by downloading this data in Excel  
[Power BI RELATED Function](https://www.selectdistinct.co.uk/2023/03/15/power-bi-related-function/power-bi-related-function/)

In the data file we have three data sets

Vehicles — a list of unique vehicles, and their types

Vehicle Types — a list of unique types of vehicle

Miles — a daily list of mileage travelled in each vehicle

Costs — a standard cost per mile for each vehicle

This data set is simplified to help with clarity

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*j4Zmc-NfAsUT8l1R0QuLvQ.png)

We want to be able to report the costs for each vehicle based on the mileage records, using a lookup for the standard cost per mile for each type of vehicle

After we have loaded these data sets to Power BI, the first thing we need to do is to set the relationships

## You need to set the relationships as follows

Vehicle in the Miles tables joins to the Vehicle ID in the Vehicles Table

Type in the Vehicles table joins to the Vehicle Type in the Costs Table

Vehicle Type ID in the Vehicle Types table joins to the Vehicle Type in the Costs table

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*I4ldbCLMOeHvPQafJSkrug.png)

## Now create a table visual on the canvas

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*VQFpLzDZLvuWbyYX15JNsg.png)

Drag a new table visual object to the canvas and bring these fields in

Vehicle from the Miles table, Vehicle Type Name from the Vehicle Types table, Cost per Mile from the Costs table and Sum of the Distance \[mi\] from the Miles table  
Please note: the Distance should default to using a SUM aggregation, but if not you can select the option from the chevron

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*AK4TAJpx2a4f-Q6dHFafWQ.png)

Now, your table should look like this

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*AOkDzJ7RwDLrwQjAfWhq6Q.png)

## Now add the calculated column

On the data pane, select the Miles table and click the New Column icon on the ribbon

Then paste in this DAX code

```c
Mileage Cost = related(Costs[Cost per Mile ])*Miles[Distance [mi]]]
```
```c
press enter and the new column is created
```

## Power BI RELATED Function Explained

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_uXL1pbDGbc3Pg2l3aMLCg.png)

## Errors to avoid with the Related Function in Power BI

The Related function only works when a single value can be returned

It cannot work if there is no clear relationship to return a single value, if a relationship returns many possible results it cannot be used, The solution there is to use RELATEDTABLE and perform a aggregation, this topic will be covered in a future post so it can be fully explained

## Conclusion

The Power BI RELATED function is easy to learn, especially if you have some experience of using LOOKUPS in Excel, and can help to simplify your data modelling

There is not much to go wrong if you focus on getting the correct relationships between your tables

We hope you find this useful

[(38) The Power BI RELATED Function — YouTube](https://www.youtube.com/watch?v=MHWYyQWVQPw)

Subscribe to our channel to see more Power BI tips and timesavers

[https://www.youtube.com/channel/UC\_DiGjuhpRbv6fE8cqD4QBg](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

This post was originally featured in our Business Analytics Blog

[Power BI RELATED Function — Select Distinct](https://www.selectdistinct.co.uk/2023/03/15/power-bi-related-function/)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)